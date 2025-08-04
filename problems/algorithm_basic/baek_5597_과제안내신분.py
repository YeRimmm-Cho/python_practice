student_lst = []
for i in range(1, 31):
    student_lst.append(i)

for j in range(28):
    id_num = int(input())
    student_lst.remove(id_num)

student_lst.sort()

print(student_lst[0])
print(student_lst[1])

