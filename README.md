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
pip install BeautifulSoup
pip install markdown

# CodingTest/make_directory_structure.py 를 실행한다.
# 첫 번째 인자는 본인의 이름
# 두 번째 인자는 식별 가능 주제 어휘 ex) 탐욕 알고리즘 => 탐욕, BFS & DFS => BFS 또는 DFS

python make_directory_structure.py 이동규 탐욕

# 이렇게 하면 'CodingTest/이동규/탐욕' 디렉토리 아래 풀어야 하는 알고리즘 파일과 input 디렉토리 및 파일을 자동으로 생성해준다.
```



## 커리큘럼

### 1. 탐욕 알고리즘(Greedy Algorithm)

[탐욕 알고리즘 강의](https://youtu.be/2zjoKjt97vQ)


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


### 2. 완전 탐색 (DFS & BFS)

[DFS & BFS 강의](https://youtu.be/7C9RgOcvkvo)

| 번호 | 문제                                                        | 난이도   | 순석 | 성훈 | 준현 | 재유 | 아현 | 동규 | 비고 |
| ---- | ----------------------------------------------------------- | -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1    | [boj_1260_DFS와 BFS](https://www.acmicpc.net/problem/1260) | 실버 2   | -    | o  | o    | -    | -    | o  | -    |
| 2    | [boj_1303_전투](https://www.acmicpc.net/problem/1303)      | 실버 1   | -    | o   | o    | -    | -    | o  | -    |
| 3    | [boj_2178_미로 탐색](https://www.acmicpc.net/problem/2178) | 실버 1   | -    | o  | o    | -    | -    | o  | -    |
| 4    | [boj_1743_음식물 피하기](https://www.acmicpc.net/problem/1743) | 실버 1   | -    | o  | o    | -    | -    | o  | -    |
| 5   | [boj_17086_아기 상어2](https://www.acmicpc.net/problem/17086) | 실버 1   | -    | -    | o   | -    | -    | -   | -    |
| 6    | [boj_16953_A to B](https://www.acmicpc.net/problem/16953) | 실버 1   | -    | -    | o   | -    | -    | -   | -    |
| 7    | [boj_12851_숨바꼭질 2](https://www.acmicpc.net/problem/12851) | 골드 5   | -    | -    | -    | -    | -    | -   | -    |
| 8    | [boj_2503_숫자야구](https://www.acmicpc.net/problem/2503)  | 실버 5   | -    | -    | -    | -    | -    | -   | -    |
| 9    | [boj_2231_분해합](https://www.acmicpc.net/problem/2231)    | 브론즈 2 | -    | -    | -    | -    | -    | -   | -    |
| 10   | [boj_14226_이모티콘](https://www.acmicpc.net/problem/14226) | 골드 5   | -    | -    | -    | -    | -    | -   | -    |
| 11    | [boj_2606_바이러스](https://www.acmicpc.net/problem/2606)  | 실버 3   | -    | -    | -    | -    | -    | -   | -    |
| 12   | [boj_10448_유레카 이론](https://www.acmicpc.net/problem/10448) | 브론즈 2 | -    | -    | -    | -    | -    | -   | -    |
| 13   | [boj_3085_사탕 게임](https://www.acmicpc.net/problem/3085) | 실버 4   | -    | -    | -    | -    | -    | -   | -    |
| 14   | [boj_9095_1, 2, 3 더하기](https://www.acmicpc.net/problem/9095) | 실버 3   | -    | -    | -    | -    | -    | -   | -    |
| 15   | [boj_16930_달리기](https://www.acmicpc.net/problem/16930)  | 플레 2   | -    | -    | -    | -    | -    | -   | -    |

### 3. 다이나믹 프로그래밍 (DP)

[다이나믹 프로그래밍 강의](https://youtu.be/5Lu34WIx2Us)