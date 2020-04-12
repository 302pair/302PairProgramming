def calMPF(income):
    if income/12>30000:
        MPF = 18000
        print('Your MPF is: ')
        print(MPF)
    elif 7100<income/12:
        MPF=income*0.05
        print('Your MPF is: ')
        print(MPF)
    else:
        MPF=income*0.05
        print('Your MPF is: ')
        print(MPF)
    return MPF

def taxBracket(chargeable):
    if chargeable<0:
        chargeable=0
        print('No need to pay tax')
    if chargeable<50000:
        total= chargeable* 0.02
        first=total
        chargeable-50000
        if first:
            tax=first
            print('Your final tax total is :')
            print(tax)  
    else:
        total= chargeable-50000  
        total*0.06
        second=total*0.06
        chargeable-50000
        if chargeable>0:
            total= chargeable-50000  
            total*0.1
            third=total*0.1
            chargeable-50000
            if chargeable>0:
                total =chargeable-50000 
                total*0.14
                fourth=total*0.14
                chargeable-50000
                if chargeable>0:
                    total *0.17
                    five =total*0.17
                    if second:
                        tax=1000+second
                        print('Your final tax total is :')
                        print(tax)
                    elif second and third:
                        tax=1000+second+third
                        print('Your final tax total is :')
                        print(tax)
                    elif second and third and fourth:
                        tax=1000+second+third+fourth
                        print('Your final tax total is :')
                        print(tax)
                    elif second and third and fourth and five:
                        tax=1000+second+third+fourth+five
                        print('Your final tax total is :')
                        print(tax)

def one():
    
    income=int(input('Your Income for the year of assessment '))
    print(income)
    MPF = calMPF(income)
    allowance=132000
    chargeable=income-MPF-allowance
    taxBracket(chargeable)

def two():

    Fincome=int(input('Your Income for the year of assessment (first)'))
    print(Fincome)
    MPF1 = calMPF(Fincome)
    Sincome=int(input('Your Income for the year of assessment (second)'))
    print(Sincome)
    MPF2 = calMPF(Sincome)

    Tincome = Fincome + Sincome
    MPF = MPF1 + MPF2

    CombinedAllowance=132000*2
    allowance1=132000
    allowance2=132000

    chargeable=Tincome-MPF-CombinedAllowance
    chargeable1=Fincome-MPF1-allowance1
    chargeable2=Sincome-MPF2-allowance2

    taxBracket(chargeable)
    taxBracket(chargeable1)
    taxBracket(chargeable2)

def clear_screen(line):
    print('\n'*line)

def user_option():
    clear_screen(5)
    print('***What is your Marital status? ***')
    print('[1] Single / Separated / Divorced / Widowed')
    print('[2] Married')

    return(input('Select:'))

option=user_option()
while option !='0':
    if option=='1':
        one()
    if option=='2':
        two()

    input('Press Enter to continue')
    option = user_option()

print('Finished')
