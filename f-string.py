''''
2 There is a list of friends [""John"", ""Marta"", ""James"", ""Amanda"", ""Marianna""].
 print to the console the names of each on a new line, right-aligned using the string method and formatting via f string.
 Also, above the names, in the first line, display the headings Names where the word names should be in the middle, and the rest of the space is filled with the symbol ""*""
3 There is a string "" name=Amanda=sssss&age=32&&salary=1500&currency=euro "".
 Convert this string to a dictionary {name: Amanda, age: 32, salary: 1500, currency: quro}'''


#1 Capital letter

names_string = "john peter brian Morgan Adam Maria bart"
print(f'{names_string.title()}')

#2

#3 Dictionary
# mess_string = 'name=Amanda=sssss&age=32&&salary=1500&currency=euro'
# print(mess_string.split('='))
# for el in mess_string:
#     if el.isalpha():
#         print(el, end='')
#     else:
#         continue
# print()

#4
list1 = ['FirstItem', 'FriendsList', 'MyTuple']
list2 = []
for el in list1:
    for n in el:
        if n.isupper() and n!= el[0]:
            list2.append('_')
            list2.append(n.lower())
        else:
            list2.append(n.lower())
    list2.append(' ')
list2 = ''.join(list2).split()
print(list2)