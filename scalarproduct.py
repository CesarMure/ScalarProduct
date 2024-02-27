import numpy as np

print("<---------FIRST VECTOR------------>")
vector1 = [
    int(input("First number: ")),
    int(input("second number: ")),
    int(input("third number: "))
]
print("<---------SECOND VECTOR------------>")
vector2 = [
    int(input("First number: ")),
    int(input("second number: ")),    
    int(input("third number: "))
]

x = vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]
a = vector1[0] * vector1[0] + vector1[1] * vector1[1] + vector1[2] * vector1[2]
b = vector2[0] * vector2[0] + vector2[1] * vector2[1] + vector2[2] * vector2[2]
    
a = np.sqrt([a])

b = np.sqrt([b])

over = a * b

output = np.arccos([x / over])
print(output)


input = int(input("Press 1 for line and plane, Press 2 For 2 planes"))

if input == 1:
  output = 0.5 - output
  print(output)
  
elif input == 2:
  output = 1 - output
  print(output)
else:
  print("Invalid Input")


