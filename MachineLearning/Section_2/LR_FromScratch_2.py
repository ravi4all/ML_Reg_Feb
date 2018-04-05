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

def str_to_float(dataset):
    for row in dataset:
        for col in range(len(row)):
            row[col] = float(row[col])

def minmax_dataset(dataset):
    minmax = []
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        min_value = min(col_values)
        max_value = max(col_values)    
        minmax.append([min_value, max_value])
    return minmax
    

def normalize_dataset(minmax, dataset):
    numer = 0
    denom = 0
    for row in dataset:
        for i in range(len(row)):
            numer = row[i] - minmax[i][0]
            denom = minmax[i][1] - minmax[i][0]
            row[i] = numer/denom

# K-Fold Cross Validation
def cross_validation(dataset, n_folds):
    dataset_split = []
    dataset_copy = list(dataset)
    fold_size = int(len(dataset) / n_folds)
    
    for i in range(n_folds):
        fold = []
        while len(fold) < fold_size:
            index = random.randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        dataset_split.append(fold)
    
    return dataset_split

def accuracy_metrics(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / len(actual) * 100

def predict(row, coef):
    yhat = coef[0]
    for i in range(len(row) - 1):
        yhat += coef[i + 1] * row[i]
    return 1.0 / (1.0 + math.exp(-yhat))

def evaluate_algorithm(dataset, algorithm, n_folds, learning_rate,nb_epoch):
    scores = []
    folds = cross_validation(dataset, n_folds)
    for fold in folds:
        train = list(folds)
        train.remove(fold)
        train = sum(train,[])
        test = []
        for row in fold:
            row_copy = list(row)
            row_copy[-1] = None
            test.append(row_copy)
            
        predicted = algorithm(train,test,learning_rate,nb_epoch)
        actual = [row[-1] for row in fold]
        score = accuracy_metrics(actual, predicted)
        scores.append(score)
    return scores
        

def sgd_logistic(dataset, np_epoch, learning_rate):
    coef = [0 for i in range(len(dataset[0]))]
    
    for epoch in range(nb_epoch):
        for row in dataset:
            ycap = predict(row,coef)
            error = row[-1] - ycap
            coef[0] = coef[0] + learning_rate * error * ycap * (1 - ycap)
            for i in range(len(row) - 1):
                coef[i + 1] = coef[i + 1] + learning_rate * error * ycap * (1 - ycap) * row[i]
    return coef
    

def logistic_regression(train,test,learning_rate,nb_epoch):
    predictions = []
    coef = sgd_logistic(train, nb_epoch, learning_rate)
    for row in test:
        ycap = predict(row,coef)
        ycap = round(ycap)
        predictions.append(ycap)
    return predictions
        
        
filename = 'pima-indians-diabetes.data.csv'
dataset = load_csv(filename)
str_to_float(dataset)
minmax = minmax_dataset(dataset)
normalize_dataset(minmax, dataset)
#f = cross_validation(dataset,5)
n_folds = 5
learning_rate = 0.01
nb_epoch = 1000
scores = evaluate_algorithm(dataset,logistic_regression, n_folds, learning_rate,nb_epoch)
print(scores)