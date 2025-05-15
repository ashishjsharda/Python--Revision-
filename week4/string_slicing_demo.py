text = "Python Programming"

# Basic slicing
slice1 = text[0:6]    # "Python" (characters from index 0 to 5)
slice2 = text[7:18]   # "Programming" (characters from index 7 to 17)

# Omitting start or end
slice3 = text[:6]     # "Python" (from beginning to index 5)
slice4 = text[7:]     # "Programming" (from index 7 to end)

# Negative indices in slicing
slice5 = text[-11:]   # "Programming" (last 11 characters)
slice6 = text[:-12]   # "Python" (from beginning to 12th last character)

# Stride/step in slicing
every_other = text[::2]    # "Pto rgamn" (every 2nd character)
reverse = text[::-1]       # "gnimmargorP nohtyP" (reversed string)
reverse_words = text[::-1].split()[::-1]  # ['nohtyP', 'gnimmargorP']
