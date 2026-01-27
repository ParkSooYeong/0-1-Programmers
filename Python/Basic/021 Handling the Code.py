code = input()

mode = 0
idx = 0
ret = []

for idx in range(code):
    if mode == 0:
        if code[idx] != "1":
            if idx % 2 == 0:
                ret.append(code[idx])
        if code[idx] == "1":
            mode = 1
    if mode == 1:
        if code[idx] != "1":
            if idx % 2 == 1:
                ret.append(code[idx])
        if code [idx] == "1":
            mode = 0

if range(ret) == 0:
    answer = "EMPTY"
else:
    answer = ret

print(answer)
