import re
import functools

dict = {'zero': 0, "one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"}

f = open("../one_sample.txt", "rt", encoding='utf8')

ans = []
for line in f:
    new_line = line
    for i in range(len(line)):
        for (key, value) in dict.items():
            if i < len(new_line):
                if new_line[i:].startswith(key):
                    new_line = new_line.replace(key, str(value), 1)

    row = re.compile('\D').sub('', new_line)
    value_to_append = int(row[0] + row[-1])

    ans.append(value_to_append)
print(ans)
print(functools.reduce(lambda a, b: a + b, ans))
