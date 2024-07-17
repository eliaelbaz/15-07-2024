## start

positive_count: int = 0;
negative_count = 0;
zero_count = 0;
divisible_by_7_count = 0;
last_positive = None;
last_negative = None;

for _ in range(10):
    num = int(input("Enter a number: "));

    if num == -9999:
        break
    if num > 1000 or num < -1000:
        continue

    if num > 0:
        positive_count += 1
        last_positive = num
    elif num < 0:
        negative_count += 1
        last_negative = num
    else:
        zero_count += 1

    if num % 7 == 0:
        divisible_by_7_count += 1

else:
    print(f"""
    Positive numbers: {positive_count}
    Negative numbers: {negative_count}
    Zeros: {zero_count}
    Numbers divisible by 7: {divisible_by_7_count}
    Last positive number: {last_positive if last_positive is not None else 'None'}
    Last negative number: {last_negative if last_negative is not None else 'None'}
    """);

## End
