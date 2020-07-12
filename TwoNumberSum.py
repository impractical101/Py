#Two number sum
#This problem can be solved using a single for loop but that will have more time complexity.
#Will be covering the two soltions. One using the hash table and another one using double for loops.

#1. Using double for loops. We will have time complexitu of O(nlogn) because of sorting and space complexity of O(1).
#Lets get started

nums = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10
#First step we will be doing is to sort the array.
nums = sorted(nums)
left, right= 0, len(nums) -1
check = 0
while left < right:
    check = left + right
    if check == target:
        print([nums[left], nums[right]]) 
    elif check < target:
        left += 1
    elif check > target:
        right -= 1
print([])


#2. Solution using hash table
# Checking the availibilty of differnce of target and num in dic.
    dic = {}
    for num in nums:
        if target - num in dic:
            return [target - num, num]
        else: dic[num] = true  
    return []