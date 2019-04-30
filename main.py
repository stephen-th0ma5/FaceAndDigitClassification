
#Digit Data
########################################################################
digit_data_test_images = open("./digitdata/testimages", "r")
digit_data_test_labels = open("./digitdata/testlabels", "r")

digit_data_training_images = open("./digitdata/trainingimages", "r")
digit_data_training_labels = open("./digitdata/traininglabels", "r")

digit_data_validation_images = open("./digitdata/validationimages", "r")
digit_data_validation_labels = open("./digitdata/validationlabels", "r")
########################################################################

#Face Data
########################################################################
face_data_test_images = open("./facedata/facedatatest", "r")
face_data_test_labels = open("./facedata/facedatatestlabels", "r")

face_data_training_images = open("./facedata/facedatatrain", "r")
face_data_training_labels = open("./facedata/facedatatrainlabels", "r")

face_data_validation_images = open("./facedata/facedatavalidation", "r")
face_data_validation_labels = open("./facedata/facedatavalidationlabels", "r")
########################################################################

digitMatrices = []
faceMatrices = []

#creates array of 2D matrices of digits (10% of training data)
def createTrainingDigitMatrix(digitMatrices):
    for i in range(14000):
        imageMatrix = []
        for i in range(28):
            imageMatrix.append(digit_data_training_images.readline())
        digitMatrices.append(imageMatrix)

#creates array of 2D matrices of faces (10% of training data)
def createTrainingFaceMatrix(faceMatrices):
    for i in range(3157):
        imageMatrix = []
        for i in range(70):
            imageMatrix.append(face_data_training_images.readline())
        faceMatrices.append(imageMatrix)

createTrainingDigitMatrix(digitMatrices)
createTrainingFaceMatrix(faceMatrices)

for line in digitMatrices[0]:
    print(line)
