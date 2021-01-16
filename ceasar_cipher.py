def ceaser(chau,mau):
    val=0
    new=[]
    for i in a:
        val=ord(i)
        chau=val+mau
        new.append(chr(chau))
    return(''.join(new))

a=[str(i) for i in input("enter the character : ")]
b=int(input("enter the shift : "))
print("the cipher is : ",ceaser(a,b))
