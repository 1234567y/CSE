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
Fruits = round(totalF, 2)
Clothes = round(totalC, 2)
Beverages = round(totalB, 2)
Meat = round(totalM, 2)
Office_Supplies = round(totalO, 2)
Cosmetics = round(totalCm, 2)
Snacks = round(totalS, 2)
Personal_Care = round(totalPC, 2)
Vegetables = round(totalV, 2)
Household = round(totalH, 2)
Baby_Food = round(totalBF, 2)
Cereal = round(totalCE, 2)
Item = [Fruits, Clothes, Beverages, Meat, Office_Supplies, Cosmetics, Snacks, Personal_Care, Vegetables, Household,
        Baby_Food, Cereal]
item_names = ["Fruits", "Clothes", "Beverages", 'Meat', 'Office_Supplies', "Cosmetics", 'Snacks', 'Personal_Care',
              'Vegetables', 'Household', 'Baby_Food', 'Cereal']
print("Fruits =", Fruits)
print('Clothes =', Clothes)
print('Beverages =', Beverages)
print('Meat =', Meat)
print('Office Supplies =', Office_Supplies)
print('Cosmetics =', Cosmetics)
print('Snacks =', Snacks)
print('Personal Care =', Personal_Care)
print('Vegetables =', Vegetables)
print('Household =', Household)
print('Baby Food =', Baby_Food)
print('Cereal =', Cereal)
highest_profit = max(Item)
index = Item.index(highest_profit)
item_name = item_names[index]
print("The one with the highest profit is", item_name)
