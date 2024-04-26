
def input_age(prompt):
    while True:
        n=int(input(prompt))    
        if 0<=n<=120:
            return n
        
def is_adult(age):
    if age>19:
        return True
        
    else:
        return False

age=input_age('나이는?')
if is_adult(age):
    print('당신은성인입니다')

else: 
    print('당신은 성인이 아닙니다')
