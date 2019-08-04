import numpy as np

fileName = 'Data/facedata/facedatatrainlabels.txt'
f = open(fileName)
lines = f.readlines()
f.close()

# convert list of each line into integer list
integers = list(map(int, lines))

# initialize 10x1 numpy vector to represent labels
labels = [np.zeros((1, 1)) for i in range(len(lines))]

# make element at index of label to 1
for i, vector in zip(integers, labels):
    vector[0][0] = i

print(labels)




# fileName = 'Data/digitdata/trainingimages.txt'
# f = open(fileName)
# lines = f.readlines()
# f.close()
#
# del lines[28*20]
# images = []
#
# i=0
# k=0
# image = np.zeros((28,28))
# while k < len(lines):
#     if (i==28):
#         i=0
#         images.append(image)
#         image = np.zeros((28,28))
#     line = lines[k]
#     for c,j in zip(line,range(0,28)):
#         if c == '\n':
#             continue
#         elif c == '#':
#             image[i][j] = 1
#         elif c == '+':
#             image[i][j] = .5
#     k+=1
#     i+=1
#
#
# print(images)

# features = [np.zeros(( img.size//4, 1) )for img in images]
# for image, ft in zip(images, features):
#     x = np.nditer(ft, op_flags=['writeonly'])
#     for i in range(0, 28, 2):
#         for j in range(0, 28, 2):
#             submatrix = image[i:i + 2, j:j + 2]
#             x[0] = np.mean(submatrix)
#             x.iternext()
#             if (x.finished): break
#         if (x.finished): break
#
#
# fileName = 'Data/digitdata/traininglabels.txt'
# f = open(fileName)
# lines = f.readlines()
# f.close()
#
# integers = list(map(int, lines))
# print(len(lines))
#
# labels = [np.zeros((10, 1)) for i in range(len(lines))]
#
# for i,vector in zip(integers, labels):
#     vector[i][0] = 1
#
#
# print(features)
# print(images)
#
# # print(labels)

