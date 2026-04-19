from pathlib import Path
from setuptools import find_packages, setup


def read_version():
    ns = {}
    path = Path("hamnosys") / "_version.py"
    with path.open("r", encoding="utf-8") as f:
        exec(f.read(), ns)
    return ns["__version__"]


version = read_version()

setup(
    name="hamnosys",
    version=version,
    description="A Python library for converting HamNoSys codes to SiGML.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Mohamed Yehia",
    url="https://github.com/24-mohamedyehia/hamnosys",
    packages=find_packages(),
    python_requires=">=3.10",
    include_package_data=True,
    package_data={"hamnosys": ["data/*.txt"]},
    install_requires=[
    ],
    extras_require={
        "dev": [
            "notebook==6.5.4",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
