def calculate_binary(s:str)->int:
        sum = 0
        pos = 0
        str_s = str(s)
        n = len(str_s)
        for x in range(n-1,-1,-1):
            sum+=(2**x)*(int(str_s[pos]))
            pos+=1
        return sum
hi = calculate_binary(1101)
print(hi)