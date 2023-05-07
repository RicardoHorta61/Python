s = "olo olo ola"

def verify_palindrome(s):
    s = s.replace(" ", "")
    s = s.replace(",", "")
    z = s[::-1]
    if s == z:
        return print("It is polindrome!")
    else:
        return print("It is not polindrome!")

verify_palindrome(s)