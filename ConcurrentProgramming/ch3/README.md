# 동기 처리 1

동시성 프로그래밍을 할 때, 여러 프로세스 사이 타이밍 동기화, 데이터 업데이트 등이 필요하다. 이러한 작업을 동기 처리라 한다.

## 레이스 컨디션

여러 프로세스가 동시에 공유하는 자원에 접근함에 따라 일어나는 예상치 않은 이상이나 상태

레이스 컨디션을 일으키는 프로그램 코드를 크리티컬 섹션이라 하며, 보호하기 위해 동기 처리가 필요하다.

## 아토믹 처리

더 이상 나눌 수 없는 단위로 처리하는 방법. 보통 한 개의 연산이 아니라, 여러 번의 메모리 접근이 필요한 작업을 아토믹하게 한다.

> 어떤 처리가 아토믹하다 = 해당 처리 도중 상태는 관측 불가하며, 만약 처리 실패 시, 원래 상태로 돌아온다.

트랜잭션과 비슷하지만 (All or Nothing) 현대 CPU가 지원하는 일부 간단한 명령어를 활용하는 것을 말한다.

### Compare and Swap

세마포어, 락프리, 웨이트 프리 데이터 구조 구현에 이용한다.

전체적인 동작 흐름을 코드로 작성하면 아래와 같다.

```c
bool cmopare_and_swap(uint64_t *p, uint64_t val. uint64_t newval) {
    if (*p != val) {
        return false;
    }
    *p = newval;
    return true;
}
```

책에서 나오듯, 실제로 해당 코드를 컴파일하면 여러 어셈블리 명령어 조합으로 나오며, 아토믹한 명령어가 아니게 된다. gcc나 clang의 내장 함수인 `__sync_bool_compare_and_swap()`을 호출해야 의도한대로 아토믹한 명령어를 사용하게 된다.

```asm
movq %rsi, %rax
xorl %ecx, %ecx
lock cmpxchgq %rdx, (%rdi)
sete %cl
movl %ecx, %eax
retq
```

위는 x86_64 어셈블리로 표현한 `__sync_bool_compare_and_swap()` 함수 호출을 래핑한 함수이다. 여기에서 `lock`은 `%rdi`의 주소값은 여러 코어가 있더라도 동시에 하나만 접근해야 함을 의미한다.

### Test and Set

부울 변수 `p`의 값을 확인하여, `true`였다면 `true`를, `false`였다면 `true`로 변경하고, `false`를 반환한다.

동일하게 아토믹 처리로 제공되며, 스핀락을 구현할 때 사용된다.

```c
bool test_and_set(bool *p) {
    if (*p) {
        return true;
    } else {
        *p = true;
        return false;
    }
}
```

컴파일러 내장 함수인 `__sync_lock_test_and_set()` 함수는 아래와 같이 동작성이 다르다.

```c
type __sync_lock_test_and_set(type *p, type val) {
    type tmp = *p;
    *p = val;
    return tmp;
}
```

내장 함수에서 뒤의 `val` 값을 1로 설정하면 처음에 언급한 `test_and_set()` 함수와 동일한 역할을 하게 된다.

```asm
movb  $1, %al
xchgb %al, (%rdi)
andb  $1, %al
retq
```

위의 `xchgb` 명령은 따로 언급하지 않아도 lock이 붙어있는 것으로 취급한다.

`__sync_lock_release()`를 통해 lock을 건 변수를 해제할 수 있다.

### Load-Link / Store-Conditional

x86_64는 `lock` 명령어 접두사로 메모리 접근을 배타적으로 할 수 있고, ARM64 등은 Load-Link / Store-Conditional 명령으로 아토믹 처리를 구현한다.

