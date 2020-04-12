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

def taxBracket(chargeable,print5print):
    if chargeable<0:
        chargeable=0
        tax=0
        if print5print ==True:
            print('No need to pay tax')
        return tax
    else:
        if chargeable > 200000:
            progresstax = 1000+3000+5000+7000+((chargeable-200000)*0.17)
            standardtax= chargeable*0.1525
            
            if print5print ==True:
                print('Your final tax total is :')
                if (min(progresstax, standardtax)==progresstax):
                    text = 'progresstax'
                elif (min(progresstax,standardtax)==standardtax):
                    text = 'standardtax'
                print(text,min(progresstax,standardtax))
            return(min(progresstax,standardtax))
            
        elif chargeable > 150000:
            tax = 1000+3000+5000+((chargeable-150000)*0.14)
            if print5print ==True:
                print('Your final tax total is :')
                print(tax)
            return tax
        elif chargeable > 100000:
            tax = 1000+3000+((chargeable-100000)*0.10)
            if print5print ==True:
                print('Your final tax total is :')
                print(tax)
            return tax
        elif chargeable > 50000:
            tax = 1000+((chargeable-50000)*0.06)
            if print5print ==True:
                print('Your final tax total is :')
                print(tax)
            return tax    
        else:
            tax = chargeable * 0.02
            if print5print ==True:
                print('Your final tax total is :')
                print(tax)
            return tax
        
def one():
        income=int(input('Your Income for the year of assessment '))
        if income>0:
            MPF = calMPF(income)
            allowance=132000
            chargeable=income-MPF-allowance
            taxBracket(chargeable,True)
        elif income<0:
            print('Please enter value greater than or equal to zero')

def two():

    Fincome=int(input('Your Income for the year of assessment (first)'))
    Sincome=int(input('Your Income for the year of assessment (second)'))
    if Fincome < 0 or Sincome < 0:
        print('Please enter value greater than or equal to zero')
    elif Fincome >= 0 and  Sincome >= 0:
        MPF1 = calMPF(Fincome)
        MPF2 = calMPF(Sincome)
        Tincome = Fincome + Sincome
        MPF = MPF1 + MPF2

        CombinedAllowance=132000*2
        allowance1=132000
        allowance2=132000

        chargeable=Tincome-MPF-CombinedAllowance
        chargeable1=Fincome-MPF1-allowance1
        chargeable2=Sincome-MPF2-allowance2

        c0 = taxBracket(chargeable,False)
        c1 = taxBracket(chargeable1,False)
        c2 = taxBracket(chargeable2,False)
        
        if c0>(c1+c2):
            print("This is your tax (Using separate)")
            print(c1+c2)
        elif c0<(c1+c2):
            print("This is your tax (Using joint)")
            print(c0)
        elif c0==(c1+c2):
            print("This is your tax")
            print(c0)

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