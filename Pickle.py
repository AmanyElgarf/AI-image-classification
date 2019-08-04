from ProcessFaceData import ProcessFaceData
from Labels import Labels
import pickle

face_data = ProcessFaceData('Data/facedata/facedatatrain.txt').main()
labels = Labels('Data/facedata/facedatatrainlabels.txt').get_labels()

with open('parrot.pkl', 'wb') as f:
    pickle.dump(face_data, f)
    pickle.dump(labels, f)