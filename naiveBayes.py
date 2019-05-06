import math
from settings import *
from features import *

faceIndexes = []
notFaceIndexes = []


digitZeroIndexes = []
digitOneIndexes = []
digitTwoIndexes = []
digitThreeIndexes = []
digitFourIndexes = []
digitFiveIndexes = []
digitSixIndexes = []
digitSevenIndexes = []
digitEightIndexes = []
digitNineIndexes = []


#creates array of face indexes and not face indexes
def face_marginal_prob(matrixLabels):
    for i in range(int(451 * PERCENT)):
        label = matrixLabels[i]
        if(label == "1"):
            faceIndexes.append(i)
        else:
            notFaceIndexes.append(i)

def digit_marginal_prob(digitLabels):
    for i in range(int(5000 * PERCENT)):
        label = digitLabels[i]
        if(label == "0"):
            digitZeroIndexes.append(i)
        if(label == "1"):
            digitOneIndexes.append(i)
        elif(label == "2"):
            digitTwoIndexes.append(i)
        elif(label == "3"):
            digitThreeIndexes.append(i)
        elif(label == "4"):
            digitFourIndexes.append(i)
        elif(label == "5"):
            digitFiveIndexes.append(i)
        elif(label == "6"):
            digitSixIndexes.append(i)
        elif(label == "7"):
            digitSevenIndexes.append(i)
        elif(label == "8"):
            digitEightIndexes.append(i)
        elif(label == "9"):
            digitNineIndexes.append(i)

#calculates prior probability of image being a face
def face_prior_prob():
    return round(len(faceIndexes) / int(len(faceLabels) * PERCENT), 2)

#calculates prior probability of image not being a face
def not_face_prior_prob():
    return round((int(len(faceLabels) * PERCENT) - len(faceIndexes)) / int(len(faceLabels) * PERCENT), 2)

def digit_zero_prior_prob():
    return round(len(digitZeroIndexes) / int(len(digitLabels) * PERCENT), 2)

def digit_one_prior_prob():
    return round(len(digitOneIndexes) / int(len(digitLabels) * PERCENT), 2)

def digit_two_prior_prob():
    return round(len(digitTwoIndexes) / int(len(digitLabels) * PERCENT), 2)

def digit_three_prior_prob():
    return round(len(digitThreeIndexes) / int(len(digitLabels) * PERCENT), 2)

def digit_four_prior_prob():
    return round(len(digitFourIndexes) / int(len(digitLabels) * PERCENT), 2)

def digit_five_prior_prob():
    return round(len(digitFiveIndexes) / int(len(digitLabels) * PERCENT), 2)

def digit_six_prior_prob():
    return round(len(digitSixIndexes) / int(len(digitLabels) * PERCENT), 2)

def digit_seven_prior_prob():
    return round(len(digitSevenIndexes) / int(len(digitLabels) * PERCENT), 2)

def digit_eight_prior_prob():
    return round(len(digitEightIndexes) / int(len(digitLabels) * PERCENT), 2)

def digit_nine_prior_prob():
    return round(len(digitNineIndexes) / int(len(digitLabels) * PERCENT), 2)


def calc_cond_prob_digit_zero(featureVectors, featureVector):
    prob = 1
    i = 0
    k = 1
    for value in featureVector:
        counter = k
        for index in digitZeroIndexes:
            vector = featureVectors[index]
            if(vector[i] == value):
                counter += 1
        prob *= counter / (len(digitZeroIndexes) + k)
        i += 1
    return math.log(prob)

def calc_cond_prob_digit_one(featureVectors, featureVector):
    prob = 1
    i = 0
    k = 1
    for value in featureVector:
        counter = k
        for index in digitOneIndexes:
            vector = featureVectors[index]
            if(vector[i] == value):
                counter += 1
        prob *= counter / (len(digitOneIndexes) + k)
        i += 1
    return math.log(prob)

def calc_cond_prob_digit_two(featureVectors, featureVector):
    prob = 1
    i = 0
    k = 1
    for value in featureVector:
        counter = k
        for index in digitTwoIndexes:
            vector = featureVectors[index]
            if(vector[i] == value):
                counter += 1
        prob *= counter / (len(digitTwoIndexes) + k)
        i += 1
    return math.log(prob)

