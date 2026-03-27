from collections import Counter
users = dict()
common_items = []
unique_items = set()

print("Enter number of users: " , end = ' ')
num_users = int(input())

if num_users < 1:
    print("Invalid number of users")
    exit()

for i in range(num_users):
    user_items = []

    print("Enter username: " , end = ' ')
    username = str(input())

    print("How many items? " , end = ' ')
    num_items = int(input())
    if num_items < 1:
        print("Invalid number of items")
        exit()

    for j in range( 1, num_items + 1):
        print("Item %d: " % j, end = ' ')
        item = str(input())
        user_items.append(item)
        users[username] = user_items


print("USER DATA:")
for user in users:
    print(user, "->", users[user])

for (key, value) in users.items():
    for item in value:
        unique_items.add(item)


print()

print("COMMON ITEMS:")
for (key, value) in users.items():
    for item in value:
        common_items.append(item)


common_items_counter = Counter(common_items)
for (key, value) in common_items_counter.items():
    if value > 1:
        print(key)


print()

print("UNIQUE ITEMS:")

for(key,value) in common_items_counter.items():
    if value == 1:
        print(key)

print()

print("MOST POPULAR ITEM:")
print(Counter(common_items).most_common(1)[0][0])







