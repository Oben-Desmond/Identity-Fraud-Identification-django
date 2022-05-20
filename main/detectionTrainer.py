#supervised machine learning with KNN and anormally detection

# import the necessary packages
# import libraries
from cmath import sqrt

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
import math
 


def convertToNumber (s):
    return int.from_bytes(s.encode(), 'little')

def convertFromNumber (n):
    return n.to_bytes(math.ceil(n.bit_length() / 8), 'little').decode()


# import data from csv file
# url for the dataset iris
url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"


def getAnormally(data):
   
    # df = data[["amount", "created_at","receiver_id","sender_id","type","id"]]
    
   
    print(data)
    return
    
    
    for i in range(len(df["receiver_id"])):
            df["receiver_id"][i]=convertToNumber(df["receiver_id"][i])
            print(df["receiver_id"][i])
       
    
    for i in range(len(df["sender_id"])):
            df["sender_id"][i]=convertToNumber(df["sender_id"][i])


    for i in range(len(df["type"])):
        df["type"][i]=convertToNumber(df["type"][i])
    
    X= df.values
    
    

    k=3 # number of neighbors

    nbrs = NearestNeighbors(n_neighbors=k, algorithm='ball_tree')\

    nbrs.fit(df)


    # distances and indexes of k-neaighbors from model outputs
    distances, indexes = nbrs.kneighbors(X) # plot mean of k-distances of each observation
    # plt.plot(distances.mean(axis =1))
    # plt.show()

    cutoff = []
    cutoff=distances.mean(axis =1)
    # find average of cuttoff values
    cutoff_avg = cutoff.mean()
    print("cutoff: ", cutoff_avg)
    outlier_index = np.where(distances.mean(axis = 1) >cutoff_avg)


    # filter outlier values
    outlier_values = df.iloc[outlier_index]
    print(outlier_values)

    return  list(outlier_values["id"])

    # plot data
    # plt.scatter( df["type"], df["sender_id"],color = "b", s = 65)# plot outlier values
    # plt.scatter(outlier_values["type"], outlier_values["sender_id"],  color = "r")
    # plt.show()