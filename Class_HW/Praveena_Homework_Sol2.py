# Program to calculate the number of times a characters appears consecutively and place it next to the count

word = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
count = 1
length = ""
for i in range(1, len(word)):
    if word[i-1] == word[i]:
       count += 1
    else :
        length += str(count)+word[i-1]
        count = 1
length = length + str(count)+word[i]
print(length)

