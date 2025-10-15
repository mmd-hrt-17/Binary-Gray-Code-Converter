# **Gray Code Converter (CLI)**

A simple Python CLI for converting between Gray Code and Binary.

------------------------------------------

**Features**

Convert Gray → Binary and Binary → Gray.

Uses colorama for colored terminal output.

------------------------------------------

**Requirements**

Python 3.8+

colorama 0.4.8

------------------------------------------

**Installation**

python -m venv .venv  # Optional but recommended

source .venv/bin/activate  # macOS/Linux

.venv\Scripts\activate  # Windows

pip install -r requirements.txt

------------------------------------------

**Quick Start**

python Converter.py

------------------------------------------

**Usage**

Gray → Binary

Binary → Gray

As a Library:

from Converter import Gray_to_Binary, Binary_to_Gray

print(Gray_to_Binary("1101"))  # => "1011"

print(Binary_to_Gray("1011"))  # => "1101"
