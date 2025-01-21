import random
import math
def cosineSimilarity(A,B):
    dotValue = 0
    valueA = 0 
    valueB = 0

    for i in range(len(A)):
        dotValue += A[i]*B[i]
        valueA += A[i]*A[i]
        valueB += B[i]*B[i]
    return dotValue/(math.sqrt(valueA)*math.sqrt(valueB))

def bubbleSort(unsorted):
    
    n = len(unsorted)
    for i in range(len(unsorted) - 1):
        for j in range(n - 1 - i):
            if unsorted[j][0] > unsorted[j + 1][0]:
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]

    


N = 20
M = 30
U = []
nMovieFeatures  = 15
nUserFeature = 10
for i in range(N):
    U.append([])
    for j in range(nUserFeature):
        U[i].append(random.random()) 


I = []
for i in range(M):
    I.append([])
    for j in range(nMovieFeatures):
        I[i].append(random.random())

R = []

for i in range(N):
    R.append([])

    for j in range(M):
        R[i].append(random.random())
    for j in range(M//3):
        index = int(random.random() * len(R[i])) - 1
        R[i][index] = -1

testUser = 1
topK = 5
similarityList = []
for i in range(N):
    if i != testUser:
        similarityList.append((cosineSimilarity(U[i], U[testUser]), i))
bubbleSort(similarityList)
predictedRatings = []
for i in range(M):
    if R[testUser][i] == -1:
        rating = 0
        sim = 0
        j = 0
        k = 0
        while j < topK:
            similarity = similarityList[k][0]
            userIndex = similarityList[k][1]
            if R[userIndex][i] != -1:
                rating += similarity*R[userIndex][i]
                sim += similarity
                j += 1
            k += 1
        predictedRating = rating/sim
        predictedRatings.append((predictedRating, i))
bubbleSort(predictedRatings)
print("Movie recommendation for user no:" + str(testUser ))
for i in range(topK):
    print("Movie no: " + str(predictedRatings[i][1]) + ", with a predicted rating of " + str(predictedRatings[i][0]))
print(":(")



ItemtoItemSimilarityMatrix = []
for i in range(M):
    ItemtoItemSimilarityMatrix.append([])
    for j in range(M):
        ItemtoItemSimilarityMatrix.append(cosineSimilarity(I[i], I[j]))