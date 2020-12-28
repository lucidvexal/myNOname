def cipher(words,step): 
    code = '' 
    for i in range(len(words)): 
        x = words[i] 
        if x.isupper(): 
            code += chr((ord(x) + s-65)%26+65)
        else:
            code += chr((ord(x) + s-97)%26+65)
    return code 

words=input()
s=int(input())
print(cipher(words,s))
