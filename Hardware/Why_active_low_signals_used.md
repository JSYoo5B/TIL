# [왜 Active-Low 신호를 사용하는가?](https://embeddeddesignblog.blogspot.com/2014/09/basics-why-active-low-signals-used.html)

분명 논리적으로는 0:Off, 1:On이 일반적이고, 심지어 이걸 디지털 시스템 설명의 대표적인 예시로 사용한다.
이를 Active-High 신호라 한다. (전압이 높은 상태가 활성화 상태)

하지만 실제 GPIO 제어 코드(ex. LED), I2C나 SPI 스펙을 보면 Off, Idle 상태를 High상태로 표현한다.
(I2C, SPI에서 실제 신호값의 해석은 전통적인 Low:0, High:1로 해석하지만, 전송하지 않는 대기 상태에서 High를 유지한다.)
심지어 Reset pin도 High 상태를 유지하다가 Low로 낮춰서 재시작시키기도 한다.
이렇게 전압이 높은 상태가 비활성화이고, 전압이 낮은 상태에서 활성화되는 신호를 Active-Low 신호라 한다.

SPI나 I2C는 그냥 통신 인터페이스라 그런가보다 치더라도, GPIO 제어 코드에서 LED를 켜기 위해 0을 출력하는 상황은 
쉽게 이해되지 않을 것이다.

왜 Active-Low 신호를 사용하는지에 대하여 찾아본 결과 아래와 같은 이유가 있었다.

* 반도체의 구조적 이유 (npn MOSFET 트랜지스터의 기본 동작이 Active-Low 구현에 유리함)
* 전력 공급 불안정에 의한 비결정적 상태 제거에 도움을 준다.
* pull-down(전압을 내리는 것) 신호 생성이 pull-up 신호 생성보다 쉬움.
* Wired-OR(점퍼선 연결 등을 통해 OR 구현), 여러 칩에 대한 공용 Reset 가능(하드웨어 확장성).
* Reset과 같이 중요한 신호는 상태가 계속 유지되어야 하는데, Active-High시 노이즈에 의해 Reset이 걸릴 수 있음.
* 사용하는 uC에서 내보내는 전력 공급 한계를 초과할 수 있으므로, 확장성이 낮아진다.

