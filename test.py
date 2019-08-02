import numpy as np

fileName = 'Data/digitdata/trainingimages.txt'
f = open(fileName)
lines = f.readlines()
f.close()

del lines[28*3]
images = [np.zeros((28, 28)) for i in range( 3 ) ]

j=0
for image in images:
    x = np.nditer(image, op_flags=['writeonly'])
    i = 0
    for line in lines:
        for c in line:
            if c == '\n':
                continue
            elif c == '#':
                x[0] = 1
            elif c == '+':
                x[0] = .5
            x.iternext()
            if(x.finished):break
        if(x.finished):break
print(images)
f.close()

imagez = [np.random.randint(0, 10, (8, 8)) for i in range(0,3)]
features = [np.zeros(( img.size//4, 1) )for img in imagez]
for image, ft in zip(imagez, features):
    x = np.nditer(ft, op_flags=['writeonly'])
    for i in range(0, 8, 2):
        for j in range(0, 8, 2):
            print(image)
            submatrix = image[i:i + 2, j:j + 2]
            print(submatrix)
            print(np.mean(submatrix))
            x[0] = np.mean(submatrix)
            print(x[0])
            x.iternext()
            if (x.finished): break
        if (x.finished): break

print(features)

fileName = 'Data/digitdata/traininglabels.txt'
f = open(fileName)
lines = f.readlines()
f.close()

integers = list(map(int, lines))

labels = [np.zeros((10, 1)) for i in range(len(lines))]

for i,vector in zip(integers, labels):
    print(i)
    vector[i][0] = 1
    print(vector)

print(labels)