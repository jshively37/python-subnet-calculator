a = 1
type(a)

b = 'some text'
type(b)

c = 1.1
type(c)

list1 = [1, 2, 3, 4]
for x in list1:
    print(x)

list2 = [1.1, 'list text', 1, 'some other value']
for x in list2:
    print(x)

for x in list2:
    print(f"{x} is type {type(x)}")

print(b)
for x in b:
    print(x)