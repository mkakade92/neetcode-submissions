class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        tot = m + n

        k = 0
        i = 0
        j = 0
        prev, curr = None, None

        while k != (tot // 2 + 1):
            if i == m:
                prev = curr
                curr = nums2[j]
                j += 1
            elif j == n:
                prev = curr
                curr = nums1[i]
                i += 1
            elif nums1[i] < nums2[j]:
                prev = curr
                curr = nums1[i]
                i += 1
            else:
                prev = curr
                curr = nums2[j]
                j += 1
            k += 1

        if tot % 2 == 0:
            return (prev + curr) / 2
        else:
            return curr