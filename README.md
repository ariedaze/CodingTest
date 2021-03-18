# CodingTest

## 코테 운영 방식
1. 주마다 하나의 주제를 정합니다. ex) 탐욕 알고리즘, 완전 탐색
2. 그 주제와 관련된 이론 공부를 독학합니다. 방식은 자유이나 문제 풀기 전에 꼭 한 번 훑어보기로 합시다.
(youtube 강의 참고)
3. 그 주제와 관련된 문제를 1주일에 10개 풉니다.
4. 관련 문제는 깃헙을 통해 서로 공유합니다.
5. 1주일 중 하루는 저번 주 한거 서로 리뷰, 하루는 중간점검 시간을 가짐 (월, 목)
6. 파일 이름과 커밋 메시지도 컨벤션에 맞춰서 올릴 것.


### 파일 이름

백준 : `boj_(문제번호)_(문제이름)` 

SW Expert Academy : `swea_(문제번호)_(문제이름)`

프로그래머스 : `프로그래머스_(문제이름)`


### 커밋 메시지

모든 소스파일을 작성 후 commit 을 할때는 자신의 이름과 문제를 푼 번호, 못 푼 번호를 같이 올려주어야한다.

`commit -m '준현 -S: boj_1590, boj_1349, -F: swea_1345'` : -S 뒤에는 푼 문제, -F 뒤에는 못 푼 문제(코드 리뷰를 하기 위한것)

### 파일 구조 자동생성

README.md 에 주어진 주제 명(h3로 쓰여진)과 테이블로 파일 구조를 자동생성합니다.

```
# 다음 두 모듈을 import 한다
# BeautifulSoup4는 pip install --upgrade pip 가 필요할 수 있다.
pip install BeautifulSoup4
pip install markdown

# CodingTest/make_directory_structure.py 를 실행한다.
# 첫 번째 인자는 본인의 이름
# 두 번째 인자는 식별 가능 주제 어휘 ex) 탐욕 알고리즘 => 탐욕, BFS & DFS => BFS 또는 DFS

python make_directory_structure.py 이동규 탐욕

# 이렇게 하면 'CodingTest/이동규/탐욕' 디렉토리 아래 풀어야 하는 알고리즘 파일과 input 디렉토리 및 파일을 자동으로 생성해준다.
```



## 커리큘럼

### 1. 탐욕 알고리즘(Greedy Algorithm) [탐욕 알고리즘 강의](https://youtu.be/2zjoKjt97vQ)


