# 알파벳 대문자랑 0~9 
import re

S = input()

onlyN = re.sub(r'[^0-9]', '', S)

onlyS = list(filter(str.isalpha, S))
onlyS.sort()

onlyS = ''.join(onlyS)

num = 0
for i in onlyN:
    num += int(i)

print(onlyS+str(num))