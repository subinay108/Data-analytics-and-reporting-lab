# Input a dataset
# Input a sample
# Find k nearest neighbors of the sample in the dataset
# - calculate the distance between input sample and other samples in the dataset
# - Among n distance find the k minimum distances
# - Find what is the most common label of those k-neighbors
# - Most common label is the output of the classifer

import pandas as pd

def euclidean_distance(X, Y):
    if len(X) != len(Y):
        raise ValueError('X and Y are of different sizes')
    
    s = 0
    for x, y in zip(X, Y):
        s += (x - y) ** 2
    
    return s ** 0.5;

def knn_classifier(dataset, inputData, k):
    distances = {}
    for sample in dataset:
        distances[euclidean_distance(sample[:-1], inputData)] = sample[-1]
    
    count = 0
    labelsCount = {}
    for i in sorted(distances):
        if distances[i] not in labelsCount:
            labelsCount[distances[i]] = 1
        else:
            labelsCount[distances[i]] += 1
        
        count += 1
        if count == k:
            break
    
    maxLabelCount = max(labelsCount.values())    
    for i in labelsCount:
        if labelsCount[i] == maxLabelCount:
            output = i
            break
    
    return output

if __name__ == '__main__':
    # dataset = [
    #     [30,    5,  'Cat'],
    #     [25,	4,	'Cat'],
    #     [35,	6,	'Cat'],
    #     [45,	20,	'Dog'],
    #     [50,	25,	'Dog']
    # ]
    df = pd.read_csv('Lab-8\datasets\gender_height_weight.csv')
    cols = df.columns.tolist()
    cols = cols[1:] + [cols[0]]
    df = df[cols]
    
    inputData = [40, 10]
    
    print(list(df))
    
    predicted_class = knn_classifier(df, inputData, 4)
    print('The predicted class of the given input :', predicted_class)