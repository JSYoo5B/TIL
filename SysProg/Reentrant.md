# [reentrant](https://sunyzero.tistory.com/97)

내가 생각한 reentrant라는 개념은 lock이 thread 단위로 걸리는 걸로 이해했는데
그게 아니다. 내가 생각한 개념은 예를 들어 thread-A가 mutex1를 lock해서 critical
section으로 진입했고, 그 안에서 사용하는 함수가 또 mutex1을 lock하려고 했을 때
wait이 걸려서 deadlock이 되지 않는 것을 생각했는데, 그거랑 다른 개념이다.

thread safety 중에서도 재귀 호출을 포함한 병렬 실행이 보장되는 것들을
reentrant라고 하는 것이다. 이해한대로라면 순수함수들은 언제나 reentrant할 것
같은데, 순수함수는 thread safety 정의에 나와 있는 예시로만 언급되어 있다. 그럼
순수함수 중에서도 reentrant하지 않은 함수가 있다는 것 같은데, 이건 순수함수의
정의를 좀 더 확인해 봐야 할 것 같다.
