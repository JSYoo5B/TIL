# 형식 언어

## 언어의 정의

* 언어: 문장의 집합
* 문장: 단어의 집합
* 문법: 단어들을 구성하는 방법

### 언어의 수학적 정의

* Alphabet: `T` (언어에서 어떤 글자로 구성되는가)
* String: `w` (알파벳을 연속으로 연결한 문자열)
* Length: `|w|` (문자열의 길이)
* Empty string: `e` (문자열 중 길이가 0인 것)
* 가능한 문자열의 집합 표현
  * `T*` (알파벳 0개 이상으로 연결한 문자열, `e` 포함)
  * `T+` (알파벳 1개 이상으로 연결한 문자열, `e` 제외)
* Language: `L` (언어를 구성하는 문자열의 집합)
  * `L`은 `T*`의 부분집합 (모든 가능한 문자열 중 일부만 언어로 정의)
* 수식 연산에 대한 정의도 있으나 이건 생략

수학적 정의가 무슨 의미가 있는가?

* 언어에 어떤 글자가 들어갈 수 있는지 유한하게 정의
* 언어를 정의한다는 것은 유효한 문자열 집합을 정의한다는 것

## 언어의 표현

수학적으로 언어 == 문자열의 집합임은 알게 됨, 그렇다면 언어는 어떻게 표현할 것인가?

* 원소 나열 및 조건 제시
  * 각 프로그래밍 언어의 키워드들은 원소 나열이 가능함  
    `if`, `switch`, `break`, `return`은 모두 나열 가능
  * 하지만 원소 나열만으로는 모든 문자열의 조합을 나타내기 힘듬  
    `my_123`은 프로그래밍 언어의 변수/상수/함수가 될 수 있음  
    하지만 모든 경우의 수를 다 표현해서 집합으로 표현하는건 힘듬  
    길이 제한이 없다면 언어의 원소 개수가 무한해짐
* 생성 규칙을 표현하여 언어의 조건을 제시해야 한다
  * `Grammar`로 생성 규칙을 표현
  * 이 문자열이 언어에 속하는지 확인하는 `Recognizer`가 필요 (오토마타)

## 문법

### 문법의 수학적 정의

* Grammar: `G = (Vn, Vt, P, S)`
  * Non-terminal symbols: `Vn` (사용할 알파벳이 완전히 결정되지 않은 상태, 문법적인 개념)
  * Terminal symbols: `Vt` (사용할 알파벳이 완전히 결정된 상태, 실제 언어를 구성하는 단어의 일부)
  * Production rule: `P` (`V`에서 다음 `V`로 갈 수 있는 방법을 정의)
  * Start(sentence) symbol: `S` (문법 심볼의 시작점)
* `Vn`과 `Vt`는 교집합이 없음

### 예시를 통한 언어 구성 과정

> G = ({A, B, C}, {a, b, c}, P, A)  
> P: A -> abc | aBbc  
>    Bb -> bB  
>    Bc -> Cbcc  
>    bC -> Cb  
>    aC -> aaB  
>    aC -> aa

(참고로 terminal과 non-terminal이 연결되는 rule은 context-sensitive grammar임)

#### abc 유도

> A => abc

#### aabbcc 유도

> A => aBbc  
>   => abBc     // Bb -> bB  
>   => abCbcc   // Bc -> Cbcc  
>   => aCbbcc   // bC -> Cb  
>   => aabbcc   // aC -> aa

### 문법 기술 방법

사실 문법의 핵심은 Production rule임

* Embedded production rule: 시작 symbol이 production 결과에 포함되는, recursive