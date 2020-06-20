billThickness = 0.11 * 0.001
searsHeight = 442
numBills = 1
day = 1

while numBills * billThickness < searsHeight:
    print(day, numBills, numBills * billThickness)
    day = day + 1
    numBills = numBills * 2

print('Number of days', day)
print('Number of bills', numBills)
print('Final height', numBills * billThickness)