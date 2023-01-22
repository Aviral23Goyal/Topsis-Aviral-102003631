#Importing Libraries
import pandas as pd
import numpy as np
import sys

def main():
    #Reading Dataset
    data=pd.read_csv(sys.argv[1])

    if len(sys.argv)!=5:
        print("Parameter Error")
        exit()
        try:
            with open(sys.argv[1], 'r') as filee:
                file=pd.read_csv(filee)
        except FileNotFoundError:
            print("File not found")
            exit()

    #Copying numerical values into another dataframe
    col=len(data.axes[1])
    new_data = data.iloc[:,1:col+1]
    new_data

    #Weights
    #w = [0.25,0.25,0.25,0.25]
    #impact = ['-','+','+','+']
    w = list(map(float,sys.argv[2].split(',')))
    impact = list(map(str,sys.argv[3].split(',')))

    norm_data=new_data/np.sqrt(np.power(new_data.iloc[:,0:col],2).sum(axis=0))
    norm_data

    #Creation of Weighted Normalised Decision Matrix

    norm_wdata = norm_data * w
    norm_wdata

    #Identifying Ideal best and Ideal worst values

    ideal_best=[]
    ideal_worst=[]
    for i in range(0,col-1):
        if(impact[i]=="+"):
            ideal_best.append(norm_wdata.iloc[:,i].max())
            ideal_worst.append(norm_wdata.iloc[:,i].min())
        else:
            ideal_best.append(norm_wdata.iloc[:,i].min())
            ideal_worst.append(norm_wdata.iloc[:,i].max())

    print("Ideal best Values\n")
    print(ideal_best)

    print("\nIdeal worst Values\n")
    print(ideal_worst)

    #Separation/Euclidean distance Measurements 
    #from Ideal best
    dis_ib = np.sqrt(np.power(norm_wdata - ideal_best , 2).sum(axis=1))

    #from Ideal Worst
    dis_iw = np.sqrt(np.power(norm_wdata - ideal_worst , 2).sum(axis=1))

    print("\nDistance from Ideal Best :\n",dis_ib)
    print("\nDistance from Ideal Worst :\n",dis_iw)

    #Performance Score Calculation
    per_score = dis_iw / (dis_ib + dis_iw )

    print("Performance Scores are :\n", per_score)

    data.insert(col,"Performance",per_score,True)
    data

    rank=data.sort_values(['Performance'],ascending=False).index
    data['Rank']=pd.Series(range(1,len(data)+1),index=rank)
    data

    data.to_csv(sys.argv[4])