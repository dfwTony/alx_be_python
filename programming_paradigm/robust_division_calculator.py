# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Perform safe division with error handling.
    Returns result or an error message as a string.
    """
    try:
        # Convert inputs to floats (may raise ValueError)
        num = float(numerator)
        den = float(denominator)

        try:
            # Attempt division (may raise ZeroDivisionError)
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
