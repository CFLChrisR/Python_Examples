BlankArray = []
UserInput = int(input(f"\nEnter a number:"))
while UserInput > 0:
    BlankArray.append(UserInput % 2)
    UserInput = UserInput // 2
    BlankArray.reverse()
for i in BlankArray:
    print(i,end="")