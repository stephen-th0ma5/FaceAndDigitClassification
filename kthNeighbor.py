import math
from settings import *
from features import *
from collections import Counter

def k_nearest_digits(digitMatrix, index, featureVectors):
    featureVector = calc_feature_vector(digitMatrix, index, digit_function_arr)

    diffArr = []

    for vector in featureVectors:
        sum = 0
        i = 0
        for value in featureVector:
            sum += abs(vector[i] - value)
            i += 1
        diffArr.append(sum)


    indexArr = []
    k = int(math.sqrt(len(digitLabels)))
    for _ in range(k):
        diff = min(diffArr)
        index = diffArr.index(diff)
        indexArr.append(index)
        diffArr[index] = 10000000


    valueArr = []
    for index in indexArr:
        valueArr.append(digitLabels[index])

    counter = Counter(valueArr)
    value = counter.most_common(1)[0][0]

    return value

def k_nearest_faces(faceMatrix, index, featureVectors):
    featureVector = calc_feature_vector(faceMatrix, index, face_function_arr)

    diffArr = []

    for vector in featureVectors:
        sum = 0
        i = 0
        for value in featureVector:
            sum += abs(vector[i] - value)
            i += 1
        diffArr.append(sum)


    indexArr = []
    k = int(math.sqrt(len(faceLabels)) / 2)
    for _ in range(k):
        diff = min(diffArr)
        index = diffArr.index(diff)
        indexArr.append(index)
        diffArr[index] = 10000000


    valueArr = []
    for index in indexArr:
        valueArr.append(faceLabels[index])

    counter = Counter(valueArr)
    value = counter.most_common(1)[0][0]

    return value

def run_kth_n_faces():
    correct = 0
    incorrect = 0
    print("Learning...")
    featureVectors = create_fv_for_training(faceMatrices, face_function_arr)
    print("Validating...")
    for i in range(int(301 * VALPERCENT)):
        return_value = k_nearest_faces(faceValidationMatrices, i, featureVectors)
        if(return_value == faceValidationLabels[i]):
            correct += 1
        else:
            incorrect += 1
    print("SUCCESS RATE " + str((correct / (correct + incorrect)) * 100) + "%")

def run_kth_n_digits():
    correct = 0
    incorrect = 0
    print("Learning...")
    featureVectors = create_fv_for_training(digitMatrices, digit_function_arr)
    print("Validating...")
    for i in range(int(1000 * VALPERCENT)):
        return_value = k_nearest_digits(digitValidationMatrices, i, featureVectors)
        if(return_value == digitValidationLabels[i]):
            correct += 1
        else:
            incorrect += 1
    print("SUCCESS RATE " + str((correct / (correct + incorrect)) * 100) + "%")
