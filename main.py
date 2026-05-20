# main.py
#
# Entry point for the compression experiment application.
# Menu-driven interface; follow the prompts to run compression experiments.

import os
from experiment_runner import run, run_from_file
from result_reporter import write_results


def handle_compress_string() -> None:
    print("\n-- Compress a String --")

    input_text = input("Enter input string: ").strip()
    if not input_text:
        print("Input cannot be empty.")
        return

    description = input("Enter a short description for this input (e.g. high-repetition-4char): ").strip()
    if not description:
        description = "manual-input"

    results_file = prompt_path("Results file path (e.g. results/results.csv): ")
    os.makedirs(os.path.dirname(results_file) if os.path.dirname(results_file) else ".", exist_ok=True)

    print()
    results = run(input_text, description)
    write_results(results, results_file)

    print(f"\nResults written to: {results_file}")


def handle_compress_file() -> None:
    print("\n-- Compress a File --")

    input_file = prompt_existing_file("Input file path: ")

    description = input("Enter a short description for this input (e.g. natural-text-gutenberg): ").strip()
    if not description:
        description = "file-input"

    results_file = prompt_path("Results file path (e.g. results/results.csv): ")
    os.makedirs(os.path.dirname(results_file) if os.path.dirname(results_file) else ".", exist_ok=True)

    print()
    results = run_from_file(input_file, description)
    write_results(results, results_file)

    print(f"\nResults written to: {results_file}")


def prompt_path(message: str) -> str:
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Please enter a valid file path.")


def prompt_existing_file(message: str) -> str:
    while True:
        value = input(message).strip()
        if os.path.isfile(value):
            return value
        print(f"File not found: {value}. Please try again.")


def main() -> None:
    print("\nCompression Experiment")
    print("======================")

    running = True
    while running:
        print("\nWhat would you like to do?")
        print("  1. Compress a string")
        print("  2. Compress a file")
        print("  3. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            handle_compress_string()
        elif choice == "2":
            handle_compress_file()
        elif choice == "3":
            running = False
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()