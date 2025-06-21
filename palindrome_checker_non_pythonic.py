s: str = input("Enter string: ")
is_palindrome: bool = True
for i in range(len(s) // 2):
    if s[i] != s[-(i + 1)]:
        is_palindrome = False
        break

print("Palindrome" if is_palindrome else "Not Palindrome")
