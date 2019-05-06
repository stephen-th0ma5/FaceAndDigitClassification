from settings import *
from features import *
from naiveBayes import *
from kthNeighbor import *


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



def createTestingDigitLabels():
    for line in digit_data_test_labels:
        digitTestingLabels.append(line[0])

def createValidationDigitLabels():
    for line in digit_data_validation_labels:
        digitValidationLabels.append(line[0])

#creates array of digit labels from training data
def createTrainingDigitLabels():
    for line in digit_data_training_labels:
        digitLabels.append(line[0])

#creates array of face labels from training data
def createTrainingFaceLabels():
    for line in face_data_training_labels:
        faceLabels.append(line[0])

#creates array of face labels from validation data
def createValidationFaceLabels():
    for line in face_data_validation_labels:
        faceValidationLabels.append(line[0])

def createTestingDigitMatrix(digitMatrices):
    for i in range(1000):
        imageMatrix = []
        for i in range(28):
            imageMatrix.append(digit_data_test_images.readline())
        digitMatrices.append(imageMatrix)

#creates array of 2D matrices of training digits
def createTrainingDigitMatrix(digitMatrices):
    for i in range(int(5000 * PERCENT)):
        imageMatrix = []
        for i in range(28):
            imageMatrix.append(digit_data_training_images.readline())
        digitMatrices.append(imageMatrix)

#creates array of 2D matrices of training faces
def createTrainingFaceMatrix(faceMatrices):
    for i in range(int(451 * PERCENT)):
        imageMatrix = []
        for i in range(70):
            imageMatrix.append(face_data_training_images.readline())
        faceMatrices.append(imageMatrix)

#creates array of 2D matrices of vlidation faces
def createValidationFaceMatrix(faceMatrices):
    for i in range(int(301 * VALPERCENT)):
        imageMatrix = []
        for i in range(70):
            imageMatrix.append(face_data_validation_images.readline())
        faceMatrices.append(imageMatrix)

def createValidationDigitMatrix(digitMatrices):
    for i in range(int(1000 * VALPERCENT)):
        imageMatrix = []
        for i in range(28):
            imageMatrix.append(digit_data_validation_images.readline())
        digitMatrices.append(imageMatrix)


def init():
    createTestingDigitMatrix(digitTestingMatrices)
    createTestingDigitLabels()

    createTrainingDigitMatrix(digitMatrices)
    createTrainingDigitLabels()

    createValidationDigitMatrix(digitValidationMatrices)
    createValidationDigitLabels()

    createTrainingFaceMatrix(faceMatrices)
    createTrainingFaceLabels()

    createValidationFaceMatrix(faceValidationMatrices)
    createValidationFaceLabels()


if __name__ == "__main__":
    init()
    print("FACIAL RECOGNITION")
    print("####################################")
    print("[NAIVE BAYES ALGORITHM]")
    run_naive_bayes_faces()
    print("[PERCEPTRON ALGORITHM]")
    print("[KTH NEIGHBOR ALGORITHM]")
    run_kth_n_faces()
    print("####################################")
    print("\nDIGIT RECOGNITION")
    print("####################################")
    print("[NAIVE BAYES ALGORITHM]")
    run_naive_bayes_digits()
    print("[PERCEPTRON ALGORITHM]")
    print("[KTH NEIGHBOR ALGORITHM]")
    run_kth_n_digits()
    print("####################################")






























"""
#DIGIT TEST DATA#
###############################
correct = 0
incorrect = 0
#print("Learning...")
featureVectors = create_fv_for_training(digitMatrices, digit_function_arr)
for i in range(1000):
    return_value = naive_bayes_digit(digitTestingMatrices, i, featureVectors, digit_function_arr)
    if(return_value == int(digitTestingLabels[i])):
        correct += 1
        #print("CORRECT")
    else:
        incorrect += 1
        #print("INCORRECT its " + str(digitTestingLabels[i]))

#print("SUCCESS RATE " + str(correct / (correct + incorrect)) + "%")
###############################
"""
