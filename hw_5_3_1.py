## start

num: int = int(input("Enter a positive number greater than 0: "));
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(j, end="");
    print();

for i in range(num - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end="");
    print();

## End