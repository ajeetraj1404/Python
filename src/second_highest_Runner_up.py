'''
Find the runner up/ Second highest score but not the same score
ex: 6,6 both player scored 6 its tie but not the second highest score
6 6 5, here 5 is the highest
'''
n = int(input())
arr = list(map(int, input().split())) #List input
arr = list(set(arr)) # Remove duplicates
arr1 = sorted(arr,reverse=True) # Sort descending order
print(arr1[1]) # Print the second runner up but not the same marks scorer
