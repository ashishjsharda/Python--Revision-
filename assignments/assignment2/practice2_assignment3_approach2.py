from collections import Counter

def character_frequency(text):
    """
    Count the frequency of each character in the given text.
    
    Args:
        text (str): The input text.
    
    Returns:
        dict: A dictionary with characters as keys and their frequencies as values.
    """
    return Counter(text)

print(character_frequency("hello world"))

