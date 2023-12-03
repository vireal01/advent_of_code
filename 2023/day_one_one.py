import re
import functools

f = open("../one_sample.txt", "rt", encoding='utf8')
ans = []
for line in f:
    value = re.compile('\D').sub('', line)
    ans.append(int(value[0] + value[-1]))
print(ans)
print(functools.reduce(lambda a, b: a+b, ans))