def calc_cond_prob_digit_three(featureVectors, featureVector):
    prob = 1
    i = 0
    k = 1
    for value in featureVector:
        counter = k
        for index in digitThreeIndexes:
            vector = featureVectors[index]
            if(vector[i] == value):
                counter += 1
        prob *= counter / (len(digitThreeIndexes) + k)
        i += 1
    return math.log(prob)

def calc_cond_prob_digit_four(featureVectors, featureVector):
    prob = 1
    i = 0
    k = 1
    for value in featureVector:
        counter = k
        for index in digitFourIndexes:
            vector = featureVectors[index]
            if(vector[i] == value):
                counter += 1
        prob *= counter / (len(digitFourIndexes) + k)
        i += 1
    return math.log(prob)

def calc_cond_prob_digit_five(featureVectors, featureVector):
    prob = 1
    i = 0
    k = 1
    for value in featureVector:
        counter = k
        for index in digitFiveIndexes:
            vector = featureVectors[index]
            if(vector[i] == value):
                counter += 1
        prob *= counter / (len(digitFiveIndexes) + k)
        i += 1
    return math.log(prob)

def calc_cond_prob_digit_six(featureVectors, featureVector):
    prob = 1
    i = 0
    k = 1
    for value in featureVector:
        counter = k
        for index in digitSixIndexes:
            vector = featureVectors[index]
            if(vector[i] == value):
                counter += 1
        prob *= counter / (len(digitSixIndexes) + k)
        i += 1
    return math.log(prob)

def calc_cond_prob_digit_seven(featureVectors, featureVector):
    prob = 1
    i = 0
    k = 1
    for value in featureVector:
        counter = k
        for index in digitSevenIndexes:
            vector = featureVectors[index]
            if(vector[i] == value):
                counter += 1
        prob *= counter / (len(digitSevenIndexes) + k)
        i += 1
    return math.log(prob)

def calc_cond_prob_digit_eight(featureVectors, featureVector):
    prob = 1
    i = 0
    k = 1
    for value in featureVector:
        counter = k
        for index in digitEightIndexes:
            vector = featureVectors[index]
            if(vector[i] == value):
                counter += 1
        prob *= counter / (len(digitEightIndexes) + k)
        i += 1
    return math.log(prob)

def calc_cond_prob_digit_nine(featureVectors, featureVector):
    prob = 1
    i = 0
    k = 1
    for value in featureVector:
        counter = k
        for index in digitNineIndexes:
            vector = featureVectors[index]
            if(vector[i] == value):
                counter += 1
        prob *= counter / (len(digitNineIndexes) + k)
        i += 1
    return math.log(prob)

#calculates conditional probability of a face
def calc_cond_prob_face(featureVectors, featureVector):
    prob = 1
    i = 0
    for value in featureVector:
        counter = 1
        for index in faceIndexes:
            vector = featureVectors[index]
            if(vector[i] == value):
                counter += 1
        prob *= counter / (len(faceIndexes) + 1)
        i += 1
    return math.log(prob)

#calculates conditional probability of not a face
def calc_cond_prob_not_face(featureVectors, featureVector):
    prob = 1
    i = 0
    for value in featureVector:
        counter = 1
        for index in notFaceIndexes:
            vector = featureVectors[index]
            if(vector[i] == value):
                counter += 1
        prob *= counter / (len(notFaceIndexes) + 1)
        i += 1
    return math.log(prob)

