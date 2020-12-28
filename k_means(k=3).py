import numpy as np

def calculate(x1, y1, x2, y2): # calculating the distance between two points
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    return ((((x2-x1)**2.0 + (y2-y1)**2.0))**(1.0/2.0))

def meanX(cluster):  # calculating meanX of the cluster
    xTotal = 0.0
    lenght = 0.0
    for i in cluster:
        xTotal += float(i[1])
        lenght += 1.0
    xTotal = xTotal / lenght
    return xTotal

def meanY(cluster):  # calculating meanY of the cluster
    yTotal = 0.0
    lenght = 0.0
    for i in cluster:
        yTotal += float(i[2])
        lenght += 1.0
    yTotal = yTotal / lenght
    return yTotal

def minDistance(distance1, distance2, distance3):   # calculating the min distance to add the pointX to clusterX
    if (distance1 < distance2) and (distance1 < distance3):
        min = distance1
    elif (distance2 < distance1) and (distance2 < distance3):
        min = distance2
    else:
        min = distance3
    return min



DATA_SET = [      # Example data set

    ['A',3,3],
    ['B',8,5],
    ['C',4,4],
    ['D',2,4],
    ['E',7,7],
    ['F',5,8],
    ['G',3,5],
    ['H',4,8],
    ['I',6,9],
    ['J',9,6]

]

CLUSTER_1 = [DATA_SET[0]] # A
CLUSTER_2 = [DATA_SET[4]] # E      # Example clusters
CLUSTER_3 = [DATA_SET[7]] # H

cluster1Set = []
cluster2Set = []
cluster3Set = []

for i in range(10):  # We have 10 points, loop should be range(10)
    distance1 = calculate(DATA_SET[i][1],DATA_SET[i][2],DATA_SET[0][1],DATA_SET[0][2])
    distance2 = calculate(DATA_SET[i][1],DATA_SET[i][2],DATA_SET[4][1],DATA_SET[4][2])
    distance3 = calculate(DATA_SET[i][1],DATA_SET[i][2],DATA_SET[7][1],DATA_SET[7][2])

    min = minDistance(distance1,distance2,distance3)

    if (min == distance1):
        cluster1Set.append(DATA_SET[i])

    elif (min == distance2):
        cluster2Set.append(DATA_SET[i])

    elif (min == distance3):
        cluster3Set.append(DATA_SET[i])


while True:        # Checking the sets
    b = 0

    newCluster1Set = []
    newCluster2Set = []
    newCluster3Set = []

    meancluster1x = meanX(cluster1Set)
    meancluster1y = meanY(cluster1Set)
    meancluster2x = meanX(cluster2Set)
    meancluster2y = meanY(cluster2Set)
    meancluster3x = meanX(cluster3Set)
    meancluster3y = meanY(cluster3Set)

    for b in range(10):
        newDistance1 = calculate(DATA_SET[b][1], DATA_SET[b][2], meancluster1x, meancluster1y)
        newDistance2 = calculate(DATA_SET[b][1], DATA_SET[b][2], meancluster2x, meancluster2y)
        newDistance3 = calculate(DATA_SET[b][1], DATA_SET[b][2], meancluster3x, meancluster3y)

        newMin = minDistance(newDistance1, newDistance2, newDistance3)

        if (newMin == newDistance1):
            newCluster1Set.append(DATA_SET[b])

        elif (newMin == newDistance2):
            newCluster2Set.append(DATA_SET[b])

        elif (newMin == newDistance3):
            newCluster3Set.append(DATA_SET[b])

    if (newCluster1Set != cluster1Set and newCluster2Set != cluster2Set and newCluster3Set != cluster3Set):
        cluster1Set = newCluster1Set
        cluster2Set = newCluster2Set
        cluster3Set = newCluster3Set

    else:
        break

print("Cluster 1: ", newCluster1Set, "\n" + "Cluster 2: ", newCluster2Set, "\n" + "Cluster 3: ", newCluster3Set)


















