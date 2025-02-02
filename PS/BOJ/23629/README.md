# [이 얼마나 끔찍하고 무시무시한 수식이니](https://www.acmicpc.net/problem/23629)

| 시간 제한 | 메모리 제한 |
| :-------: | :---------: |
| 1 초      | 256 MB      |

## 문제

하루 종일 숫자만 보다가 정신이 나가버린 사람이 무시무시한 일을 저질러 버렸다. 숫자가 보기 싫으면 없애면 된다고 생각하며 아래와 같은 무시무시한 문자열을 쓴 것이다.

`ONETWOTHREEFOUR+TWOTHREEFOURFIVE=`

그렇다. 숫자만 안 보이면 된다. 그래서, 아래의 표를 보고 숫자를 모두 영단어로 바꾸었다.

| 숫자 | 영단어 |
| :--: | :----: |
| 0    | ZERO   |
| 1    | ONE    |
| 2    | TWO    |
| 3    | THREE  |
| 4    | FOUR   |
| 5    | FIVE   |
| 6    | SIX    |
| 7    | SEVEN  |
| 8    | EIGHT  |
| 9    | NINE   |

그런데 이런, 문자열을 보다가 그만 문자열을 적은 사람이 정신을 잃었다. 우리가 문자열을 보고 원래의 식을 계산해서 알려주자. 변환되기 전의 수식을 정확하게 판단하여 정답을 구할 수 있다면, 정답을 출력하자. 만약 변환되기 전의 수식으로 가능한 것이 없다면 "**Madness!**"를 출력하자.

변환되기 전의 수식은 양의 정수로 시작해서 양의 정수와 연산자가 번갈아서 등장하며, 마지막 연산자는 =이고, =은 수식의 마지막에만 등장한다. 등장하는 연산자는 +, -, x, /, =으로 총 5가지가 있다. 기존의 사칙연산 방식과는 다르게 앞에서부터 순서대로 계산이 이루어지며, / 연산의 결과로 정수가 아닌 수가 나오면 0에 가까운 방향으로 반올림된다. 예를 들어 1.8은 1로, -1.8은 -1로 반올림된다.


## 입력

영문 대문자 및 +,-,x,/,=로 이루어진 문자열이 주어진다. 문자열은 =로 끝나며, 연산자로 시작하지 않는다. =은 항상 문자열의 마지막에만 등장한다. 문자열의 시작 또는 연산자의 바로 다음에 "ZERO"가 등장하는 경우는 없다.

주어지는 문자열 S의 길이는 4 ≤ | S | ≤ 100,000 이고, 문자열에 포함된 수는 1 이상 1,000,000 이하이다.


## 출력

변환되기 전의 수식으로 가능한 것이 없는 경우, **Madness!** 를 출력한다.

가능한 수식이 있을 경우, 첫 번째 줄에는 그 수식을 출력하고, 두 번째 줄에는 식의 계산값을 모든 숫자를 다시 영단어로 변환하여 출력한다.


## 제한

정답 및 계산 과정 중에 나오는 수의 절댓값은 모두 10^15보다 작다.

