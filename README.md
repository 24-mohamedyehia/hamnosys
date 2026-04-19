<div align="center">

<img src="https://raw.githubusercontent.com/24-mohamedyehia/hamnosys/main/public/banner.svg" alt="HamNoSys Banner" width="100%"/>

<p>
  <a href="https://pypi.org/project/hamnosys/"><img src="https://img.shields.io/pypi/v/hamnosys.svg" alt="PyPI Version"></a>
  <img src="https://img.shields.io/badge/python-3.9%2B-blue.svg" alt="Python Versions">
  <a href="https://github.com/24-mohamedyehia/hamnosys/blob/main/LICENSE"><img src="https://img.shields.io/github/license/24-mohamedyehia/hamnosys.svg" alt="License"></a>
</p>

# 🤟 hamnosys

A lightweight Python library for converting HamNoSys tokens into SiGML XML.

</div>

---

## ✨ Features

- **Robust Tokenization:** Handles individual hex codes, names, or contiguous raw unicode streams smoothly.
- **Fast Dictionary Lookups:** In-memory conversion map loaded once for rapid sequence mapping.
- **Customizable Glosses:** Easily append optional semantic word glosses to the SiGML output.
- **Standardized XML:** Formats and pretty-prints SiGML suitable for direct avatar rendering.

## 📦 Installation

### Option 1: Install the library to use it

```bash
pip install hamnosys
```

Or install it directly from GitHub:

```bash
python -m pip install "git+https://github.com/24-mohamedyehia/hamnosys.git"
```

## 🚀 Basic Usage

```python
from hamnosys import HamToSigml

converter = HamToSigml()

ham_code = ""
word = "again"

sigml_result = converter.convert(ham_code, gloss=word)
print(sigml_result)
```

## 🤝 Contributing
Contributing to this project is welcome! Please feel free to submit issues or pull requests on GitHub.

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgements
Special thanks to the [Institute of German Sign Language and Communication of the Deaf (IDGS) at the University of Hamburg](https://www.sign-lang.uni-hamburg.de/dgs-korpus/index.php/hamnosys-97.html) for developing and releasing the **Hamburg Notation System (HamNoSys)**, which is the foundational phonetic transcription system for sign languages used in this toolkit.