Load-Link는 특정 변수(공유된 메모리 영역)를 읽을 때, 링크를 걸어 놓고, Store-Conditional은 그 변수의 링크가 유효할 때만 값을 저장하는 방식이다.  
Load-Link가 수행된 상황에서 다른 프로세스가 해당 변수에 쓰기를 하면, 링크가 유효하지 않게 된다. (앞에서 Load-Link 할 때의 값이 아니게 된다.)  
Store-Conditional은 위의 Link가 유효할 때만 값을 저장할 수 있게 한다.

## 뮤텍스

~~작성 필요~~

## 세마포어

~~작성 필요~~

## 조건 변수

~~작성 필요~~

## 배리어 동기

메모리 배리어 개념은 아니고, 조건변수나 세마포어 사용 예시와 비슷한데, 주어진 조건이 만족될 때 까지 기다리다가 실행될 수 있게 하는 개념이다.

```c
void barrier(volatile int *cnt, int max) {
    __sync_fetch_and_add(cnt, 1);
    while (*cnt < max);
}
```

### pthread를 이용한 배리어 동기

기존 코드는 max 값에 도달하기까지 반복문을 수행하므로 CPU 낭비 가능성이 있다. 모든 barrier count가 채워지기 전까지는 조건 변수를 활용하여 대기시키다가, 마지막 대기 카운터가 채워질 때 알리는 방식을 사용한다.

### Rust 동기 처리 라이브러리

`std::sync::Barrier`가 제공된다.

## Readers-Writer 락

동기화 문제의 핵심 원인은 쓰기 때문이다. (원하는 생태로 쓰는 일관성을 유지하기 위해 쓰기를 배타적으로 한다.) 즉, 읽기들 끼리는 배타적일 필요가 없다는 생각에서 조금이라도 효율적인 활용을 하기 위한 접근법이다.

* 락을 획득 중인 Reader는 같은 시각에 다수(0 이상) 존재할 수 있다.
* 락을 획득 중인 Writer는 같은 시각에 1개만 존재할 수 있다.
* Reader와 Writer는 같은 시각에 락 획득 상태가 될 수 없다.

### 스핀락 기반 RW락

```c
void rwlock_read_acquire(int *rcnt, volatile *wcnt) {
    while (1) {
        while (*wcnt);
        __sync_fetch_and_add(rcnt, 1);
        if (*wcnt == 0)
            break;
        __sync_fetch_and_sub(rcnt, 1);
    }
}

void rwlock_read_release(int *rcnt) {
    __sync_fetch_and_sub(rcnt, 1);
}

void rwlock_write_acquire(bool *lock, volatile int *rcnt, int *wcnt) {
    __sync_fetch_and_add(wcnt, 1);
    while (*rcnt);
    spinlock_acquire(lock);
}

void rwlock_write_release(bool *lock, int *wcnt) {
    spinlock_release(lock);
    __sync_fetch_and_sub(wcnt, 1);
}
```

보면 Reader는 실질적인 lock을 걸지는 않으며, 카운터 기반으로 대기하게 되어있다.

### pthread의 RW락

rwlock API를 제공한다.

### 실행 속도 측정

코드 조건에 따라 잠금 API를 다르게 써서 성능을 측정해보면, Reader가 많은 경우는 효율이 잘 나오지만, Writer가 생기면 실질적으로 mutex와 동일한 수준의 성능이 나오는 것을 알 수 있다.

## 베이커리 알고리즘

지금까지의 알고리즘은 atomic 명령어를 제공하는 환경을 기준으로 했다. 하지만 해당 명령어를 제공하지 않는 환경에서는 베이커리 알고리즘, 데커 알고리즘, 피터슨 알고리즘을 사용할 수 있다.

베이커리 알고리즘은 순차적으로 번호가 증가하는 티켓을 발급받고, 자신의 티켓 번호가 가장 낮을 때 실행하는 알고리즘이다. 기본적인 논리는 간단하게 순차적으로 증가하는 것이지만, 현대 CPU에서는 OoOE 등 최적화로 인해 제대로 작동하지 않을 수 있다.

이 경우에 Fence를 사용하여 순서를 강제로 보장한다.
