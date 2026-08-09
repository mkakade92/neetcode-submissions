class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        print(nums)

        def twoSum(nums2,target):
            l = 0
            r = len(nums2) - 1

            # print(f"Searching for {target} in {nums2}")

            ans = []
            while l<r:
                if nums2[l]+nums2[r]==target:
                    # print(f"Found {[nums2[l],nums2[r],-target]}")
                    ans.append([nums2[l],nums2[r],-target])
                    l+=1
                    r-=1
                    while nums2[l]==nums2[l-1] and l<r:
                        l+=1
                elif nums2[l]+nums2[r]<target:
                    l+=1
                else:
                    r-=1
            return ans
        res = []
        
        for i,num in enumerate(nums):
            if num>0:
                break
            if i>0 and num==nums[i-1]:
                continue
            
            k = twoSum(nums[i+1:],-nums[i])
            # print(f"k = {k}")
            for l in k:
                res.append(l)
        return res
            