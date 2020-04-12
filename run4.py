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

def taxBracket(allowance,MPF,income,print5print):
    chargeable = income-MPF-allowance
    if chargeable<0:
        chargeable=0
        tax=0
        if print5print ==True:
            print('No need to pay tax')
        return tax
    else:
        if chargeable > 200000:
            progresstax = 1000+3000+5000+7000+((chargeable-200000)*0.17)
            standardtax= (chargeable+allowance)*0.15
            Text = ''
            if min(progresstax,standardtax) == standardtax:
                Text = 'Using Standard rate tax is better'
            else:
                Text = 'Using Progress rate tax is better'
            if print5print ==True:
                print(Text + ' Your tax is: ')
                print(min(progresstax,standardtax))
            return(min(progresstax,standardtax))
            
        elif chargeable > 150000:
            tax = 1000+3000+5000+((chargeable-150000)*0.14)
            if print5print ==True:
                print(' Your tax calculated by progess rate is: ')
                print(tax)
            return tax
        elif chargeable > 100000:
            tax = 1000+3000+((chargeable-100000)*0.10)
            if print5print ==True:
                print(' Your tax calculated by progess rate is: ')
                print(tax)
            return tax
        elif chargeable > 50000:
            tax = 1000+((chargeable-50000)*0.06)
            if print5print ==True:
                print(' Your tax calculated by progess rate is: ')
                print(tax)
            return tax    
        else:
            tax = chargeable * 0.02
            if print5print ==True:
                print(' Your tax calculated by progess rate is: ')
                print(tax)
            return tax
        
def one():
        income=int(input('Your Income for the year of assessment '))
        MPF = calMPF(income)
        if income>0:
            allowance=132000
            taxBracket(allowance,MPF,income,True)
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

        c0 = taxBracket(CombinedAllowance,MPF,Tincome,False)
        c1 = taxBracket(allowance1,MPF1,Fincome,False)
        c2 = taxBracket(allowance2,MPF2,Sincome,False)
        print("This is your tax (Joint Tax)")
        print(c0)
        print("This is your tax (Seperate Tax)")
        print(c1+c2)
        
        if c0>(c1+c2):
            print("Pay seperate Tax is cheaper")
        elif c0<(c1+c2):
            print("Pay joint Tax is cheaper")
        elif c0==(c1+c2):
            print("Seperate Tax and Joint Tax is same amount")

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