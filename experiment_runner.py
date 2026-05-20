# experiment_runner.py
#
# Runs compression experiments on a given input string or file,
# applying both RLE and fixed length encoding and recording results.

import os
from compression_algorithm import rle_compress, rle_decompress, fixed_length_compress, fixed_length_decompress
from compression_result import CompressionResult


def run(input_text: str, input_description: str) -> list[CompressionResult]:
    """
    Runs both compression schemes on the provided input string.
    Returns one CompressionResult per scheme.
    """
    results = []

    input_length = len(input_text)
    distinct_characters = len(set(input_text))
    original_size_bits = input_length * 8

    # --- RLE ---
    print("  Running RLE...")
    encoded, run_count, rle_compressed_bits = rle_compress(input_text)
    decoded = rle_decompress(encoded)

    if decoded != input_text:
        print("  WARNING: RLE decode does not match original input.")

    results.append(CompressionResult.create(
        scheme="RLE",
        input_description=input_description,
        input_length=input_length,
        distinct_characters=distinct_characters,
        original_size_bits=original_size_bits,
        compressed_size_bits=rle_compressed_bits,
        run_count=run_count
    ))

    print(f"  RLE complete. Runs: {run_count}, "
          f"Compressed: {rle_compressed_bits} bits, "
          f"Ratio: {original_size_bits / rle_compressed_bits:.4f}")

    # --- Fixed Length Encoding ---
    print("  Running Fixed Length Encoding...")

    try:
        fl_encoded, code_table, bits_per_char, fl_compressed_bits = fixed_length_compress(input_text)
        fl_decoded = fixed_length_decompress(fl_encoded, code_table, bits_per_char)

        if fl_decoded != input_text:
            print("  WARNING: Fixed length decode does not match original input.")

        results.append(CompressionResult.create(
            scheme="FixedLength",
            input_description=input_description,
            input_length=input_length,
            distinct_characters=distinct_characters,
            original_size_bits=original_size_bits,
            compressed_size_bits=fl_compressed_bits,
            run_count=None
        ))

        print(f"  Fixed length complete. Bits per char: {bits_per_char}, "
              f"Compressed: {fl_compressed_bits} bits, "
              f"Ratio: {original_size_bits / fl_compressed_bits:.4f}")

    except NotImplementedError:
        print("  Fixed length encoding not yet implemented.")

    return results


def run_from_file(file_path: str, input_description: str) -> list[CompressionResult]:
    """
    Loads a text file and runs both compression schemes on its contents.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Input file not found: {file_path}")

    with open(file_path, "r") as f:
        input_text = f.read()

    return run(input_text, input_description)