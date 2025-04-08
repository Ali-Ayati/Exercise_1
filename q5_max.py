def find_max(a: int, b: int, c: int) -> int:
    max_num = a
    for i in [a, b, c]:
        if i > max_num:
            max_num = i
    return max_num

a, b, c = float(input("enter first number: ")), float(input("enter second number: ")), float(input("enter third number: "))

print(find_max(a, b, c))