from xml.sax.xmlreader import InputSource


def kuadrat(objk, pangkat):
    ans=1; A=0
    while A< pangkat :
        ans=ans*objk
        A=A+1
        print("perkalian ke-"+ str(A) + " : " +str(ans))
    print("\nhasil akhir : " +str(ans))
   
num1=int(input("enter first num  : "))
num2=int(input("enter second num : "))
kuadrat(num1,num2)