"""
----------------------------------------------------
-- CMPSC_132, Spring 2024, Bashir Hilaly
-- Bucket Sort
----------------------------------------------------
"""
import math
import random

"""

<---------PSEUDO CODE---------->

BucketSort(numbers, numbersSize, bucketCount) {
   if (numbersSize < 1)
      return

   buckets = Create list of bucketCount buckets

   // Find the maximum value
   maxValue = numbers[0]
   for (i = 1; i < numbersSize; i++) {
      if (numbers[i] > maxValue)
         maxValue = numbers[i]
   }

   // Put each number in a bucket
   for each (number in numbers) {
      index = floor(number * bucketCount / (maxValue + 1))
      Append number to buckets[index]
   }

   // Sort each bucket
   for each (bucket in buckets)
      Sort(bucket)

   // Combine all buckets back into numbers list
   result = Concatenate all buckets together
   Copy result to numbers
}
"""

def BucketSort(lst, bucketCount):
    if len(lst) < 1:
        return
    
    buckets = [[] for i in range(bucketCount)]

    # Find the max value
    maxValue = lst[0]
    for num in lst[1:]:
        if num > maxValue:
            maxValue = num

    # Put each number in a bucket
    for num in lst:
        index = math.floor(num * bucketCount / (maxValue + 1))
        buckets[index].append(num)

    # DEBUGGING - Print out buckets
    #print("Buckets: ", buckets)

    # Sort each bucket
    for bucket in buckets:
        bucket.sort()

    # Combine all buckets back into numbers list
    result = []
    for bucket in buckets:
        for num in bucket:
            result.append(num)
    
    lst = result
    return lst


if __name__ == "__main__":

    numbers = [random.randint(1, 100) for i in range(40)]

    #numbers = [5,23,5,456,453,5,54,3,3,4,62,54,34,535,35,3,5,34,54,34,4,5,431,36,34]

    print("Before Bucket Sort: ", numbers)

    print("After Bucket Sort: ", BucketSort(numbers, 5))