dict = {
  
    "A X" : 3,
    "A Y" : 4,
    "A Z" : 8,
  
    "B X" : 1,
    "B Y" : 5,
    "B Z" : 9,
  
    "C X" : 2,
    "C Y" : 6,
    "C Z" : 7,

}

f = open("input.txt", "r")
sum1 = 0
for line in f:
  sum1 += dict3[line.split("\n")[0]]


print(sum1)
