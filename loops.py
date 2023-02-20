if __name__ == '__main__':

#1
    counter = 1
    list1 = []
    while counter < 3:
        list1.append(counter)
        counter += 1
    print(list1)

    total = 1
    while True: #enter here 0 to stop the loop
        x = int(input())
        if x == 0:
            break
        total *= x
    print(total)

    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
      print(x, end=' ')
    print()

#2
    var = 10
    result = True if var == 10 else False
    print(f'{result}')

#3
    list1 = [1, 2, 3, 4, 5, 6, 7, 8]
    list2 = []
    list3 = []
    index = 0
    for value in list1:
        if value % 2 == 0:
            list2.append((index, value))
        else:
            list3.append((index, value))
        index += 1
    print(f'{list2}\n{list3}')

#4
    friends = ["John", "Marta", "James"]
    enemies = ["John", "Johnatan", "Artur"]

    for i in friends:
        if i == "James":
            continue
        elif i in enemies:
            print(f'{i} we are not friends anymore')
        elif i not in enemies:
            print(f'{i} we are the best friends')
