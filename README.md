# Compression Experiment (Python)

A console application for running controlled compression experiments and recording results to CSV. Built for the Science of Computing & Digital Media (UI110010) UHI BSc Hons, core exercise six.

## Purpose

This application lets you compress strings or text files using two schemes, run length encoding and fixed length encoding, and record compression ratio data for analysis. RLE is supplied as the baseline implementation. Your task is to implement fixed length encoding and design a series of experiments that reveal how input characteristics affect compression performance.

## Project Structure

| File | Purpose |
|------|---------|
| `main.py` | Entry point and menu-driven interface |
| `compression_algorithm.py` | Compression algorithm implementations |
| `experiment_runner.py` | Runs both schemes and records results |
| `result_reporter.py` | Writes results to CSV |
| `compression_result.py` | Dataclass holding the result of a single run |

## Getting Started

Requires Python 3.10 or later.

```bash
python main.py
```

The application will present a menu. You can compress a string entered directly or load a text file.

## Compression Schemes

### RLE — Run Length Encoding
Supplied and ready to use. Replaces consecutive repeated characters with count-character pairs. Compressed size is measured using a fixed cost model of 16 bits per run (8 bits for count, 8 bits for character).

### Fixed Length Encoding
Your implementation. Assigns every character in the input alphabet a unique binary code of equal length, using only as many bits as needed to represent the alphabet. See the tutorial articles for implementation guidance.

## Cost Model

Both schemes measure compressed size in bits using a consistent model:

| Scheme | Cost Model |
|--------|-----------|
| RLE | 16 bits per run |
| Fixed Length | input length × bits per character |

Original size is always input length × 8 bits (ASCII).

## CSV Output

Results are written to CSV with the following columns:

| Column | Description |
|--------|-------------|
| `Scheme` | RLE or FixedLength |
| `InputDescription` | Short description you provide when running |
| `InputLength` | Number of characters in the input |
| `DistinctCharacters` | Number of distinct characters in the input |
| `OriginalSizeBits` | Original size in bits |
| `CompressedSizeBits` | Compressed size in bits |
| `CompressionRatio` | OriginalSizeBits / CompressedSizeBits |
| `RunCount` | Number of runs (RLE only, N/A for fixed length) |

## Where to Extend

Open `compression_algorithm.py`. Implement `fixed_length_compress` and `fixed_length_decompress` following the guidance in the docstrings. The tutorial articles on fixed length encoding cover the bit calculation and code table construction in detail.

Verify your implementation by confirming that `fixed_length_decompress(*fixed_length_compress(input)[:3])` returns the original input, and that your compression ratios match the predictions you can calculate by hand from the alphabet size.

## Sample Data

Four sample files are included in the `data/` directory:

| File | Description |
|------|-------------|
| `sample_high_repetition.txt` | Long runs of repeated characters |
| `sample_low_repetition.txt` | Alternating pattern, minimal repetition |
| `sample_natural_text.txt` | Natural English style text |
| `sample_small_alphabet.txt` | Small alphabet, mixed repetition |

Use these for initial testing and verification before designing your own experimental inputs.

## Generating Experimental Inputs

| Input Type | Suggested Approach |
|------------|-------------------|
| High repetition | Enter directly: `AAAAAABBBBBBCCCCCC` |
| Low repetition | Enter directly: `ABCDABCDABCDABCD` |
| Random characters | Generate at random.org/strings |
| Natural text | Download plain text from gutenberg.org or generate at lipsum.com |
| Large alphabet | Generate at random.org/strings with a large character set |

## Notes

- Results are appended to the CSV file if it already exists, allowing multiple sessions to accumulate into a single dataset.
- Both schemes are run on the same input in a single session, ensuring direct comparability.
- The experiment runner prints a round-trip warning if decoded output does not match the original input.
- Input descriptions are recorded in the CSV; use short descriptive names such as `high-repetition-4char` or `natural-text-100chars` to make your results easy to interpret later.
- Requires Python 3.10 or later for type hint syntax used throughout the codebase.