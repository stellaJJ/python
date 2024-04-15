one_digit=['영','일','이','삼','사','오','육','칠','팔','구']
def read_single_digit(n):
    if 0<=n<=9:
        return one_digit[n]

def read_number(n1):
    if 1<=n1<=9:
        return read_single_digit(n1)
    elif n1<=99:
        return f'{one_digit[n1//10]}{one_digit[n1%10]}'
    elif n1<1000:
        return f'{one_digit[n1//100]}{one_digit[(n1%100)//10]}{one_digit[(n1%100)%10]}'
    else:
        return '세자리 이하의 정수가 아닙니다.'
    
num=int(input('세자리 이하 정수 입력'))
result=read_number(num)

if 0<=num<=9:
    print(f'{read_single_digit(num)}')
elif num<=999:
    print(f'{read_number(num)}')
else:
    print(result)



    