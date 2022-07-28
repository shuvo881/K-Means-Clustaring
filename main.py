from matplotlib import pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
import math

def distance(p1, p2):
    d = math.dist(p1, p2)
    return d



df = pd.read_csv("Clustering.csv")
x = df["x"]
y = df["y"]


print("Enter value of K: ")

k = int(input())
cntroid = []

for i in range(k):
    cntroid.append([x[i], y[i]])




while(1):

    nCnX = [0 for i in range(k)]
    nCnY = [0 for i in range(k)]
    numberClaster = [0 for i in range(k)]
    newCntoid = []
    assignGroup = list()
    for i in range(len(x)):

        dist = []
        for j in range(k):
            dist.append(distance(cntroid[j], [x[i], y[i]]))
        minDist = min(dist)
        minIndex = dist.index(minDist)
        assignGroup.append(minIndex)
       # print(assignGroup)
        nCnX[minIndex] = nCnX[minIndex] + x[i]
        nCnY[minIndex] = nCnY[minIndex] + y[i]
        numberClaster[minIndex] = numberClaster[minIndex] + 1


    for i in range(k):
        newCntoid.append([nCnX[i] / numberClaster[i], nCnY[i] / numberClaster[i]])
    if(newCntoid == cntroid):
        break;
    cntroid = newCntoid



print("The Cluster Array")

print(assignGroup)

cntroidXCOlor = [[] for i in range(k)]

cntroidYCOlor = [[] for i in range(k)]
j = 0
for i in assignGroup:
    cntroidXCOlor[i].append(x[j])
    cntroidYCOlor[i].append(y[j])
    j = j + 1

colors = "bgrcmykw"
color_index = 0

for i in range(k):
    plt.scatter(cntroidXCOlor[i], cntroidYCOlor[i], s=30, c=colors[color_index])
    color_index += 1

plt.show()