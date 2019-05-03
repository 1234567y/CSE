import csv
test_num = "5337843058931904"
# list1 = list(test_num)
# print(list1)


def validate(num: str):
    if len(num) is not 16:
        print("does not pass.")
        return False
    last_num = int(num[15])
    new_list = list(num)[:15][::-1]
    print(new_list)
    print(last_num)
    for index in range(len(new_list)):
        new_list[index] = int(new_list[index])
        if index % 2 == 0:
            new_list[index] *= 2
            if new_list[index] > 9:
                new_list[index] -= 9
    print(new_list)
    total = sum(new_list)
    print(total)
    return total % 10 == last_num


print(validate(test_num))


with open("Book1.csv", 'r') as test_num:
