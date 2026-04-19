"""HamNoSys to SiGML conversion utilities."""

from __future__ import annotations

import re
import xml.dom.minidom
import xml.etree.ElementTree as ET
from importlib.resources import files
from typing import Dict, List, Optional


class HamToSigml:
    """Convert HamNoSys tokens into SiGML XML."""

    def __init__(self) -> None:
        self._tag_by_code, self._tag_by_name = self._load_dictionary()

    def _load_dictionary(self) -> tuple[Dict[str, str], Dict[str, str]]:
        data_path = files("hamnosys.data").joinpath("conversion_dict.txt")
        tag_by_code: Dict[str, str] = {}
        tag_by_name: Dict[str, str] = {}

        with data_path.open("r", encoding="utf-8") as handle:
            for raw_line in handle:
                line = raw_line.strip()
                if not line or "," not in line:
                    continue

                tag, code = [part.strip() for part in line.split(",", maxsplit=1)]
                tag_lower = tag.lower()
                code_upper = code.upper()

                tag_by_code[code_upper] = tag_lower
                tag_by_name[tag_lower] = tag_lower

        return tag_by_code, tag_by_name

    def _tokenize(self, ham_code: str) -> List[str]:
        raw_parts = re.split(r"[\s,;]+", ham_code.strip())
        tokens = []
        for part in raw_parts:
            if not part:
                continue
            # If it's a known name, keep it as one token
            if part.lower() in self._tag_by_name:
                tokens.append(part)
                continue
            
            # If it looks like a hex code (e.g., E000, U+E000, \uE000)
            if re.fullmatch(r"(?i)(U\+|\\U)?[0-9A-F]{4}", part):
                tokens.append(part)
                continue
                
            # If it's a continuous string of hex codes like "E000E001"
            if len(part) % 4 == 0 and re.fullmatch(r"(?i)[0-9A-F]+", part):
                for j in range(0, len(part), 4):
                    tokens.append(part[j:j+4])
                continue

            # Otherwise, treat it as a sequence of raw unicode characters
            for char in part:
                tokens.append(char)
                
        return tokens

    def _normalize_code_token(self, token: str) -> Optional[str]:
        candidate = token.strip().upper()

        if candidate.startswith("U+"):
            candidate = candidate[2:]
        elif candidate.startswith("\\U") and len(candidate) == 6:
            candidate = candidate[2:]

        if re.fullmatch(r"[0-9A-F]{4}", candidate):
            return candidate

        if len(token) == 1:
            return f"{ord(token):04X}"

        return None

    def _resolve_tag(self, token: str) -> str:
        normalized_name = token.strip().lower()
        if normalized_name in self._tag_by_name:
            return self._tag_by_name[normalized_name]

        normalized_code = self._normalize_code_token(token)
        if normalized_code and normalized_code in self._tag_by_code:
            return self._tag_by_code[normalized_code]

        raise ValueError(f"Unknown HamNoSys token: {token}")

    def convert(self, ham_code: str, gloss: Optional[str] = None) -> str:
        """Convert a HamNoSys code string into SiGML XML."""
        if not isinstance(ham_code, str) or not ham_code.strip():
            raise ValueError("ham_code must be a non-empty string")

        tokens = self._tokenize(ham_code)
        if not tokens:
            raise ValueError("No HamNoSys tokens found in ham_code")

        tags = [self._resolve_tag(token) for token in tokens]

        root = ET.Element("sigml")
        sign = ET.SubElement(root, "hns_sign")
        if gloss is not None:
            sign.set("gloss", str(gloss))

        ET.SubElement(sign, "hamnosys_nonmanual")
        manual = ET.SubElement(sign, "hamnosys_manual")

        for tag in tags:
            ET.SubElement(manual, tag)

        xml_bytes = ET.tostring(root, encoding="utf-8")
        parsed = xml.dom.minidom.parseString(xml_bytes)
        return parsed.toprettyxml(indent="  ", encoding="UTF-8").decode("utf-8")
