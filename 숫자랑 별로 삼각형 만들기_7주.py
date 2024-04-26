def display_triangle(height,ch='*'):
    for i in range(1, height+1):
        draw_line(' ', height-i)
        draw_line(ch, i)
        print()

def draw_line(ch, n):
    print(ch*n,end='')
#   for i in range(1, n+1):
#        print('*', end='')

h=int(input('높이?'))
display_triangle(h)