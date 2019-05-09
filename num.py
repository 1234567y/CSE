import csv


with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    totalF = 0
    totalC = 0
    totalB = 0
    totalO = 0
    totalCm = 0
    totalS = 0
    totalM = 0
    totalPC = 0
    totalV = 0
    totalH = 0
    totalBF = 0
    totalCE = 0
    for row in reader:
        old_number = row[13]
        if row[2] == "Fruits":
            num = float(old_number)
            totalF += num
        if row[2] == "Clothes":
            num = float(old_number)
            totalC += num
        if row[2] == "Beverages":
            num = float(old_number)
            totalB += num
        if row[2] == "Meat":
            num = float(old_number)
            totalM += num
        if row[2] == "Office Supplies":
            num = float(old_number)
            totalO += num
        if row[2] == "Cosmetics":
            num = float(old_number)
            totalCm += num
        if row[2] == "Snacks":
            num = float(old_number)
            totalS += num
        if row[2] == "Personal Care":
            num = float(old_number)
            totalPC += num
        if row[2] == "Vegetables":
            num = float(old_number)
            totalV += num
        if row[2] == "Household":
            num = float(old_number)
            totalH += num
        if row[2] == "Baby Food":
            num = float(old_number)
            totalBF += num
        if row[2] == "Cereal":
            num = float(old_number)
            totalCE += num
print('Fruits = ', round(totalF, 2))
print('Clothes = ', round(totalC, 2))
print('Beverages = ', round(totalB, 2))
print('Meat = ', round(totalM, 2))
print('Office Supplies = ', round(totalO, 2))
print('Cosmetics = ', round(totalCm, 2))
print('Snacks = ', round(totalS, 2))
print('Personal Care = ', round(totalPC, 2))
print('Vegetables = ', round(totalV, 2))
print('Household = ', round(totalH, 2))
print('Baby Food = ', round(totalBF, 2))
print('Cereal = ', round(totalCE, 2))
