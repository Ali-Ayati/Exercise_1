def is_pallindrome(string: str) -> bool:
    string = string.lower()
    if string == string[::-1]:
        return True
    else:
        return False
    
my_str = input()

# print(is_pallindrome(my_str))

if is_pallindrome(my_str):
    print("YES")
else:
    print("NO")
