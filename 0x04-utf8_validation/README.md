# 0x04-utf8_validation

## Overview

This project implements the validUTF8(data) function to determine whether a given dataset represents valid UTF-8 encoding. The algorithm checks the patterns of starting bytes and continuation bytes to ensure they conform to the UTF-8 encoding standards.

## Background
### ASCII
* ASCII (American Standard Code for Information Interchange) is an encoding standard that uses 7 bits to represent characters. It can encode 128 characters, including control characters, punctuation, digits, and English letters. ASCII uses a single byte (8 bits) with the most significant bit (MSB) set to 0, leaving 7 bits for character representation.

### Unicode
* Unicode is a universal character encoding standard that aims to cover all characters used in writing systems around the world. It assigns a unique code point to each character, regardless of the platform, program, or language. Unicode provides a comprehensive character set and can represent over 1.1 million characters.

### UTF-8
* UTF-8 (8-bit Unicode Transformation Format) is a variable-width character encoding for Unicode. It is designed to encode Unicode characters in a way that is backward-compatible with ASCII while supporting a wide range of characters.
UTF-8 uses one to four bytes to encode characters:

- 1 byte (0xxxxxxx): Represents ASCII characters (0-127).
- 2 bytes (110xxxxx 10xxxxxx): Represents additional characters (128-2047).
- 3 bytes (1110xxxx 10xxxxxx 10xxxxxx): Represents even more characters (2048-65535).
- 4 bytes (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx): Represents characters beyond the Basic Multilingual Plane (65536-1114111).

For further reading, these resources were particularly helpful in understanding the concepts:

[Characters, Symbols, and the Unicode Miracle](https://www.youtube.com/watch?v=MijmeoH9LT4)


[The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)


## Function: validUTF8(data)
The validUTF8(data) function verifies if the given list of integers represents valid UTF-8 encoded data.

* Parameters
  -  data (list of integers): A list where each integer represents a byte in the UTF-8 encoded data.
 * Returns
  - True if the data is valid UTF-8 encoding.
  - False otherwise.
* Algorithm
Starting Byte Detection:

Determines if a byte is a valid starting byte for a UTF-8 character and sets the number of continuation bytes required.
Continuation Byte Validation:

Checks that each continuation byte starts with 10 and decrements the counter for expected continuation bytes.
Final Validation:

Ensures that all expected continuation bytes are accounted for by the end of the dataset.

* Example

`` data = [229, 65] ``
`` print(validUTF8(data)) `` # Output: True
This function will return True if the data list conforms to UTF-8 encoding rules and False otherwise.
