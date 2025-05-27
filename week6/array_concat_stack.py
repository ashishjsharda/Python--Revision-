a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Concatenate
concat = np.concatenate([a, b])
print(concat)  # [1 2 3 4 5 6]

# Stack
vertical = np.vstack([a, b])    # Stack vertically
horizontal = np.hstack([a, b])  # Stack horizontally

print(vertical)
# [[1 2 3]
#  [4 5 6]]

print(horizontal)  # [1 2 3 4 5 6]
