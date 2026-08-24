class Solution:
    def calPoints(self, operations: List[str]) -> int:

        st = []

        for op in operations:
            if op == "D":
                if st[-1]:
                    st.append(2*st[-1])
                continue
            if op == "C":
                st.pop()
                continue
            if op == "+":
                if st[-1] and st[-2]:
                    st.append(st[-1]+st[-2])
                continue
            else:
                st.append(int(op))
        return sum(st)