class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        m = len(nums1)
        n = len(nums2)

        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
            
        tot = m+n

        half = (tot+1)//2

        NEG_INF = -float('inf')
        POS_INF =float('inf')

        st = 0
        en = min(m,n)
        while st <= en:
            x = (st + en) // 2
            y = half - x

            if y > n:
                st = x + 1
                continue
            if y < 0:
                en = x - 1
                continue

            n1_l = nums1[x - 1] if x > 0 else NEG_INF
            n1_r = nums1[x] if x < m else POS_INF
            n2_l = nums2[y - 1] if y > 0 else NEG_INF
            n2_r = nums2[y] if y < n else POS_INF

            if n1_l <= n2_r and n2_l <= n1_r:
                if tot % 2 == 0:
                    return (max(n1_l, n2_l) + min(n1_r, n2_r)) / 2
                else:
                    return max(n1_l, n2_l)
            elif n1_l > n2_r:
                en = x - 1
            else:
                st = x + 1

        return None

            

            