#!/usr/bin/env python3
"""
Setup script for CodingYok Programming Language
"""

from setuptools import setup, find_packages

# Read README for long description
def read_readme():
    try:
        with open("README.md", "r", encoding="utf-8") as fh:
            return fh.read()
    except FileNotFoundError:
        return "CodingYok - Bahasa Pemrograman Indonesia"

# Read requirements
def read_requirements():
    try:
        with open("requirements.txt", "r", encoding="utf-8") as fh:
            return [line.strip() for line in fh if line.strip() and not line.startswith("#")]
    except FileNotFoundError:
        return []

setup(
    name="codingyok",
    version="2.0.0",
    author="MrXploisLite",
    author_email="108934584+MrXploisLite@users.noreply.github.com",
    description="Bahasa pemrograman modern dengan keyword bahasa Indonesia - Now with Comprehensions, Generators, and Pattern Matching!",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/MrXploisLite/CodingYok",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Interpreters",
        "Topic :: Software Development :: Compilers",
        "Natural Language :: Indonesian",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "mypy>=0.900",
            "flake8>=3.8",
            "pre-commit>=2.0",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
            "myst-parser>=0.15",
        ],
    },
    entry_points={
        "console_scripts": [
            "codingyok=codingyok.cli:main",
            "cy=codingyok.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "codingyok": ["stdlib/*.cy", "stdlib_modules/*.cy", "examples/*.cy"],
    },
    project_urls={
        "Bug Reports": "https://github.com/MrXploisLite/CodingYok/issues",
        "Source": "https://github.com/MrXploisLite/CodingYok",
        "Documentation": "https://github.com/MrXploisLite/CodingYok/wiki",
    },
    keywords="programming-language indonesia interpreter python-like",
    zip_safe=False,
)
