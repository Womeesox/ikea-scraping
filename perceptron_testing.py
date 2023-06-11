import pandas as pd
import perceptron as perc
import random

#0 is plate and 1 is glass
test_df = pd.read_csv("D:\\Programming\\Projects\\My_perceptron_implementation\\test.csv")
learning_df = pd.read_csv("D:\\Programming\\Projects\\My_perceptron_implementation\\training.csv")

#shuffle datasets
learning_df = learning_df.sample(frac=1).reset_index(drop=True)
test_df = test_df.sample(frac=1).reset_index(drop=True)

weights = perc.teach_perceptron(learning_df, learning_rate=0.4)
output = perc.use_perceptron(weights, test_df)

evaluation = perc.evaluate_models(output, perc.dummy_model2(test_df), test_df["target"])

print(evaluation)