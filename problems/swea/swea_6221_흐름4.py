case = ["가위", "바위", "보"]

man1 = input()
man2 = input()

if case.index(man1) == case.index(man2):
    print("Result : Draw")
elif case.index(man1) - case.index(man2) == 1:
    print("Result : Man1 Win!")
elif case.index(man1) - case.index(man2) == 2:
    print("Result : Man2 Win!")