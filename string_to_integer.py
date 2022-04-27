class Solution:
    def myAtoi(self, s: str) -> int:
        st = list(s)
        n = ''
        while len(st) > 0 and st[0] == ' ':
            st.pop(0)
        if len(st) > 0 and (st[0] == '-' or st[0] == '+'):
            n += st[0]
            st.pop(0)
        while len(st) > 0 and st[0].isnumeric():
            n += st[0]
            st.pop(0)
        n = 0 if n == '' or n == '-' or n == '+' else int(n)
        n = -2**31 if n < -2**31 else n
        n = 2**31 - 1 if n > 2**31 - 1 else n
        return n