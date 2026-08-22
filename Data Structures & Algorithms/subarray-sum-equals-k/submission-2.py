class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        pre = {0:1}
        currSum = 0
        subCount = 0
        for num in nums:
            currSum+=num

            diff = currSum-k

            subCount+=pre.get(diff,0)
            pre[currSum] = pre.get(currSum,0)+1
                    
        return subCount

            