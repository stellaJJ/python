scores=[]
def input_scores():
    for i in range(6):
        s=int(input(f'#{i+1}?'))
        
        if s<0:
            break
        scores.append(s)
    return s
       
    
def get_average(s):
    total=0
    for j in s:
        total+=s
    return total/len(scores)

def show_scores(s):
    print(f'{scores}')

print('[점수입력]')
show_scores(scores)
sc=input_scores()
print('[점수출력]')
print(f'개인점수:{scores}')
print(f'평균:{get_average(sc)}')

import os

filename = 'score.bin'
filepath = '/Users/jang-yunha/Desktop/pywork' + filename


def save_data(score, filepath):
    with open(filepath, 'w', encoding = 'utf8') as file :
        for item in score :
            file.write(f'{item}\n')

def load_data(filepath) :
    lines = []
    with open(filepath, 'r', encoding = 'utf8') as file :
        for line in file :
            lines.append(line.strip('\n'))
    return lines

if os.path.exists(filename) :
    print('[파일 읽기]')
    scores = load_data(filename)
    show_scores(scores)
else :
    scores = []


