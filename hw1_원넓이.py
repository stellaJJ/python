def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(r):
    area = r**2 * 3.14
    return area

result = get_radius('반지름은?')
print(f'원의 넓이는 {result}*{result}*3.14 = {get_circle_area(result)}')