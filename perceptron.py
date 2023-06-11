import pandas as pd
import inspect, random

#region Perceptron
def perceptron_predict(row, weights, learning_rate=0.4):
        oryginal_output = row[0]*weights[0] + row[1]*weights[1]
        if oryginal_output < 0:
            return 0
        else:
            return 1

def teach_perceptron(learning_set, learning_rate=0.4):
    weights = [random.randint(-2, 2), random.randint(-2, 2)]

    for count, row in learning_set.iterrows():
        output = perceptron_predict(row, weights)

        #update weights
        error = row[2] - output
        if output != row[2]:
            weights[0] += learning_rate*row[0]*error
            weights[1] += learning_rate*row[1]*error
    
    return weights

def use_perceptron(weights, test_set):
    output_list = list()

    for count, row in test_set.iterrows():
        output_list.append(perceptron_predict(row, weights))
    return output_list
#endregion

#region utility functions
#dumb functions: they return list of 0 or 1 with the length of given test set
def dummy_model(test_set):
    return [0]*len(test_set)

def dummy_model2(test_set):
    return [1]*len(test_set)

def evaluate_models(model1_output, model2_output, target_list):
    model1_TP = 0
    model1_FP = 0
    model1_TN = 0

    model2_TP = 0
    model2_FP = 0
    model2_TN = 0

    for index, row in enumerate(target_list):
        if row == model1_output[index] and row == 1:
            model1_TP += 1
        elif row != model1_output[index] and model1_output[index] == 1:
            model1_FP += 1
        elif row == model1_output[index] and model1_output[index] == 0:
            model1_TN += 1
        
        if row == model2_output[index] and row == 1:
            model2_TP += 1
        elif row != model2_output[index] and model2_output[index] == 1:
            model2_FP += 1
        elif row == model2_output[index] and model2_output[index] == 0:
            model2_TN += 1

    glass_precision1 = safe_division(model1_TP, model1_TP+model1_FP)
    plate_precision1 = safe_division(model1_TN, model1_TN+model1_FP)

    glass_precision2 = safe_division(model2_TP, model2_TP+model2_FP)
    plate_precision2 = safe_division(model2_TN, model2_TN+model2_FP)

    return f"my perceptron is {(glass_precision1-glass_precision2)*100}% better in getting glasses right and {(plate_precision1-plate_precision2)*100}% in getting plates right than dummy model"

#Math teacher if he sees this: 😠
def safe_division(x, y):
    try:
        return x/y
    except ZeroDivisionError as e:
        print(f"Warning: Division by zero occurred on line {inspect.currentframe().f_back.f_lineno}")
        return 0
#endregion
