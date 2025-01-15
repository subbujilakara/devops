class DecimalDigitTransformer:
    def __init__(self, digit):
        
        if not isinstance(digit, int) or digit < 0 or digit > 9:
            raise ValueError("Input must be a single digit between 0 and 9.")
        self.digit = digit

    def calculate_transformation(self):
        
        X = str(self.digit)
        XX = X * 2
        XXX = X * 3
        XXXX = X * 4
        
        
        result = int(X) + int(XX) + int(XXX) + int(XXXX)
        return result


try:
    
    digit = int(input("Enter a single digit (0-9): "))
    
    transformer = DecimalDigitTransformer(digit)
    result = transformer.calculate_transformation()
    print(f"Result: {result}")
except ValueError as e:
    print(f"Error: {e}")



