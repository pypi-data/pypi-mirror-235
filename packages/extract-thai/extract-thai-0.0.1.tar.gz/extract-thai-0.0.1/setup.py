from setuptools import setup, find_packages

setup(
    name="extract-thai",
    version="0.0.1",
    author="JayTrairat",
    author_email="jay.trairat@gmail.com",
    description="Thai Text Extractor from Images",
    packages=find_packages(),
    install_requires=[
        "Pillow",
        "pytesseract",
    ],
    entry_points={
        "console_scripts": [
            "extract-thai = extract_thai.extract_thai:main",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
