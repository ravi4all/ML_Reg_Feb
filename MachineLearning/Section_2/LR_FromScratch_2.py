import csv
import math
import random

def load_csv(filename):
    dataset = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            dataset.append(row)
    
    return dataset

def str_to_float():
    pass

def minmax_dataset():
    pass

def normalize_dataset():
    pass

def cross_validation():
    pass

def accuracy_metrics():
    pass

def predict():
    pass

def evaluate_algorithm():
    pass

def sgd_logistic():
    pass

def logistic_regression():
    pass

filename = 'pima-indians-diabetes.data.csv'
dataset = load_csv(filename)


