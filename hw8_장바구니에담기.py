shopping_bag={}
def buy(g):
        print('[구입]')
        item=input('상품명?')
        if item=='':
            return False
        
        cnt=int(input('수량은?'))
        print(f'장바구니에 {item}이(가) {cnt}개 담겼습니다.')

        shopping_bag[item]=cnt
        return True
    
def show(p):
    print(f'{shopping_bag}')

def find(p):
    print('[검색]')
    g=input('장바구니에서 확인하고자 하는 상품은?')
    if g in shopping_bag:
        print(f'{g}은(는) {shopping_bag[g]}개 담겨있습니다.')
    else:
         print(f'{g}은(는) 장바구니에 없습니다.')

b=buy(shopping_bag)

while True:
    if buy(shopping_bag)==False:
        break
      
    print(f'>>>장바구니 보기: {shopping_bag}')
      
show(shopping_bag)
find(shopping_bag)