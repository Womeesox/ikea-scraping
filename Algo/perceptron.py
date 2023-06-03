import pandas as pd

test = pd.read_csv("D:\\Programming\\Projects\\My_perceptron_implementation\\Algo\\test.csv")

#learn_perceptron function: learns from given learning set and returns weights

#use_percepytron functiion: uses learned weights on given test set and returns outputs

#dumb function: returns list of 0 with the length of given test set
def dummy_model(test_set):
    return [0]*len(test_set)

def dummy_model2(test_set):
    return [1]*len(test_set)

#precision function: takes as parameters 2 lists of answers from other models and list of actual answers
#then using formula TP / (TP + FP) returns precision
def evaluate_models(model1_output, model2_output, target_list):
    model1_TP = 0
    model1_FP = 0
    model1_FN = 0

    model2_TP = 0
    model2_FP = 0
    model2_FN = 0

    for index, row in enumerate(target_list):
        if row == model1_output[index] and row == 0:
            model1_TP += 1
        elif row != model1_output[index] and model1_output[index] == 1:
            model1_FP += 1
        elif row != model1_output[index] and model1_output[index] == 0:
            model1_FN += 1
        
        if row == model2_output[index] and row == 0:
            model2_TP += 1
        elif row != model2_output[index] and model2_output[index] == 1:
            model2_FP += 1
        elif row != model2_output[index] and model2_output[index] == 0:
            model2_FN += 1

    #TODO: DIVISION BY ZERO ERROR
    precision1 = model1_TP / (model1_TP + model1_FP)
    precision2 = model2_TP / (model2_TP + model2_FP)

    recall1 = model1_TP / (model1_TP + model1_FN)
    recall2 = model2_TP / (model2_TP + model2_FN)

    #return compared evaluations: model1 - model2 for both precision and recall
    return f"{model2_TP}"

print(evaluate_models(dummy_model(test), dummy_model2(test), test["target"]))

#recall function: same as precision function but using this formula: TP / (TP + FN)