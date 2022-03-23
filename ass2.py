def reverse(str):
    string=""
    for i in str:
        string =i+string
    return string
str ="edyoda"
print("the original string is:",str)
print("the reverse string is:",reverse(str))
