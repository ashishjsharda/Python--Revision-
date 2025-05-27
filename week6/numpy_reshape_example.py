arr = np.arange(12)
print(arr)  # [0  1  2  3  4  5  6  7  8  9 10 11]

# Reshape to 2D
reshaped = arr.reshape(3, 4)
print(reshaped)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# Reshape to 3D
reshaped_3d = arr.reshape(2, 2, 3)
print(reshaped_3d.shape)  # (2, 2, 3)

# Flatten back to 1D
flattened = reshaped.flatten()
print(flattened)  # [0  1  2  3  4  5  6  7  8  9 10 11]
