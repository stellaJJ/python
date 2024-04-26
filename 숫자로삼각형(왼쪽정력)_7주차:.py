def display_triangle(height):
    for i in range(1, height+1):
        for j in range(1, i+1):
            print(j,end='')
        print()

h=int(input('높이?'))
display_triangle(h) 