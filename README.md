# Number to Words Converter

A Python program that converts numerical values into their English word representations. This tool supports both positive and negative integers from zero up to trillions (999,999,999,999).

## Features

- Converts numbers to their English word equivalents
- Supports numbers from -999,999,999,999 to 999,999,999,999
- Handles negative numbers with "minus" prefix
- Properly formats numbers with commas and hyphens
- Interactive command-line interface
- Error handling for invalid inputs

## Usage

### Running the Program

1. Ensure you have Python 3.x installed on your system
2. Run the script using:
   ```bash
   python main.py
   ```

### Interactive Mode

The program runs in an interactive loop where you can:
- Enter any integer to convert it to words
- Type 'quit' to exit the program
- The program handles invalid inputs gracefully

### Examples

- `123` → "one hundred and twenty-three"
- `-4567` → "minus four thousand, five hundred and sixty-seven"
- `1000000` → "one million"
- `0` → "zero"

## Number Formatting

The program follows standard English number formatting:
- Uses "and" after hundreds before smaller numbers
- Uses commas between large number groups (thousands, millions, etc.)
- Uses hyphens between tens and units (twenty-one, forty-five)
- Properly handles special cases for numbers under twenty

## Supported Range

The converter supports numbers in these ranges:
- Units: 0-9
- Teens: 10-19
- Tens: 20-99
- Hundreds: 100-999
- Thousands: 1,000-999,999
- Millions: 1,000,000-999,999,999
- Billions: 1,000,000,000-999,999,999,999
- Trillions: 1,000,000,000,000-999,999,999,999,999

## Error Handling

The program includes comprehensive error handling:
- Validates that input is a valid integer
- Handles unexpected errors gracefully
- Provides clear error messages to users

## Requirements

- Python 3.x (no external dependencies required)