|번호|문제|난이도|순석|성훈|준현|재유|아현|비고|
|---|---|---|---|---|---|---|---|---|
|1|[2875 대회 Or 인턴](https://www.acmicpc.net/problem/2875)|브론즈 3|o|o|o|o|o|-|
|2|[10610 30](https://www.acmicpc.net/problem/10610)|실버 5|o|o|o|o|o|-|
|3|[1783 병든 나이트](https://www.acmicpc.net/problem/1783)|실버 5|o|o|o|o|o|-|
|4|[1931 회의실 배정](https://www.acmicpc.net/problem/1931)|실버 2|o|o|o|o|o|-|
|5|[11399 ATM](https://www.acmicpc.net/problem/11399)|실버 3|o|o|o|o|o|-|
|6|[2217 로프](https://www.acmicpc.net/problem/2217)|실버 4|o|o|o|o|o|-|
|7|[13458 시험감독](https://www.acmicpc.net/problem/13458)|브론즈 2|o|o|o|o|o|-|
|8|[1946 신입 사원](https://www.acmicpc.net/problem/1946)|실버 1|o|o|o|x|o|-|
|9|[4796 캠핑](https://www.acmicpc.net/problem/4796)|실버 5|o|-|o|o|-|-|
|10|[1541 잃어버린 괄호](https://www.acmicpc.net/problem/1541)|실버 2|o|-|o|o|-|-|
|11|[12845 모두의 마블](https://www.acmicpc.net/problem/12845)|실버 2|o|-|o|o|-|-|
|12|[1969 DNA](https://www.acmicpc.net/problem/1969)|실버 5|o|-|o|-|-|-|
|13|[11047 동전0](https://www.acmicpc.net/problem/11047)|실버 1|o| -    |-|o|-|-|
|14|[1202 보석 도둑](https://www.acmicpc.net/problem/1202)|골드 2|x|-|-|-|-|-|
|15|[1700 멀티탭 스케줄링](https://www.acmicpc.net/problem/1700)|골드 2|x|-|-|x|-|-|


### 2. 완전 탐색 (DFS & BFS)  [DFS & BFS 강의](https://youtu.be/7C9RgOcvkvo)

| 번호 | 문제                                                        | 난이도   | 순석 | 성훈 | 준현 | 재유 | 아현 | 동규 | 비고 |
| ---- | ----------------------------------------------------------- | -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1    | [boj_1260_DFS와 BFS](https://www.acmicpc.net/problem/1260) | 실버 2   | o   | o  | o    | o   | o   | o  | -    |
| 2    | [boj_1303_전투](https://www.acmicpc.net/problem/1303)      | 실버 1   | o   | o   | o    | o   | o   | o  | -    |
| 3    | [boj_2178_미로 탐색](https://www.acmicpc.net/problem/2178) | 실버 1   | o   | o  | o    | o  | o   | o  | -    |
| 4    | [boj_1743_음식물 피하기](https://www.acmicpc.net/problem/1743) | 실버 1   | o   | o  | o    | x   | o   | o  | -    |
| 5   | [boj_17086_아기 상어2](https://www.acmicpc.net/problem/17086) | 실버 1   | o   | o   | o   | o   | -   | o   | -    |
| 6    | [boj_16953_A to B](https://www.acmicpc.net/problem/16953) | 실버 1   | o   | o  | o   | o   | -    | o   | -    |
| 7    | [boj_12851_숨바꼭질 2](https://www.acmicpc.net/problem/12851) | 골드 5   | o   | x   | o   | o  | o   | o   | -    |
| 8    | [boj_2503_숫자야구](https://www.acmicpc.net/problem/2503)  | 실버 5   | o   | o  | o   | -    | o   | x   | -    |
| 9    | [boj_2231_분해합](https://www.acmicpc.net/problem/2231)    | 브론즈 2 | o   | o   | o   | o   | -    | o   | -    |
| 10   | [boj_14226_이모티콘](https://www.acmicpc.net/problem/14226) | 골드 5   | -    | x  | o   | x    | x    | -   | -    |
| 11    | [boj_2606_바이러스](https://www.acmicpc.net/problem/2606)  | 실버 3   | o   | o   | o   | o   | o   | -   | -    |
| 12   | [boj_10448_유레카 이론](https://www.acmicpc.net/problem/10448) | 브론즈 2 | -    | -    | -    | -    | -    | x   | -    |
| 13   | [boj_3085_사탕 게임](https://www.acmicpc.net/problem/3085) | 실버 4   | -    | -    | -    | -    | o    | -   | -    |
| 14   | [boj_9095_1, 2, 3 더하기](https://www.acmicpc.net/problem/9095) | 실버 3   | -    | -    | -    | -    | o    | -   | -    |
| 15   | [boj_16930_달리기](https://www.acmicpc.net/problem/16930)  | 플레 2   | -    | -    | -    | -    | x  | -  | -    |

### 3. 모의 SW 역량테스트 A형 대비 & 그리디, 완전 탐색

| 번호 | 문제                                                        | 난이도   | 순석 | 성훈 | 준현 | 재유 | 아현 | 동규 | 비고 |
| ---- | ----------------------------------------------------------- | -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1    | [swea_10966_물놀이를 가자](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXWXMZta-PsDFAST&categoryId=AXWXMZta-PsDFAST&categoryType=CODE&problemTitle=10966&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) | 모의 A | o    | -  | o  | -  | o | - | -    |
| 2    | [swea_1953_탈주범검거](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpLlKAQ4DFAUq&categoryId=AV5PpLlKAQ4DFAUq&categoryType=CODE&problemTitle=%EB%AA%A8%EC%9D%98&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=2) | 모의 A | -    | -  | o  | -  | o  | - | -    |
| 3    | [swea_4012_요리사](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH&categoryId=AWIeUtVakTMDFAVH&categoryType=CODE&problemTitle=%EB%AA%A8%EC%9D%98&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) | 모의 A | -    | - | o  | - | o  | - | -    |
| 4    | [swea_4008_숫자만들기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeRZV6kBUDFAVH&categoryId=AWIeRZV6kBUDFAVH&categoryType=CODE&problemTitle=%EB%AA%A8%EC%9D%98&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) | 모의 A | -    | - | o  | -  | o  | - | -    |
| 5   | [swea_5656_벽돌깨기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo&categoryId=AWXRQm6qfL0DFAUo&categoryType=CODE&problemTitle=%EB%AA%A8%EC%9D%98&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) | 모의 A | -    | -  | -  | -  | -   | -  | -    |
| 6    | [swea_2117_홈 방범 서비스](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V61LqAf8DFAWu&categoryId=AV5V61LqAf8DFAWu&categoryType=CODE&problemTitle=%EB%AA%A8%EC%9D%98&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=2) | 모의 A | -    | -  | -  | -  | -   | -  | -    |
| 7    | [swea_5644_무선충전](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRDL1aeugDFAUo&categoryId=AWXRDL1aeugDFAUo&categoryType=CODE&problemTitle=%EB%AA%A8%EC%9D%98&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) | 모의 A | -    | -   | -  | -  | o  | -  | -    |
| 8    | [boj_11047_동전0](https://www.acmicpc.net/problem/11047) | 실버 1  | 풀음 | -  | -  | 풀음 | -  | -  | -    |
| 9    | [boj_3085_사탕 게임](https://www.acmicpc.net/problem/3085) | 실버 4 | -    | -  | -  | -    | -    | -  | -    |
| 10   | [boj_1202_보석 도둑](https://www.acmicpc.net/problem/1202) | 골드 2 | -    | -    | -  | -    | -    | -   | -    |
| 11    | [boj_1700_멀티탭 스케줄링](https://www.acmicpc.net/problem/1700) | 골드 2 | -    | -    | -  | -  | -  | -   | -    |
| 12   | [boj_10448_유레카 이론](https://www.acmicpc.net/problem/10448) | 브론즈 2 | -    | -    | -    | -    | -    | -  | -    |
| 13   | [boj_1969_DNA](https://www.acmicpc.net/problem/1969) | 실버 5 | -    | -    | -    | -    | -    | -   | -    |
| 14   | [boj_9095_1, 2, 3 더하기](https://www.acmicpc.net/problem/9095) | 실버 3   | -    | -    | -    | -    | 풀음 | -   | -    |
| 15   | [boj_16930_달리기](https://www.acmicpc.net/problem/16930)  | 플레 2   | -    | -    | -    | -    | - | -  | -    |

### 4. 다이나믹 프로그래밍 (DP) [다이나믹 프로그래밍 강의](https://youtu.be/5Lu34WIx2Us)
