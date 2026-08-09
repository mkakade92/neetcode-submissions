class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        lNum = len(numbers)
        res = []

        for i in range(len(numbers)):
            #binsearch for target-numbers[i]
            toSearch = target-numbers[i]
            st =i+1
            end = lNum-1

            while st<=end:
                mid = (st+end)//2
                if toSearch == numbers[mid]:
                    return [i+1,mid+1]
                elif toSearch < numbers[mid]:
                    end = mid-1
                else:
                    st = mid+1
        return []