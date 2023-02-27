def caesar_cipher(string, offset):
    # Write your code here.
    #string_lower = string.lower()
    result = ""
    for each in string:
        print(each)
        if (ord(each) - offset) < 33:
            new = ord(each) - offset + 90
            print(new)
            result += chr(new)
        else:
            new = ord(each) - offset
            print(new)
            result += chr(new)
    return result


string = "leo"

offset = 25  # offset should be always < 26 (in order to stay inside the alphabet)
res = caesar_cipher(string, offset)
print(res)
string = res
offset = 90-25
print(caesar_cipher(string, offset))
