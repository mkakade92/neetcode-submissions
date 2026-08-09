class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        st = []

        for i in tokens:
            if i=='*':
                st.append(st.pop()*st.pop())
            elif i=='/':
                a,b = st.pop(),st.pop()
                st.append(int(float(b)/a))
            elif i=='-':
                a,b= st.pop(),st.pop()
                st.append(b-a)
            elif i=='+':
                st.append(st.pop()+st.pop())
            else:
                st.append(int(i))
        return st[0]