def findSecondMax(arr):
    large = secondLarge = -1
    for i in arr:
        if i > large:
            secondLarge = large
            large = i
        elif secondLarge < i < large:
            secondLarge = i
    return secondLarge
#Importation in happened here
import sys
def findSecondMin(arr):
    min = secondMin = sys.maxsize
    for i in arr:
        if i<min:
            secondMin = min
            min = i
        elif min < i < secondMin:
            secondMin = i
    return secondMin


nums = [2, 3, 4, 5, 6]
print(f"Second Max = {findSecondMax(nums)} And Second Minimum = {findSecondMin(nums)}")


