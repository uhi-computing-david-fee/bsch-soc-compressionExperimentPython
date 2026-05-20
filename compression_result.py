# compression_result.py
#
# Data class holding the result of a single compression experiment run.
# RunCount is None for fixed length encoding since it does not produce runs.
# You do not need to modify this file.

from dataclasses import dataclass
from typing import Optional


@dataclass
class CompressionResult:
    scheme: str
    input_description: str
    input_length: int
    distinct_characters: int
    original_size_bits: int
    compressed_size_bits: int
    compression_ratio: float
    run_count: Optional[int]

    @classmethod
    def create(cls, scheme, input_description, input_length,
               distinct_characters, original_size_bits,
               compressed_size_bits, run_count):
        ratio = (original_size_bits / compressed_size_bits
                 if compressed_size_bits > 0 else 0.0)
        return cls(
            scheme=scheme,
            input_description=input_description,
            input_length=input_length,
            distinct_characters=distinct_characters,
            original_size_bits=original_size_bits,
            compressed_size_bits=compressed_size_bits,
            compression_ratio=ratio,
            run_count=run_count
        )