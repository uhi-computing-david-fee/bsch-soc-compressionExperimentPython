# compression_algorithm.py
#
# Contains compression algorithm implementations.
#
# RLE is supplied as the baseline algorithm.
# Your task is to implement fixed length encoding in the stub below.
#
# Cost model:
#   RLE:          16 bits per run (8 bits for count + 8 bits for character)
#   Fixed length: input length * bits_per_character

BITS_PER_RUN = 16


# ---------------------------------------------------------------
# RLE — supplied implementation
# ---------------------------------------------------------------

def rle_compress(input_text: str) -> tuple[str, int, int]:
    """
    Compresses input using run length encoding.

    Returns a tuple of:
        encoded          - human-readable encoded string (e.g. "4A3B2C")
        run_count        - number of runs produced
        compressed_bits  - compressed size in bits using 16 bits per run
    """
    if not input_text:
        return "", 0, 0

    encoded = []
    i = 0

    while i < len(input_text):
        current_char = input_text[i]
        count = 1

        while i + count < len(input_text) and input_text[i + count] == current_char:
            count += 1

        encoded.append(f"{count}{current_char}")
        i += count

    encoded_string = "".join(encoded)
    run_count = len(encoded)
    compressed_bits = run_count * BITS_PER_RUN

    return encoded_string, run_count, compressed_bits


def rle_decompress(encoded: str) -> str:
    """
    Decompresses an RLE encoded string.
    """
    result = []
    i = 0

    while i < len(encoded):
        count_start = i
        while i < len(encoded) and encoded[i].isdigit():
            i += 1

        count = int(encoded[count_start:i])
        character = encoded[i]
        i += 1

        result.append(character * count)

    return "".join(result)


# ---------------------------------------------------------------
# Fixed Length Encoding — your implementation goes here
# ---------------------------------------------------------------

def fixed_length_compress(input_text: str) -> tuple[str, dict[str, str], int, int]:
    """
    Compresses input using fixed length binary encoding.

    Every character in the input alphabet is assigned a unique binary
    code of equal length. The number of bits per character is the
    smallest k such that 2^k is greater than or equal to the number
    of distinct characters in the input.

    Returns a tuple of:
        encoded          - binary string representation of the compressed input
        code_table       - dictionary mapping each character to its binary code
        bits_per_char    - number of bits used per character
        compressed_bits  - compressed size in bits (input length * bits_per_char)

    See the fixed length encoding tutorial articles for implementation
    guidance including how to calculate bits per character and how to
    build the code table.
    """
    # TODO: Implement fixed length encoding.
    raise NotImplementedError("Implement fixed length encoding here.")


def fixed_length_decompress(encoded: str, code_table: dict[str, str], bits_per_char: int) -> str:
    """
    Decompresses a fixed length encoded binary string using the provided code table.
    """
    # TODO: Implement fixed length decoding.
    raise NotImplementedError("Implement fixed length decoding here.")