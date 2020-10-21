#gioi thieu
print('--Moi ban chon ra mot so tu 1 den 100--')
import sys
short = 1 
high = 100
i =0
guess = (short+high)//2
#print('  So ban chon lon hon hay nho hon %d và,%d ',%short, %high) 
#lan1
while(i!= 7):
    print("\n Co phai so ban chon la: ",guess)
    a = input('\n Neu dung nhap 1,sai nhap 0 :')
    a = int(a)
    if(a ==1) :
        print('\n -- CHINH XAC --')
        sys.exit()
    else :
        i=i+1 
        print('Lan: ',i )
        print('\n So ban nhap lon hon hay nho hon')
        b = input('\n Neu lon hon nhap 1,nho hon nhap 0 :')
        b = int(b)
        if(b==0):
            high = guess
        else :
            short = guess
            
        guess = (short+high)//2