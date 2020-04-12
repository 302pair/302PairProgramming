def one():
    
    income=int(input('Your Income for the year of assessment '))
    print(income)
    if income/12>30000:
        MPF=1500
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

    if income/12 >30000:
        MPF=18000

    allowance=132000
    chargeable=income-MPF-allowance

    if chargeable<50000:
        total= chargeable* 0.02
        first=total
        if first:
            tax=first
            print('Your final tax total is :')
            print(tax)  
    elif 100000>chargeable>50000:
        total= chargeable-50000  
        second=total*0.06
        chargeable-50000

        if 50000>chargeable>0:
            total= chargeable-50000  
            third=total*0.1
            chargeable-50000
            if 50000>chargeable>0:
                total =chargeable-50000 
                fourth=total*0.14
                chargeable-50000         
                if chargeable>0:
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

    input('Press Enter to continue')
    option = user_option()

print('Finished')