# 유한 오토마타

문법을 인식하는 방법으로, 다음 글자를 입력으로 받는 유한 상태 기계

{ Q, Σ, δ, q, F }, where:

* Q: Finite set of states
* Σ: Set of input symbols
* δ: Transition function
* q: Initial state
* F: Set of final states

종료 상태: 이 상태에서 오토마타가 종료되어야 문법을 만족한다고 판단

## DFA: Deterministic Finite Automata

각 입력에 대한 상태가 결정적인 경우 (한 입력은 한 상태로 전환이 확정)

## NFA: Nondeterministic Finite Automata

각 입력에 대한 상태가 비결정적인 경우 (한 입력이 여러 상태로 전환 가능)

* 문법의 production rule에서 글자가 중복되는 rule이 있는 경우
* 정규 언어가 아닌, 문맥 자유/문맥 종속 문법에서도 모호성이라는 문제로 취급
  (뭐가 될지 모른다 == 모호하다)

### NFA를 DFA로 변환

* 현재 state가 NFA의 state들 중 하나라면, 다음 전이는 어떻게 가능지 목록 정리
* 여러 state에 존재할 수 있음 자체를 하나로 전환하면, 결정적인 전환이 가능
* state 조합 내 종료 state가 포함되면 그 조합도 종료 state임
* 하지만 2^n-1 만큼 상태가 만들어질 수 있음. 너무 발산함
* 효과적인 방법: start state부터 전환 가능한 state의 조합을 목록 정리
* 도달할 수 없는 결정적 상태를 제거하기 때문에 효율적

### e-NFA를 DFA로 변환

e-NFA는 epsilon 전이가 포함되어 상태가 비결정적인 오토마타

* epsilon 전이가 포함된 상태 자체를 현재 상태로 취급
* e-NFA의 상태들을 일반 NFA처럼 취급한 상태에서 DFA로 전환

## 유한 오토마타 -> 정규문법 변환

문법을 인식한다 == 문법을 표현하는 방법 == 오토마타는 정규문법으로 전환 가능

* 각 상태 전이 == 문법의 production rule
* 종료 상태는 epsilon 전환이 포함되어야 함 (production rule 종료)

## DFA 최적화

같은 문법을 인식할 수 있는 문법/오토마타라면 간단한 것이 좋음  
오토마타 기준으로 상태 수를 줄이면 최적화를 한다고 볼 수 있음

1. 동일한 기능을 하는 state를 하나로 합친다  
    하지만 "동일한 기능"이라는 것을 파악하는 것은 어려움
2. final, non-final state들을 집합으로 묶어서 2개 state로 취급해본다
3. 각 집합 내 state들의 전이 관계를 확인해본다  
    각 입력에 대해 상태 전이가 동일하다면 하나로 묶어도 된다는 뜻
4. 만약 상태 전이 관계가 서로 다르다면, 같은 역할이 아니라는 뜻  
    상태 전이 관계가 다른 상태들만 분리하여 다시 반복