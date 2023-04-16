

# Here a 2-D array arr[i][j] is used to store the maximum profit starting from the i'th item to the end with max allowed weight of j.
def Knapsack(profit,weight,maxWeight,arr,i=0):
    if maxWeight==0 or i>=len(profit):
        return 0

    # If there is already a stored max profit for items from i to the end, use the stored value.
    if arr[i][maxWeight] != -1:
        return arr[i][maxWeight]

    includedMax = 0
    # The current item can be included only if its weight doesn't exceed the maximum weight allowed.
    if weight[i] <= maxWeight:

        # Find the maximum profit gained by including the i'th item.
        includedMax = profit[i] + Knapsack(profit,weight,maxWeight-weight[i],arr,i+1)

    # Find the maximum profit gained by not including the i'th item.
    excludedMax = Knapsack(profit,weight,maxWeight,arr,i+1)

    # The overall maximum profit will be the highest of the included profit and excluded profit.
    # Store the corresponding profit as the profit for including items from i to end with maximum weight and return it.
    totalMax = max(includedMax,excludedMax)
    arr[i][maxWeight] = totalMax

    return arr[i][maxWeight]


n = 3 
profit = [20,30,40]
weight = [1,1,1]
maxWeight = 2
arr = [[-1 for i in range(maxWeight+1)] for j in range(n)]
print(Knapsack(profit,weight,maxWeight,arr))
