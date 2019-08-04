from ProcessFaceData import ProcessFaceData
from Labels import Labels
import pickle

face_data = ProcessFaceData('Data/facedata/facedatatrain.txt', 70).main()
face_labels = Labels('Data/facedata/facedatatrainlabels.txt').get_labels()


with open('processed_face_data.pkl', 'wb') as f:
    pickle.dump(face_data, f)

with open('Processed_face_labels.pkl', 'wb') as q:
    pickle.dump(face_labels, q)
#
#
# digit_data = ProcessFaceData('Data/digitdata/trainingimages.txt', 28).main()
# digit_labels = Labels('Data/digitdata/traininglabels.txt').get_labels()
#
#
# with open('processed_digit_data.pkl', 'wb') as r:
#     pickle.dump(digit_data, r)
#
# with open('Processed_digit_labels.pkl', 'wb') as o:
#     pickle.dump(digit_labels, o)