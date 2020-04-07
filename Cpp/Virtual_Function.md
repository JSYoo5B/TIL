# Virtual function

C++에서 class를 작성하고, 해당 class를 상속 받는 상황을 생각해보자.

```cpp
class Person {
public:
    void PrintName() {
        printf("My name is not determined");
    }
}

class Child: Person {
public:
    void PrintName() {
        printf("My name is Alpha");
    }
}
```

간단하게, 부모와 자식이 같은 이름의 함수(+ 같은 시그니쳐)를 갖고 있고,
자식은 부모의 함수를 재정의(override)한 상태이다.  

아래와 같이 각 class type의 instance에서 해당 함수를 호출해보자.

```cpp
// pPerson에 연결한 instance가 Person type이라고 가정하자.
Person *pPerson = GetPerson(..., JUST_PERSON);
// 아마 "My name is not determined"가 출력될 것이다.
pPerson->PrintName();

// pPerson에 연결한 instance가 Child type이라고 가정하자.
Person *pPerson = GetPerson(..., CHILD);
// 과연 "My name is Alpha"라고 출력할까?
pPerson->PrintName();
```

지금 예시로 든 경우가 너무 단순해서 그렇지, 보통 상속이 일어나는 경우는
공통적인 기능에 대한 것만 부모 class에서 작성하고, 해당 구현이 각 자식 class마다
다르지만, 특정 함수를 호출하는 데 있어서 일관성있게 호출하는 것이 목적일 것이다.

어쨋든 저 상태로 출력하면 높은 확률로 "My name is not determined"가 출력될
것이다. 부모 class pointer에서 함수를 호출하더라도 해당 instance가 자식 class
type일때 override된 함수가 호출되길 바란다면, 부모 class의 함수 정의에서
virtual을 붙여줘야 한다.

```cpp
class Person {
public:
    virtual void PrintName() {
        printf("My name is not determined");
    }
}

class Child: Person {
public:
    void PrintName() {
        printf("My name is Alpha");
    }
}
```
