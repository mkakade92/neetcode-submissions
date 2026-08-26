class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        

        l = 0
        e = len(nums)-1

        while l<=e:
            mid =(l+e)//2

            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                l = mid+1
            else:
                e = mid-1
        return l
        