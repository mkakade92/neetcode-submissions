class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        buk = [[] for _ in range(3)]

        for num in nums:
            if num==0:
                buk[0].append(num)
            elif num==1:
                buk[1].append(num)
            else:
                buk[2].append(num)
        

        ind = 0

        for b in buk:
            for n in b:
                nums[ind] = n
                ind+=1
        