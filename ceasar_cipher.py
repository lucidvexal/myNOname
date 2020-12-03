def cipher(letters,step): 
    code = '' 
    for i in range(len(letters)): 
        x = letters[i] 
        if x.isupper(): 
            code += chr((ord(x) + s-65)%26+65)
        else:
            code += chr((ord(x) + s-97)%26+65)
    return code 

letters=input()
s=int(input())
print(cipher(letters,s))
