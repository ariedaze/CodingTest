import markdown
import re
import os
from bs4 import BeautifulSoup
import sys

file_path_1 = sys.argv[1] # 파일 경로 => 알고리즘 조원 이름
file_path_2 = sys.argv[2] # 알고리즘 카테고리로 폴더를 만들것임 => DFS

if len(sys.argv) != 3:
    print("python make_directory_structure 본인_이름 알고리즘_카테고리 \r 양식으로 입력해주세요")
    sys.exit()

with open('./README.md', 'r', encoding='UTF8') as f:
    text = f.read()
    html = markdown.markdown(text)

soup = BeautifulSoup(html, "html.parser")
items = soup.find('h3', text=re.compile(file_path_2)).find_next_siblings()[1].find_all('a')

os.mkdir('./{}/{}'.format(file_path_1, file_path_2))
os.mkdir('./{}/{}/input'.format(file_path_1, file_path_2))

for item in items:
    algo_title = item.get_text()
    print(algo_title)
    algo_f = open('./{}/{}/{}.py'.format(file_path_1, file_path_2, algo_title), 'w', encoding='UTF8')

    algo_f.write('import sys\n')
    algo_f.write("sys.stdin = open('input/{}.txt', 'r')".format(algo_title))

    input_f = open('./{}/{}/input/{}.txt'.format(file_path_1, file_path_2, algo_title), 'w')