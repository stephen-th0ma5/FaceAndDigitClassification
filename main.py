
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

#creates array of 2D matrices of digits
def createTestDigitMatrix(digitMatrices):
    for i in range(1000):
        imageMatrix = []
        for i in range(28):
            imageMatrix.append(digit_data_test_images.readline())
        digitMatrices.append(imageMatrix)

#creates array of 2D matrices of faces
def createTestFaceMatrix(faceMatrices):
    for i in range(10500):
        imageMatrix = []
        for i in range(70):
            imageMatrix.append(face_data_test_images.readline())
        faceMatrices.append(imageMatrix)

createTestDigitMatrix(digitMatrices)
createTestFaceMatrix(faceMatrices)

for line in faceMatrices[1]:
    print(line)
