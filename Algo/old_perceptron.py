import pandas as pd
import random

#plate: 0 and glass: 1
training = pd.read_csv("D:\\Programming\\Projects\\My_perceptron_implementation\\Algo\\training.csv")
test = pd.read_csv("D:\\Programming\\Projects\\My_perceptron_implementation\\Algo\\test.csv")


def run_perceptron(training_set, learning_rate=0.5):
    w_1 = random.randint(-3, 3)
    w_2 = random.randint(-3, 3)
    b = random.randint(-2, 2)
    #I know it's not efficent cuz it doesn't use vectorization 😜
    #I should have used numpy arrays but it is how it is
    for count, row in training_set.iterrows():
        print(f"w1: {w_1}, w2: {w_2}, b: {b}")

        #predict (I also did it with bias parameter cuz why not. Model will be better)
        oryginal_output = row[0]*w_1 + row[1]*w_2 + b
        if oryginal_output < 0:
            output = 0
        else:
            output = 1
        
        #update weights
        if output != row[2]:
            w_1 = w_1 + learning_rate*(row[2]-oryginal_output)
            w_2 = w_2 + learning_rate*(row[2]-oryginal_output)
            b = b + learning_rate*(row[2]-oryginal_output)

#evaluating my perception on test set
def evaluate_perceptron(test_set):
    pass

#model to to compare if perceptron is really working
def mean_model(test_set):
    #pretict all outputs
    pass

def evaluate_mean_model():
    pass
    #compare my and real outputs and calculate precision so TP / (TP + FP)

#how much is my model better than mean_model
#print(evaluate_perceptron() - mean_model())

run_perceptron(training)