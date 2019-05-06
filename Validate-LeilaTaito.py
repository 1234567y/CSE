import csv
test_num = "4556737586899855"
# list1 = list(test_num)
# print(list1)


def validate(num: str):
    if len(num) is not 16:
        print("does not pass.")
        return False
    last_num = int(num[15])
    new_list = list(num)[:15][::-1]
    print(new_list)
    for index in range(len(new_list)):
        new_list[index] = int(new_list[index])
        if index % 2 == 0:
            new_list[index] *= 2
            if new_list[index] > 9:
                new_list[index] -= 9
    total = sum(new_list)
    return total % 10 == last_num


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        for row in reader:
            old_number = row[0]
            if validate(old_number):
                writer.writerow(row)

print(validate(test_num))
