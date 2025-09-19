def number_to_word(number):
    """
    Convert a number to its English word representation.
    Supports numbers from 0 to 999,999,999,999 (trillions)
    """
    if number < 0:
        return "minus " + number_to_word(abs(number))
    
    if number == 0:
        return "zero"
    
    under_20 = {
        0: "", 1: "one", 2: "two", 3: "three", 4: "four", 
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 
        14: "fourteen", 15: "fifteen", 16: "sixteen", 
        17: "seventeen", 18: "eighteen", 19: "nineteen"
    }

    tens = {
        2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 
        6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"
    }

    magnitudes = {
        100: "hundred",
        1000: "thousand",
        1000000: "million",
        1000000000: "billion",
        1000000000000: "trillion"
    }
    
    if number < 20:
        return under_20[number]
    
    if number < 100:
        tens_digit = number // 10
        ones_digit = number % 10
        if ones_digit == 0:
            return tens[tens_digit]
        return tens[tens_digit] + "-" + under_20[ones_digit]
    
    magnitude = 100
    for mag in sorted(magnitudes.keys(), reverse=True):
        if number >= mag:
            magnitude = mag
            break
    
    main_part = number // magnitude
    remainder = number % magnitude
    
    main_words = number_to_word(main_part) + " " + magnitudes[magnitude]
    
    if remainder == 0:
        return main_words
    elif remainder < 100:
        return main_words + " and " + number_to_word(remainder)
    else:
        return main_words + ", " + number_to_word(remainder)


def main():
    while True:
        try:
            user_input = input("\nEnter a number (or 'quit' to exit): ")
            if user_input.lower() == 'quit':
                break
            number = int(user_input)
            print(f"{number:,} = {number_to_word(number)}")
        except ValueError:
            print("Please enter a valid integer.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()