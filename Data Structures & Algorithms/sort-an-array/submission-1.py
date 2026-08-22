class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        import random
        def partition(arr,low,high):

            pivot = random.randrange(low,high+1)
            arr[pivot],arr[high] = arr[high],arr[pivot]
            
            i  = low - 1

            for j in range(low,high):
                if arr[j] < arr[high]:
                    i+=1
                    arr[i],arr[j] = arr[j],arr[i]
            
            arr[i+1],arr[high] = arr[high],arr[i+1]
            return i+1
        
        def qsort(arr,low,high):

            if low < high:
                part = partition(arr, low,high)
                qsort(arr,low,part-1)
                qsort(arr,part+1,high)
        
        qsort(nums,0,len(nums)-1)

        return nums