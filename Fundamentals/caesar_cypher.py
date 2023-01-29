def caesar_cipher(string, offset):
    # Write your code here.
    string_lower = string.lower()
    result = ""
    for each in string_lower:
        if (ord(each) - offset) < 97:
            new = ord(each) - offset + 26
            result += chr(new)
        else:
             new = ord(each) - offset
             result += chr(new)
    return result

string = "ab"
offset = 21 #offset should be always < 26 (in order to stay inside the alphabet)
print(caesar_cipher(string, offset))