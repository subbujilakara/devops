if __name__ == "__main__":
    
    text = "A man a plan a canal Panama"
    
    
    manipulator = TextManipulator(text)
    
    
    print("Original Text:", manipulator)
    
    
    print("Reversed Text:", manipulator.reverse())  # Expected output: "amanaP lanac a nalp a nam A"
    
    
    print("Uppercase Text:", manipulator.to_upper())  # Expected output: "A MAN A PLAN A CANAL PANAMA"
    
    
    print("Vowel Count:", manipulator.count_vowels())  # Expected output: 10 (a, a, a, a, a, a, a, a, a, a)
    
  
    print("Is Palindrome:", manipulator.is_palindrome())  # Expected output: True
