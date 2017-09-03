
import numpy as np

album_vector = ["Thriller", "Back in Black", "The Dark side of the moon", "the bodyguard"
    , "Bat out of the hell", "thrie greatest hits", "Saturday night fever"
    , "rumours"]

print(album_vector)

ncols = 2
nrows = 2
matrix =  [[0]* ncols for i in range(nrows)]

matrix[0][0] = "Thriller"
matrix[0][1] = "Thriller"
matrix[1][0] = "Thriller"
matrix[1][1] = "Thriller"

print(matrix)


print(matrix.shape)

print(matrix.type)