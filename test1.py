print ("Hello World")

for i in range(1, 11):
    if i == 10:
        print (i)
    elif i == 1:
        print(i, end = "#, ")
    else:
        print(i, end = ", ")

i = 1
while i<=10:
    print(i, end = ", ")
    i += 1

print("a","b","c", sep=",")