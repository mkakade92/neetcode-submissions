class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        st = []
        pairs = [(p,s) for p,s in zip(position[::-1],speed[::-1])]
        pairs.sort(reverse=True)
        for pos,spd in pairs:

            st.append((target-pos)/spd)
            if len(st)>=2 and st[-1] <= st[-2]:
                st.pop()
        return len(st)
