# This program demonstrates the usage of the TextManipulator class.
# It performs several string manipulations, including:
# 1. Reversing the string
# 2. Converting the string to uppercase
# 3. Counting the number of vowels
# 4. Checking if the string is a palindrome

if __name__ == "__main__":
    # Initialize the text string to be manipulated
    text = "A man a plan a canal Panama"
    
    # Create an instance of the TextManipulator class with the text
    manipulator = TextManipulator(text)
    
    # Display the original text
    print("Original Text:", manipulator)
    
    # Reverse the text and display the result
    # Expected output: "amanaP lanac a nalp a nam A"
    print("Reversed Text:", manipulator.reverse())
    
    # Convert the text to uppercase and display the result
    # Expected output: "A MAN A PLAN A CANAL PANAMA"
    print("Uppercase Text:", manipulator.to_upper())
    
    # Count the vowels in the text and display the result
    # Expected output: 10 (a, a, a, a, a, a, a, a, a, a)
    print("Vowel Count:", manipulator.count_vowels())
  
    # Check if the text is a palindrome and display the result
    # Expected output: True (because the phrase is a palindrome)
    print("Is Palindrome:", manipulator.is_palindrome())
