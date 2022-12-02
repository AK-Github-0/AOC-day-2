dict3 = {
    "A X" : 4,
    "A Y" : 8,
    "A Z" : 3,
    
    "B X" : 1,
    "B Y" : 5,
    "B Z" : 9,
    
    "C X" : 7,
    "C Y" : 2,
    "C Z" : 6,

}

f = open("input.txt", "r")
sum2 = 0
for line in f:
  sum2 += dict3[line.split("\n")[0]]


print(sum2)
