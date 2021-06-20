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

<details>
  <summary><h3>1. 탐욕 알고리즘(Greedy Algorithm) [탐욕 알고리즘 강의](https://youtu.be/2zjoKjt97vQ) [접기/펼치기]</h3></summary>

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
|9|[4796 캠핑](https://www.acmicpc.net/problem/4796)|실버 5|o|o|o|o|-|-|
|10|[1541 잃어버린 괄호](https://www.acmicpc.net/problem/1541)|실버 2|o|-|o|o|-|-|
|11|[12845 모두의 마블](https://www.acmicpc.net/problem/12845)|실버 2|o|-|o|o|-|-|
|12|[1969 DNA](https://www.acmicpc.net/problem/1969)|실버 5|o|-|o|-|-|-|
|13|[11047 동전0](https://www.acmicpc.net/problem/11047)|실버 1|o| -    |-|o|-|-|
|14|[1202 보석 도둑](https://www.acmicpc.net/problem/1202)|골드 2|x|-|-|-|-|-|
|15|[1700 멀티탭 스케줄링](https://www.acmicpc.net/problem/1700)|골드 2|x|-|-|x|-|-|
</details>

<details>
  <summary><h3>2. 완전 탐색 (DFS & BFS)  [DFS & BFS 강의](https://youtu.be/7C9RgOcvkvo) [접기/펼치기]</h3></summary>

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
</details>

<details>
  <summary><h3>3. 모의 SW 역량테스트 A형 대비 & 그리디, 완전 탐색 [접기/펼치기]</h3></summary>

| 번호 | 문제                                                        | 난이도   | 순석 | 성훈 | 준현 | 재유 | 아현 | 동규 | 비고 |
| ---- | ----------------------------------------------------------- | -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1    | [swea_10966_물놀이를 가자](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXWXMZta-PsDFAST&categoryId=AXWXMZta-PsDFAST&categoryType=CODE&problemTitle=10966&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) | 모의 A | o    | -  | o  | -  | o | - | -    |
| 2    | [swea_1953_탈주범검거](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpLlKAQ4DFAUq&categoryId=AV5PpLlKAQ4DFAUq&categoryType=CODE&problemTitle=%EB%AA%A8%EC%9D%98&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=2) | 모의 A | -    | -  | o  | -  | o  | - | -    |
| 3    | [swea_4012_요리사](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH&categoryId=AWIeUtVakTMDFAVH&categoryType=CODE&problemTitle=%EB%AA%A8%EC%9D%98&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) | 모의 A | o   | - | o  | - | o  | - | -    |
| 4    | [swea_4008_숫자만들기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeRZV6kBUDFAVH&categoryId=AWIeRZV6kBUDFAVH&categoryType=CODE&problemTitle=%EB%AA%A8%EC%9D%98&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) | 모의 A | -    | - | o  | -  | o  | - | -    |
| 5   | [swea_5656_벽돌깨기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo&categoryId=AWXRQm6qfL0DFAUo&categoryType=CODE&problemTitle=%EB%AA%A8%EC%9D%98&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) | 모의 A | -    | -  | o | -  | -   | -  | -    |
| 6    | [swea_2117_홈 방범 서비스](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V61LqAf8DFAWu&categoryId=AV5V61LqAf8DFAWu&categoryType=CODE&problemTitle=%EB%AA%A8%EC%9D%98&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=2) | 모의 A | -    | -  | o | -  | -   | -  | -    |
| 7    | [swea_5644_무선충전](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRDL1aeugDFAUo&categoryId=AWXRDL1aeugDFAUo&categoryType=CODE&problemTitle=%EB%AA%A8%EC%9D%98&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) | 모의 A | -    | -   | o | -  | o  | -  | -    |
| 8    | [boj_11047_동전0](https://www.acmicpc.net/problem/11047) | 실버 1  | 풀음 | -  | o | 풀음 | -  | -  | -    |
| 9    | [boj_3085_사탕 게임](https://www.acmicpc.net/problem/3085) | 실버 4 | -    | -  | o | -    | -    | -  | -    |
| 10   | [boj_1202_보석 도둑](https://www.acmicpc.net/problem/1202) | 골드 2 | -    | -    | -  | -    | -    | -   | -    |
| 11    | [boj_1700_멀티탭 스케줄링](https://www.acmicpc.net/problem/1700) | 골드 2 | -    | -    | -  | -  | -  | -   | -    |
| 12   | [boj_10448_유레카 이론](https://www.acmicpc.net/problem/10448) | 브론즈 2 | -    | -    | -    | -    | -    | -  | -    |
| 13   | [boj_1969_DNA](https://www.acmicpc.net/problem/1969) | 실버 5 | -    | -    | -    | -    | -    | -   | -    |
| 14   | [boj_9095_1, 2, 3 더하기](https://www.acmicpc.net/problem/9095) | 실버 3   | -    | -    | o   | -    | 풀음 | -   | -    |
| 15   | [boj_16930_달리기](https://www.acmicpc.net/problem/16930)  | 플레 2   | -    | -    | -    | -    | - | -  | -    |
</details>

<details>
  <summary><h3>4. 다이나믹 프로그래밍 (DP) [다이나믹 프로그래밍 강의](https://youtu.be/5Lu34WIx2Us) [접기/펼치기]</h3></summary>

| 번호 | 문제                                                         | 난이도   | 순석 | 성훈 | 준현 | 아현 | 동규 | 비고 |
| ---- | ------------------------------------------------------------ | -------- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1    | [boj_2748_피보나치 수 2](https://www.acmicpc.net/problem/2748) | 브론즈 1 | o    | o    | o    | o    | o    | -    |
| 2    | [boj_9095_123더하기](https://www.acmicpc.net/problem/9095)   | 실버 3   | o    | o    | o    | o    | o    | -    |
| 3    | [boj_2579_계단오르기](https://www.acmicpc.net/problem/2579)  | 실버 3   | o    | o    | o    | o    | o    | -    |
| 4    | [boj_11726_2xn 타일링](https://www.acmicpc.net/problem/11726) | 실버 3   | o    | o    | o    | o    | o    | -    |
| 5    | [boj_11722_가장 감소 수열](https://www.acmicpc.net/problem/11722) | 실버 2   | o    | o    | o    | o    | o    | -    |
| 6    | [boj_15486_퇴사2](https://www.acmicpc.net/problem/15486)     | 실버 1   | o    | o    | o    | o    | o    | -    |
| 7    | [boj_1520_내리막길](https://www.acmicpc.net/problem/1520)    | 골드 4   | o    | o    | o    | o    | o    | -    |
| 8    | [boj_11066_파일합치기](https://www.acmicpc.net/problem/11066) | 골드 3   | -    | -    | o    | -    | -    | -    |
| 9    | [boj_11049_행렬 곱셈 순서](https://www.acmicpc.net/problem/11049) | 골드 3   | -    | -    | -    | -    | -    | -    |
| 10   | [boj_9252_LCS 2](https://www.acmicpc.net/problem/9252)       | 골드 5   | -    | -    | -    | -    | -    | -    |
| 11   | [boj_1562_계단수](https://www.acmicpc.net/problem/1562)      | 골드 1   | -    | -    | -    | -    | -    | -    |
| 12   | [boj_11570_환상의 듀엣](https://www.acmicpc.net/problem/11570) | 플레 5   | -    | -    | -    | -    | -    | -    |
| 13   | [boj_2618_경찰차](https://www.acmicpc.net/problem/2618)      | 플레 5   | -    | -    | -    | -    | -    | -    |
| 14   | [boj_6989_채점](https://www.acmicpc.net/problem/6989)        | 플레 3   | -    | -    | -    | -    | -    | -    |
| 15   | [boj_2315_가로등 끄기](https://www.acmicpc.net/problem/2315) | 플레 3   | -    | -    | -    | -    | -    | -    |
| 16   | [boj_1126_같은 탑](https://www.acmicpc.net/problem/1126)     | 플레 2   | -    | -    | -    | -    | -    | -    |
| 17   | [boj_1315_RPG](https://www.acmicpc.net/problem/1315)         | 플레 2   | -    | -    | -    | -    | -    | -    |
| 18   | [boj_2419_사수아탕](https://www.acmicpc.net/problem/2419)    | 플레 1   | -    | -    | -    | -    | -    | -    |
| 19   | [boj_12766_지사배정](https://www.acmicpc.net/problem/12766)  | 다이아 5 | -    | -    | -    | -    | -    | -    |
| 20   | [boj_5466_상인](https://www.acmicpc.net/problem/5466)        | 다이아 5 | -    | -    | -    | -    | -    | -    |

</details>

<details>
  <summary><h3>5. 백준 특강 대비 [접기/펼치기]</h3></summary>


| 번호 | 문제                                                        | 난이도   | 순석 | 성훈 | 준현 | 아현 | 동규 | 비고 |
| ---- | ----------------------------------------------------------- | -------- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1    | [boj_13706_제곱근](https://www.acmicpc.net/problem/13706) | 브론즈 1 | o    | o  | o   | o   | o  | -    |
| 2    | [boj_16922_로마 숫자 만들기](https://www.acmicpc.net/problem/16922) | 실버 3 | o    | o   | o   | o    | o   | -    |
| 3    | [boj_17103_골드바흐 파티션](https://www.acmicpc.net/problem/17103) | 실버 2 | o    | o | o   | o   | o   | -    |
| 4    | [boj_12026_BOJ 거리](https://www.acmicpc.net/problem/12026) | 실버 1 | x    | o | o   | o  | o   | -    |
| 5   | [boj_16973_직사각형 탈출](https://www.acmicpc.net/problem/16973) | 골드 5 | o   | x   | o   | x    | x   | -    |
| 6    | [boj_12907_동물원](https://www.acmicpc.net/problem/12907) | 골드 5 | o  | x   | o   | o   | o   | -    |
| 7    | [boj_12904_A와 B](https://www.acmicpc.net/problem/12904) | 골드 5 | o    | o  | o   | -    | o   | -    |
| 8    | [boj_10422_괄호](https://www.acmicpc.net/problem/10422) | 골드 4 | x | o | o | - | o | -    |
| 9    | [boj_1242_소풍](https://www.acmicpc.net/problem/1242) | 골드 2 | o    | x | o | -    | -  | -    |
| 10   | [boj_11025_요세푸스 문제 3](https://www.acmicpc.net/problem/11025) | 골드 2 | x    | -    | o | o    |  -   | -    |
| 11    | [boj_16959_체스판 여행 1](https://www.acmicpc.net/problem/16959) | 골드 1 | x    | -    | o | -  | -  | -    |
| 12   | [boj_17071_숨바꼭질 5](https://www.acmicpc.net/problem/17071) | 골드 1 | -    | -    | o   | -    | -  | -    |
| 13   | [boj_12967_pqr](https://www.acmicpc.net/problem/12967) | 플레 5 | -    | -    | -    | -    | -   | -    |
</details>

#### 문제별 핵심 개념
- 제곱근 : 이분탐색
- 골드바흐 파티션 : 소수 만들기(에라토스테네스의 체)
- 소풍 : 원형큐
- 요세푸스 문제 3 : [요세푸스 문제(위키)](https://ko.wikipedia.org/wiki/%EC%9A%94%EC%84%B8%ED%91%B8%EC%8A%A4_%EB%AC%B8%EC%A0%9C), [요세푸스 문제(꺼무위키)](https://namu.wiki/w/%EC%9A%94%EC%84%B8%ED%91%B8%EC%8A%A4%20%EB%AC%B8%EC%A0%9C)

</details>

<details>
  <summary><h3>6. 카카오 기출 문제 풀이 [접기/펼치기]</h3></summary>

| 번호 | 문제 | 순석 | 성훈 | 준현 | 아현 | 동규 | 비고 |
| ---- | ----------------------------------------------------------- | -------- | ---- | ---- | ---- | ---- | ---- |
| 1    | [pro_신규 아이디 추천](https://programmers.co.kr/learn/courses/30/lessons/72410) |  o  |      | o |  o   |      | -    |
| 2    | [pro_메뉴 리뉴얼](https://programmers.co.kr/learn/courses/30/lessons/72411) |  o   |      | o |      |      | -    |
| 3    | [pro_순위 검색](https://programmers.co.kr/learn/courses/30/lessons/72412) |      |      | x |    o |      | -    |
| 4    | [pro_문자열 압축](https://programmers.co.kr/learn/courses/30/lessons/60057) |      | o | o |   o   |      | -    |
| 5   | [pro_괄호 변환](https://programmers.co.kr/learn/courses/30/lessons/60058) |       |      | o |   o  |      | -    |
| 6    | [pro_자물쇠와 열쇠](https://programmers.co.kr/learn/courses/30/lessons/60059) |      |      |      |      |      | -    |
| 7    | [boj_3687_성냥개비](https://www.acmicpc.net/problem/3687) |  x   |      | o |      |      | -    |
</details>

<details>
  <summary><h3>7. 탐욕 알고리즘(Greedy Algorithm) 2번째 [접기/펼치기]</h3></summary>

| 번호 | 문제 | 난이도 | 순석 | 성훈 | 준현 | 아현 | 동규 | 재유 | 비고 |
| ---- | ----------------------------------------------------------- | -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1    | [boj_5585_거스름돈](https://www.acmicpc.net/problem/5585) | 브론즈 2 |  o  | o | o | o | o | o | -    |
| 2    | [boj_1459_걷기](https://www.acmicpc.net/problem/1459) | 브론즈 1 |  o   | x | o | o | o | x | -    |
| 3    | [boj_1543_문서 검색](https://www.acmicpc.net/problem/1543) | 실버 4 |  o   | o | o | o | o | o | -    |
| 4    | [boj_2012_등수 매기기](https://www.acmicpc.net/problem/2012) | 실버 3 | o    | o | o | o | o | o | -    |
| 5   | [boj_1911_흙길 보수하기](https://www.acmicpc.net/problem/1911) | 실버 2 | o    | x | o |o| o | o | -    |
| 6    | [boj_2036_수열의 점수](https://www.acmicpc.net/problem/2036) | 실버 1 |   o  | o | o | o | o | o | -    |
| 7    | [boj_2141_우체국](https://www.acmicpc.net/problem/2141) | 골드 4 |  o   | o | o | o | o | o | -    |
| 8    | [boj_10800_컬러볼](https://www.acmicpc.net/problem/10800) | 골드 3 |  x   |      | o |o | x | x | -    |
| 9    | [boj_1202_보석 도둑](https://www.acmicpc.net/problem/1202) | 골드 2 |      |      | o |  |      | x | -    |
| 10    | [boj_1114_통나무 자르기](https://www.acmicpc.net/problem/1114) | 골드 1 |      |      |      |  |      |      | -    |
</details>

<details>
  <summary><h3>8. 완전 탐색 (DFS & BFS) 2번째 [접기/펼치기]</h3></summary>

| 번호 | 문제                                                        | 난이도   | 순석 | 성훈 | 준현 | 재유 | 아현 | 동규 | 비고 |
| ---- | ----------------------------------------------------------- | -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1    | [boj_11724_연결 요소의 개수](https://www.acmicpc.net/problem/11724) | 실버 2   | o  | o | o | o |  o | o | -    |
| 2    | [boj_2667_단지번호붙이기](https://www.acmicpc.net/problem/2667) | 실버 1   |  o | o | o | o | o  | o | -    |
| 3    | [boj_6603_로또](https://www.acmicpc.net/problem/6603) | 실버 2  |  o | o | o | o |  o | o | -    |
| 4    | [boj_7562_나이트의 이동](https://www.acmicpc.net/problem/7562) | 실버 2  | o  | o | o | o | o   | o | -    |
| 5   | [boj_2206_벽 부수고 이동하기](https://www.acmicpc.net/problem/2206) | 골드 4 |  o | o | o | x | x   | o | -    |
| 6    | [boj_2468_안전 영역](https://www.acmicpc.net/problem/2468) | 실버 1 | o  | o | o | o | o   | o | -    |
| 7    | [boj_7569_토마토](https://www.acmicpc.net/problem/7569) | 실버 1 | o  | o | o | o |  x | o | -    |
| 8    | [boj_2644_촌수계산](https://www.acmicpc.net/problem/2644) | 실버 2  | o  | o | o | o |  o  | o | -    |
| 9    | [boj_3055_탈출](https://www.acmicpc.net/problem/3055) | 골드 5 | o  | o | o | o |  o   | o | -    |
| 10   | [boj_9019_DSLR](https://www.acmicpc.net/problem/9019) | 골드 5   |  o  | x | o | o |   o  | o | -    |

</details>

<details>
  <summary><h3>9. 다이나믹 프로그래밍 (DP) 2번째 [접기/펼치기] </h3></summary>

| 번호 | 문제                                                        | 난이도   | 순석 | 성훈 | 준현 | 재유 | 아현 | 동규 | 비고 |
| ---- | ----------------------------------------------------------- | -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1    | [boj_14720_우유 축제](https://www.acmicpc.net/problem/14620) | 브론즈 3 |64 | 68 | 68 | 68 |  72 | 64 | -    |
| 2    | [boj_10835_카드게임](https://www.acmicpc.net/problem/10835) | 실버 1   |3044 | 3328 | 2508 | 2932 | 3124  | 3324 | -    |
| 3    | [boj_2156_포도주 시식](https://www.acmicpc.net/problem/2156) | 실버 1  |72 | 540 | 596 | 536 |  524 | 564 | -    |
| 4    | [boj_14722_우유 도시](https://www.acmicpc.net/problem/14722) | 골드 5 |  2980 | x | 2180 | 984 |  1916  | x | -    |
| 5   | [boj_13302_리조트](https://www.acmicpc.net/problem/13302) | 골드 5 | 68  | x | 72 | x | 108  | x | -    |

</details>

<details>
  <summary><h3>10. 그리디 알고리즘 3번째 [접기/펼치기] </h3></summary>

| 번호 | 문제                                                        | 순석 | 성훈 | 준현 | 재유 | 아현 | 동규 | 비고 |
| ---- | ----------------------------------------------------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1    | [체육복](https://programmers.co.kr/learn/courses/30/lessons/42862) |o | o | o    | o |  o   | o | -    |
| 2    | [조이스틱](https://programmers.co.kr/learn/courses/30/lessons/42860) |  x    | x | o    | o |  o   | x | -    |
| 3    | [큰 수 만들기](https://programmers.co.kr/learn/courses/30/lessons/42883) |  o    | o | o    | o |  o   | o | -    |
| 4    | [구명보트](https://programmers.co.kr/learn/courses/30/lessons/42885) |  o    | o | o    | o |  o   | o | -    |
| 5   | [섬 연결하기](https://programmers.co.kr/learn/courses/30/lessons/42861) | o     | o | o    | o |  o   | o | -    |
| 6 | [단속카메라](https://programmers.co.kr/learn/courses/30/lessons/42884) | o | o | o | o |o | o |  |
</details>
<details>
  <summary><h3>11. 완전 탐색 (DFS & BFS) 3번째 [접기/펼치기]</h3></summary>

| 번호 | 문제                                                        | 난이도   | 순석 | 성훈 | 준현 | 재유 | 아현 | 동규 | 비고 |
| ---- | ----------------------------------------------------------- | -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1    | [boj_2573_빙산](https://www.acmicpc.net/problem/2573) | 골드 4 |  1036(pypy)    | x | 2903 | 1184(pypy) |      | 724(pypy) | -    |
| 2    | [boj_14503_로봇 청소기](https://www.acmicpc.net/problem/14503) | 골드 5 |   72   | 92 | 68 | 96 |      | 72 | -    |
| 3    | [boj_9205_맥주 마시면서 걸어가기](https://www.acmicpc.net/problem/9205) | 실버 1 | 116     | x | 112 | x |      | 196 | -    |
| 4    | [boj_10451_순열 사이클](https://www.acmicpc.net/problem/10451) | 실버 1 |   368   | 456 | 672  | 2252 |      | 808 | -    |
| 5   | [boj_11559_Puyo Puyo](https://www.acmicpc.net/problem/11559) | 골드 5 |  100    | x | 88 | 68 |      | 92 | -    |
| 6    | [boj_2234_성곽](https://www.acmicpc.net/problem/2234) | 골드 4 |  104    | x | 100 | 88 |      |      | -    |
| 7    | [boj_1389_케빈 베이컨의 6단계 법칙](https://www.acmicpc.net/problem/1389) | 실버 1 |   96   | 100 | 88 | 112 |      |      | -    |
| 8    | [boj_2583_영역 구하기](https://www.acmicpc.net/problem/2583) | 실버 1 |   80   | 104 | 116 | 96 |      |      | -    |
| 9   | [boj_16928_뱀과 사다리 게임](https://www.acmicpc.net/problem/16928) | 실버 1 | 104     | 59 | 100 | 92 |      |      | -    |
| 10  | [boj_16948_데스 나이트](https://www.acmicpc.net/problem/16948) | 실버 1 |120   | 116 | 120 | 140 |      |      | -    |
| 11  | [boj_14502_연구소](https://www.acmicpc.net/problem/14502) | 골드 5 |   x  | 5024 | 4304 | x |      |      | -    |
| 12  | [boj_12886_돌 그룹](https://www.acmicpc.net/problem/12886) | 골드 5 |  640   | x | 948(pypy) | x |      |      | -    |
</details>

<details>
  <summary><h3>12. 프로그래머스 실전 연습 lv1, lv2 [접기/펼치기]</h3></summary>

> IDE 도움 받지 않고 풀어보기

| 번호 | 문제                                                         | 난이도 | 순석 | 성훈 | 준현 | 재유 | 아현 | 동규 | 비고 |
| ---- | ------------------------------------------------------------ | ------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1    | [로또의 최고 순위와 최저 순위](https://programmers.co.kr/learn/courses/30/lessons/77484) | Lv. 1  |  o    | o    | o    | o    |    o  |      | -    |
| 2    | [음양 더하기](https://programmers.co.kr/learn/courses/30/lessons/76501) | Lv. 1  |    o  | o    | o    | o    |   o   |      | -    |
| 3    | [신규 아이디 추천](https://programmers.co.kr/learn/courses/30/lessons/72410) | Lv. 1  | o     | o    | o    | o |   o   |      | -    |
| 4    | [키패드 누르기](https://programmers.co.kr/learn/courses/30/lessons/67256) | Lv. 1  |   o   | o    | o    | o |  o    |      | -    |
| 5    | [내적](https://programmers.co.kr/learn/courses/30/lessons/70128) | Lv. 1  |   o   | o    | o    | o    |    o  |      | -    |
| 6    | [멀쩡한 사각형](https://programmers.co.kr/learn/courses/30/lessons/62048) | Lv. 2  |  o    | o    | o    | x |   o   |      | -    |
| 7    | [오픈채팅방](https://programmers.co.kr/learn/courses/30/lessons/42888) | Lv. 2  |      | o | o    | o    |   o   |      | -    |
| 8    | [124 나라의 숫자](https://programmers.co.kr/learn/courses/30/lessons/12899) | Lv. 2  |      | o    | o    | o    |    o  |      | -    |
| 9    | [전화번호 목록](https://programmers.co.kr/learn/courses/30/lessons/42577) | Lv. 2  |      | o | o    | o    |    o  |      | -    |
| 10   | [행렬 테두리 회전하기](https://programmers.co.kr/learn/courses/30/lessons/77485) | Lv. 2 |      | x | o    | o    |    o  |      | -    |
</details>

### 13. 프로그래머스 실전 연습 lv2 2번째 [접기/펼치기]

> IDE 도움 받지 않고 풀어보기

| 번호 | 문제                                                         | 난이도 | 순석 | 성훈 | 준현 | 재유 | 아현 | 동규 | 비고 |
| ---- | ------------------------------------------------------------ | ------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1    | [더 맵게](https://programmers.co.kr/learn/courses/30/lessons/42626) | Lv. 2 |   o   | o | o | o |   o   |      | -    |
| 2    | [짝지어 제거하기](https://programmers.co.kr/learn/courses/30/lessons/12973) | Lv. 2 |  o   | o | o | o |   o  |      | -    |
| 3    | [게임 맵 최단거리](https://programmers.co.kr/learn/courses/30/lessons/1844) | Lv. 2  |  o   | o | o | o |  o   |      | -    |
| 4    | [[1차] 뉴스 클러스터링](https://programmers.co.kr/learn/courses/30/lessons/17677) | Lv. 2  |  o   | o | o | o |  o   |      | -    |
| 5    | [예상 대진표](https://programmers.co.kr/learn/courses/30/lessons/12985) | Lv. 2  |  x   | o | o | o |  o   |      | -    |
| 6    | [튜플](https://programmers.co.kr/learn/courses/30/lessons/64065) | Lv. 2  |  o   | o | o | o |      |      | -    |
| 7    | [순위검색](https://programmers.co.kr/learn/courses/30/lessons/72412) | Lv. 2  | x    | x | o | o |    o  |      | -    |
| 8    | [위장](https://programmers.co.kr/learn/courses/30/lessons/42578) | Lv. 2  |      | o | o | o |    o  |      | -    |
| 9    | [스킬트리](https://programmers.co.kr/learn/courses/30/lessons/49993) | Lv. 2  |      | o | o | o |  o    |      | -    |
| 10   | [수식 최대화](https://programmers.co.kr/learn/courses/30/lessons/67257) | Lv. 2  |      | x | o | o |      |      | -    |

Brute Force => N과 M 1~8, NM과 K 1

https://programmers.co.kr/skill_checks
