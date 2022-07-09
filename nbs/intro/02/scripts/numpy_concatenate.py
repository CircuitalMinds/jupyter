import numpy as np

a1 = np.ones((2, 3), int)
print(a1)
# [[1 1 1]
#  [1 1 1]]

a2 = np.full((2, 3), 2)
print(a2)
# [[2 2 2]
#  [2 2 2]]

print(np.concatenate([a1, a2]))
# [[1 1 1]
#  [1 1 1]
#  [2 2 2]
#  [2 2 2]]

a3 = np.full((2, 3), 3)
print(a3)
# [[3 3 3]
#  [3 3 3]]

print(np.concatenate([a1, a2, a3]))
# [[1 1 1]
#  [1 1 1]
#  [2 2 2]
#  [2 2 2]
#  [3 3 3]
#  [3 3 3]]

print(np.concatenate([a1, a2], 0))
# [[1 1 1]
#  [1 1 1]
#  [2 2 2]
#  [2 2 2]]

print(np.concatenate([a1, a2], 1))
# [[1 1 1 2 2 2]
#  [1 1 1 2 2 2]]

# print(np.concatenate([a1, a2], 2))
# AxisError: axis 2 is out of bounds for array of dimension 2

a2_ = np.full((3, 3), 2)
print(a2_)
# [[2 2 2]
#  [2 2 2]
#  [2 2 2]]

print(np.concatenate([a1, a2_], 0))
# [[1 1 1]
#  [1 1 1]
#  [2 2 2]
#  [2 2 2]
#  [2 2 2]]

# print(np.concatenate([a1, a2_], 1))
# ValueError: all the input array dimensions except for the concatenation axis must match exactly

a1 = np.ones(3, int)
print(a1)
# [1 1 1]

a2 = np.full(3, 2)
print(a2)
# [2 2 2]

print(np.concatenate([a1, a2], 0))
# [1 1 1 2 2 2]

# print(np.concatenate([a1, a2], 1))
# AxisError: axis 1 is out of bounds for array of dimension 1

a1 = np.ones((2, 3), int)
print(a1)
# [[1 1 1]
#  [1 1 1]]

a2 = np.full(3, 2)
print(a2)
# [2 2 2]

# print(np.concatenate([a1, a2], 0))
# ValueError: all the input arrays must have same number of dimensions
