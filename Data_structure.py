my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(f"My appended list: {my_list}")

my_list[1] = 15

print(f"My list after inserting 15: {my_list}")

list2 = [50, 60, 70]
my_list.extend(list2)

print(f"List after extention; {my_list}" )

my_list.remove(70)

print(f"List after removing the last element: {my_list}")

my_list = [10, 15, 30, 40, 50, 60]
my_list.sort()


print(f"My list after sorting in ascending order: {my_list}")

my_list = [10, 15, 30, 40, 50, 60]

print(my_list[2])