def naive_bayes_digit(digitMatrix, index, featureVectors, function_arr):
    featureVector = calc_feature_vector(digitMatrix, index, function_arr)

    digitZeroPriorProb = digit_zero_prior_prob()
    digitOnePriorProb = digit_one_prior_prob()
    digitTwoPriorProb = digit_two_prior_prob()
    digitThreePriorProb = digit_three_prior_prob()
    digitFourPriorProb = digit_four_prior_prob()
    digitFivePriorProb = digit_five_prior_prob()
    digitSixPriorProb = digit_six_prior_prob()
    digitSevenPriorProb = digit_seven_prior_prob()
    digitEightPriorProb = digit_eight_prior_prob()
    digitNinePriorProb = digit_nine_prior_prob()

    digitZeroCondProb = calc_cond_prob_digit_zero(featureVectors, featureVector)
    digitOneCondProb = calc_cond_prob_digit_one(featureVectors, featureVector)
    digitTwoCondProb = calc_cond_prob_digit_two(featureVectors, featureVector)
    digitThreeCondProb = calc_cond_prob_digit_three(featureVectors, featureVector)
    digitFourCondProb = calc_cond_prob_digit_four(featureVectors, featureVector)
    digitFiveCondProb = calc_cond_prob_digit_five(featureVectors, featureVector)
    digitSixCondProb = calc_cond_prob_digit_six(featureVectors, featureVector)
    digitSevenCondProb = calc_cond_prob_digit_seven(featureVectors, featureVector)
    digitEightCondProb = calc_cond_prob_digit_eight(featureVectors, featureVector)
    digitNineCondProb = calc_cond_prob_digit_nine(featureVectors, featureVector)

    zeroProb = digitZeroPriorProb * digitZeroCondProb
    oneProb = digitOnePriorProb * digitOneCondProb
    twoProb = digitTwoPriorProb * digitTwoCondProb
    threeProb = digitThreePriorProb * digitThreeCondProb
    fourProb = digitFourPriorProb * digitFourCondProb
    fiveProb = digitFivePriorProb * digitFiveCondProb
    sixProb = digitSixPriorProb * digitSixCondProb
    sevenProb = digitSevenPriorProb * digitSevenCondProb
    eightProb = digitEightPriorProb * digitEightCondProb
    nineProb = digitNinePriorProb * digitNineCondProb


    arr = [zeroProb, oneProb, twoProb, threeProb, fourProb, fiveProb, sixProb, sevenProb, eightProb, nineProb]

    index = arr.index(max(arr))
    if(index == 0):
        return 0
    elif(index == 1):
        return 1
    elif(index == 2):
        return 2
    elif(index == 3):
        return 3
    elif(index == 4):
        return 4
    elif(index == 5):
        return 5
    elif(index == 6):
        return 6
    elif(index == 7):
        return 7
    elif(index == 8):
        return 8
    elif(index == 9):
        return 9


def naive_bayes_face(faceMatrix, index, featureVectors, function_arr):
    featureVector = calc_feature_vector(faceMatrix, index, function_arr)
    facePriorProb = face_prior_prob()
    notFacePriorProb = not_face_prior_prob()

    faceCondProb = calc_cond_prob_face(featureVectors, featureVector)
    notFaceCondProb = calc_cond_prob_not_face(featureVectors, featureVector)

    if((faceCondProb * facePriorProb) > (notFaceCondProb * notFacePriorProb)):
        if(faceValidationLabels[index] == "1"):
            return 0
        else:
            return 1
    else:
        if(faceValidationLabels[index] == "0"):
            return 0
        else:
            return 1


def run_naive_bayes_faces():
    face_marginal_prob(faceLabels)
    correct = 0
    incorrect = 0
    print("Learning...")
    featureVectors = create_fv_for_training(faceMatrices, face_function_arr)
    print("Validating...")
    for i in range(int(301 * VALPERCENT)):
        return_value = naive_bayes_face(faceValidationMatrices, i, featureVectors, face_function_arr)
        if(return_value == 0):
            correct += 1
        else:
            incorrect += 1

    print("SUCCESS RATE " + str((correct / (correct + incorrect)) * 100) + "%")


def run_naive_bayes_digits():
    digit_marginal_prob(digitLabels)
    correct = 0
    incorrect = 0
    print("Learning...")
    featureVectors = create_fv_for_training(digitMatrices, digit_function_arr)
    print("Validating...")
    for i in range(int(1000 * VALPERCENT)):
        return_value = naive_bayes_digit(digitValidationMatrices, i, featureVectors, digit_function_arr)
        if(return_value == int(digitValidationLabels[i])):
            correct += 1
        else:
            incorrect += 1

    print("SUCCESS RATE " + str((correct / (correct + incorrect)) * 100) + "%")
