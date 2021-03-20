# [Functional thinking](https://evan-moon.github.io/2019/12/15/about-functional-thinking/)

해당 글에서 이야기 하는 요소 중 **높은 수준의 추상화**와
**불변성 지향을 통한 동작 예측의 용이함**은 이해했음. 사실 동작 예측의 용이함은
함수형 프로그래밍 패러다임 자체에 대하여 인식했을 때 부터 알고 있었고, 높은
수준의 추상화는 해당 글에서 언급한
[함수형 사고](http://www.hanbit.co.kr/media/community/review_view.html?hbr_idx=3321)를
부분적으로 읽었을 때 이해했다. 현재 내가 이해한게 맞다면 코드의
**언어적, 접근 방법**에서의 추상화가 지원되는 환경이라면 (함수형 패러다임
언어라면) 이를 활용하자는 것이고, 결국 코드를 더 직관적으로 이해할 수 있게 해서
가독성, 유지보수성, 간결함을 확보할 수 있다는 것이 장점이라는 것이다.
물론 그 trade-off로 성능은 떨어지겠지만.

이와 관련된 다른 글인
[순수 함수](https://evan-moon.github.io/2019/12/29/about-pure-functions/)도
읽었는데, 순수함수 관련 내용은 이해는 하지만 현재 내가 적용하기에는 힘들어
보인다. 내 개발 환경이 C 기반의 프로그래밍이니 모듈화 해서 주어진 함수만을 통해
state transition하는 수 밖에 없으니 메인 개발에는 전혀 적용을 못한다. 현재 적용
가능한 것은 inline 함수나 macro function 정도밖에 안 될듯 하다.

가끔 python으로 작성한 좋은 코드들을 보면 functional하게 잘 쓰는 것 같은데, 이
부분에 대해서는 공부가 필요하겠다. 현재 내가 짜는 python code는 말이 python이지,
사실상 C scripting 수준으로 작성하고 있으니깐.
