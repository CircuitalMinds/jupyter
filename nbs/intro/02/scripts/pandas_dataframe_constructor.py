import pandas as pd
import numpy as np

print(np.arange(9).reshape(3, 3))
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

print(pd.DataFrame(np.arange(9).reshape(3, 3)))
#    0  1  2
# 0  0  1  2
# 1  3  4  5
# 2  6  7  8

print(pd.DataFrame(np.arange(9).reshape(3, 3),
                   columns=['col_0', 'col_1', 'col_2'],
                   index=['row_0', 'row_1', 'row_2']))
#        col_0  col_1  col_2
# row_0      0      1      2
# row_1      3      4      5
# row_2      6      7      8

print(pd.DataFrame([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))
#    0  1  2
# 0  0  1  2
# 1  3  4  5
# 2  6  7  8

print(pd.DataFrame([[0, 1, 2], [3, 4, 5], [6, 7, 8, 9, 10]]))
#    0  1  2    3     4
# 0  0  1  2  NaN   NaN
# 1  3  4  5  NaN   NaN
# 2  6  7  8  9.0  10.0

print(pd.DataFrame({'col_0': [0, 1, 2],
                    'col_1': np.arange(3, 6),
                    'col_2': (6, 7, 8)}))
#    col_0  col_1  col_2
# 0      0      3      6
# 1      1      4      7
# 2      2      5      8

print(pd.DataFrame({'col_0': [0, 1, 2],
                    'col_1': np.arange(3, 6),
                    'col_2': (6, 7, 8)},
                   index=['row_0', 'row_1', 'row_2']))
#        col_0  col_1  col_2
# row_0      0      3      6
# row_1      1      4      7
# row_2      2      5      8

# print(pd.DataFrame({'col_0': [0, 1, 2, 100],
#                     'col_1': np.arange(3, 6),
#                     'col_2': (6, 7, 8)}))
# ValueError: arrays must all be same length

print(pd.DataFrame({'col_0': [0, 1, 2],
                    'col_1': np.arange(3, 6),
                    'col_2': (6, 7, 8)},
                   index=['row_0', 'row_1', 'row_2']))
#        col_0  col_1  col_2
# row_0      0      3      6
# row_1      1      4      7
# row_2      2      5      8

print(pd.DataFrame({'row_0': [0, 1, 2],
                    'row_1': np.arange(3, 6),
                    'row_2': (7, 8, 9)}).T)
#        0  1  2
# row_0  0  1  2
# row_1  3  4  5
# row_2  7  8  9

print(pd.DataFrame.from_dict(
    {'row_0': [0, 1, 2],
     'row_1': [3, 4, 5],
     'row_2': [6, 7, 8]},
    orient='index'))
#        0  1  2
# row_0  0  1  2
# row_1  3  4  5
# row_2  6  7  8

print(pd.DataFrame.from_dict(
    {'row_0': np.array([0, 1, 2]),
     'row_1': np.array([3, 4, 5]),
     'row_2': np.array([6, 7, 8])},
    orient='index'))
#        0  1  2
# row_0  0  1  2
# row_1  3  4  5
# row_2  6  7  8

# print(pd.DataFrame.from_dict(
#     {'row_0': [0, 1, 2],
#      'row_1': np.array([3, 4, 5]),
#      'row_2': [6, 7, 8]},
#     orient='index'))
# TypeError: Expected list, got numpy.ndarray

print(pd.DataFrame([{'col_0': 0, 'col_1': 1, 'col_2': 2},
                    {'col_0': 3, 'col_1': 4, 'col_2': 5},
                    {'col_0': 6, 'col_1': 7, 'col_2': 8}]))
#    col_0  col_1  col_2
# 0      0      1      2
# 1      3      4      5
# 2      6      7      8

print(pd.DataFrame([{'col_0': 0, 'col_1': 1, 'col_2': 2},
                    {'col_0': 3, 'col_1': 4, 'col_2': 5},
                    {'col_0': 6, 'col_1': 7, 'col_2': 8}],
                   index=['row_0', 'row_1', 'row_2']))
#        col_0  col_1  col_2
# row_0      0      1      2
# row_1      3      4      5
# row_2      6      7      8

print(pd.DataFrame([{'col_0': 0, 'col_1': 1, 'col_2': 2},
                    {'col_0': 3, 'col_2': 5, 'col_3': 100},
                    {'col_0': 6, 'col_1': 7, 'col_2': 8}]))
#    col_0  col_1  col_2  col_3
# 0      0    1.0      2    NaN
# 1      3    NaN      5  100.0
# 2      6    7.0      8    NaN

print(pd.DataFrame({'col_0': {'row_0': 0, 'row_1': 1, 'row_2': 2},
                    'col_1': {'row_0': 3, 'row_2': 4, 'row_3': 5},
                    'col_2': {'row_0': 6, 'row_1': 7, 'row_2': 8}}))
#        col_0  col_1  col_2
# row_0    0.0    3.0    6.0
# row_1    1.0    NaN    7.0
# row_2    2.0    4.0    8.0
# row_3    NaN    5.0    NaN
