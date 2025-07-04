#!/usr/bin/env python3
"""
Setup script for ImageFlow
"""

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [
        line.strip() for line in fh if line.strip() and not line.startswith("#")
    ]

setup(
    name="imageflow",
    version="2.0.0",
    author="Alan Steinbarth",
    description="ImageFlow - Universal image converter with cross-platform support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["app"],
    python_requires=">=3.8",
    install_requires=requirements,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
    ],
    entry_points={
        "console_scripts": [
            "image-converter=app:main",
        ],
    },
)
