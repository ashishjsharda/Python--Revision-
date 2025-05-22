class NegativeException(Exception):
    """Custom exception for negative values with enhanced behavior."""
    
    def __init__(self, value, message="Negative value encountered."):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} (Received: {self.value})"

    def log_error(self):
        # Simulate logging for learning purposes
        print(f"[LOG] Error logged for value: {self.value}")

    def suggest_fix(self):
        return f"Suggestion: Use a non-negative value (e.g., abs({self.value}) = {abs(self.value)})."

def check_positive(value):
    """Check if the value is positive."""
    if value < 0:
        raise NegativeException(value)
    return True

# Example usage
try:
    check_positive(-10)
except NegativeException as e:
    print(e)              # Custom __str__ output
    e.log_error()         # Simulate logging
    print(e.suggest_fix()) # Custom fix suggestion
