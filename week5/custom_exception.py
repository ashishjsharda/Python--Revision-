class NegativeException(Exception):
    """Custom exception for negative values."""
    pass

def check_positive(value):
    """Check if the value is positive."""
    if value < 0:
        raise NegativeException("Negative value encountered.")
    return True

try:
    # Example usage
    check_positive(-5)
    print("Value is positive.")
except NegativeException as e:
    print(e)
