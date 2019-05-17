from stack import Stack

def cetakHexa():
    a = int(input("Masukkan bilangan desimal = " ))
    hexa = Stack()
    hexlist = "0123456789ABCDEF"
    while a!=0:
        sisa = a%16
        a = a//16
        hexa.push(hexlist[sisa])
    hasil=""
    for i in range(len(hexa)):
        hasil = hasil+str(hexa.pop())
    return hasil

print(cetakHexa())
