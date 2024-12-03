def part_one():
    f = open("data.txt", "r")
    data = f.readlines()
    first_list = list(map(lambda x: int(x.split('')[0]), data))
    second_list = list(
        map(lambda x: int(x.split('')[1]), data))
    first_list.sort()
    second_list.sort()
    sum = 0
    for x, y in zip(first_list, second_list):
        sum += abs(x-y)
    print(sum)


def part_two():
    f = open("data.txt", "r")
    data = f.readlines()
    first_list = list(map(lambda x: int(x.split('')[0]), data))
    second_list = list(
        map(lambda x: int(x.split('')[1]), data))
    first_list.sort()
    second_list.sort()
    sum = 0
    for item in first_list:
        length = len(list(filter(lambda x: x == item, second_list)))
        if length > 0:
            sum += (item * length)
    print(sum)


