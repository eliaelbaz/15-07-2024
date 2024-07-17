## start

while True:
    num = int(input("Enter a positive odd number greater than 0: "));
    if num % 2 != 0:
        break
for i in range(1, num + 1, 2):
    print(("*" * i).center(num));

## End