# result_reporter.py
#
# Writes compression experiment results to a CSV file.
# Results are appended if the output file already exists.

import os
from compression_result import CompressionResult


def write_results(results: list[CompressionResult], output_file: str) -> None:
    """
    Appends a list of CompressionResult objects to the specified CSV file.
    Creates the file with a header row if it does not already exist.
    """
    os.makedirs(os.path.dirname(output_file) if os.path.dirname(output_file) else ".", exist_ok=True)

    file_exists = os.path.isfile(output_file)

    with open(output_file, "a") as f:
        if not file_exists:
            f.write("Scheme,InputDescription,InputLength,DistinctCharacters,"
                    "OriginalSizeBits,CompressedSizeBits,CompressionRatio,RunCount\n")

        for r in results:
            f.write(
                f"{r.scheme},"
                f"{r.input_description},"
                f"{r.input_length},"
                f"{r.distinct_characters},"
                f"{r.original_size_bits},"
                f"{r.compressed_size_bits},"
                f"{r.compression_ratio:.4f},"
                f"{r.run_count if r.run_count is not None else 'N/A'}\n"
            )