voca = input()

lst = [0] * 26

for i in voca:
    lst[ord(i)-97] += 1

print(*lst)