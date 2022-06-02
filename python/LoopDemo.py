print("Exponentation")
number = 2
exponent = 3
product = 1
for eachPass in range(exponent):
    product = product * number
    print(product, end = ' ')

print()

print("range")
product = 1
for count in range (4):
    print("times through loop is ", count)
    product = product * (count + 1)
print(product)

print("range with lower bound")
product = 1
for count in range (1,5):
    print("times through loop is ", count)
    product = product * (count + 1)
print(product)

print("using step value (count by)")
theSum = 0
for count in range(2, 11, 2):
    print("loop counter ", count)
    theSum += count
print(theSum)
