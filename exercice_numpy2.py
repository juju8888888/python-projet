# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 22:44:01 2023

@author: legal
"""
import numpy as np

# Exercice 1
vector1 = np.arange(21)
vector1[9:16] *= -1

# Exercice 2
vector2 = np.arange(15, 56)
result2 = vector2[1:-1]

# Exercice 3
array3 = np.arange(12).reshape(3, 4)
for row in array3:
    for num in row:
        print(num)

# Exercice 4
vector4 = np.linspace(5, 50, 10)

# Exercice 5
vector5 = np.random.randint(0, 11, 5)

# Exercice 6
vector6_1 = np.array([1, 2, 3, 4])
vector6_2 = np.array([2, 3, 4, 5])
result6 = vector6_1 * vector6_2

# Exercice 7
matrix7 = np.arange(10, 22).reshape(3, 4)

# Exercice 8
matrix8 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rows, cols = matrix8.shape

# Exercice 9
matrix9 = np.zeros((4, 4))
matrix9[::2, 1::2] = 1
matrix9[1::2, ::2] = 1

# Exercice 10
array10_1 = np.array([0, 10, 20, 40, 60])
array10_2 = np.array([10, 30, 40])
common_values = np.intersect1d(array10_1, array10_2)

# Exercice 11
array11_1 = np.array([10, 10, 20, 20, 30, 30])
array11_2 = np.array([[1, 1], [2, 3]])
unique_values1 = np.unique(array11_1)
unique_values2 = np.unique(array11_2)

# Exercice 12
vector12_1 = np.array([1, 2, 3])
vector12_2 = np.array([4, 5, 6])
cross_product = np.cross(vector12_1, vector12_2)

# Exercice 13
cartesian_coordinates = np.random.rand(10, 2)
x, y = cartesian_coordinates[:, 0], cartesian_coordinates[:, 1]
polar_coordinates = np.sqrt(x**2 + y**2), np.arctan2(y, x)

# Exercice 14
original_array = np.arange(100)
value_to_compare = 34.99062268928913
closest_value = original_array[np.argmin(np.abs(original_array - value_to_compare))]