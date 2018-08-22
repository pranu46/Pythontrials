# Program to calculate number of steps to obtain keprekar constant

count = 0
val = input("Enter a number:")
if (len(val) < 4):
    val = val.zfill(4)

while True:
    l1 = sorted(list(val))
    l2 = sorted(l1[:], reverse=True)
    l1 = int("".join(l1))
    l2 = int("".join(l2))
    result = l2 - l1
    count = count + 1
    if ((result == 0) or (result == 6174)):
        break
    val = str(result)
print("Number of attempts:", count)

