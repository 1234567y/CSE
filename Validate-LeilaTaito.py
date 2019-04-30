test_num = "2067233931768570"
string1 = "2067233931768570"
list1 = list(string1)
print(list1)
print(len(list1))


def validate(num: str):
    if len(list1) is not 16:
        print("does not pass.")

    new_list = list1[0:15][::-1]
    print(new_list)
    for index in range(len(new_list)):
        new_list[index] = int(new_list[index])
        if index % 2 == 0:
            new_list[index] *= 2
            if new_list[index] >= 9:
                new_list[index] -= 9
    newer_list = sum(new_list)
    print(newer_list)
    print(71 % 10)


print(validate(test_num))
