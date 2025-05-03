def character_frequency(text):
    """
    Count the frequency of each character in the given text.

    Args:
        text (str): The input text.

    Returns:
        dict: A dictionary with characters as keys and their frequencies as values.
    """
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

print(character_frequency("hello world"))
