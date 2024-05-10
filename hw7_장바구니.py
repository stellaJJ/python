#9주차 과제
shopping_bag={}
print('[구입]')


while True:
    item=input('상품명?')
    c=input('수량은?')
    
    if item=='':
        break

    print(f'장바구니에 {item}이(가) {c}개가 담겼습니다.')
    shopping_bag[item]=c

print(f'>>>장바구니 보기: {shopping_bag}')

print('[검색]')
g=input('장바구니에서 확인하고자 하는 상품은?')

if g in shopping_bag:
    print(f'{g}은(는) {shopping_bag[g]}개 담겨있습니다.')

else:
    print(f'{g}가 장바구니에 없습니다.')