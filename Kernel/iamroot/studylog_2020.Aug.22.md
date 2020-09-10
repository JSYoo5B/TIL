# 스터디 목적

리눅스 커널, 운영체제에 대한 전반적인 구조를 이해하기 위한 이론 공부

## 스터디 범위

리눅스 커널 내부 구조 Chapter0 ~ Chapter3 (p10 ~ p93)

## 토의 내용 (자체 해결 완료)

### Q. 디스크 블록의 크기는 (일반적으로 4KB) 무엇을 기준으로 결정되었는가? (p12)

* 해당 부분의 맥락으로 보았을 때, 커널에서 디스크 사용 시 이미 지정된 Unit 단위이며,
  이를 OS가 제공한다는 점만 이해하고 넘어가도 될 것 같음.
* 굳이 4KB인 것은 page size가 4KB라서 그런 것이 아닐까?

### Q. 파일시스템을 사용자가 일관된 인터페이스로 접근한다는 것이 무슨 소리인가? (p38)

* 물리적으로 사용하는 파일시스템 포멧이 FAT32건, ext4건, 커널을 통해 파일을 쓸때는
  create(), open(), read(), write(), close() 등의 syscall을 통해 접근함.
* 그 개념을 위해 VFS (Virtual File System)이 존재하며, 여기에서 각 파일시스템 포멧의
  상황에 맞게 실제 syscall의 동작을 수행할 수 있도록 호출해 주는 것을 뜻함.
* 이전의 Unix 관련 설계 이야기에서도 Unix/Linux의 설계 상 가장 큰 특징 중 하나가
  IO처리 (ex. /dev/ttyUSB0), 실제 disk 기록 (ex. /usr/...), 내부 설정 (ex. /sys/...) 등을
  모두 파일 처리 방식으로 가능케 한다는 것으로 알고 있음.

### Q. execl()을 통해 기존 프로세스의 수행 이미지가 바뀌는 과정에서 내부적으로 do\_fork()가 일어나는 것이 아닐까? (p57)

* task\_struct의 관계는 그대로 유지되지만, 새 이미지 실행을 위한 부분 (.text, .data, .stack...)만 변경됨
* 예시 프로그램의 printf("Before exec\"); 부분에 getpid() 값을 찍어 확인해본 결과 execl()의 task와 같은 PID임이 확인됨.
* PID 안 바뀜, task\_struct 새로 생성되는 것 아님, 내부적으로 do\_fork() 호출하지 않음.
* execl()에서 호출한 프로그램이 하필 fork()를 호출하는 것, 문장의 구성으로 인해 잠시 오해했던 것으로 고려됨.

### Q. n개의 CPU를 갖는 시스템에서는 임의의 시점에 최대 n개의 task라는 것이 Physical core인가? Logical processor인가? (p70)

* 여기서 표현하는 Physical core는 독립적으로 말하는 CPU core 수 (ex. Dual core -> 2개 Physical core)를 뜻함.
* 여기서 표현하는 Logical processor는 각 Physical core에서
  Hyper-threading 등으로 구현되는 논리적으로 잡히는 processor를 뜻함.
* 당시에는 Physical core를 뜻하는 것으로 예측하는 것으로 넘어감.
* 추후 다룬 Runqueue 부분에서의 언급을 통해 Logical processor를 뜻하는 것이 맞을 것으로 예상함. (p77)

### Q. EXIT\_ZOMBIE 상태가 유지되는 경우(시스템에 불필요한 부하를 주는 상태)는 어떤 경우인가? (p71)

* 일반적인 Process의 경우, 부모 Process가 wait() 호출 등으로 자식 Process가 EXIT\_DEAD로 바뀌게 허가해 줄 것임.
* 하지만 부모 Process가 비정상 종료 시 (내부적인 fault 등으로 인해) 예기치 않게 종료될 경우, 이를 허가해 줄 수 없음.
* 그렇기 때문에 EXIT\_DEAD로 바뀔 수 있게 허가를 받아야 하는데, 이를 init 태스크가 처리해 준 다는 것.
* 아마도 real\_parent 필드는 자신을 fork()시킨 부모 Process를 가리키고 (바뀌지 않음)
  parent 필드는 상황에 따라 원래 부모 Process에서 init 태스크로 바뀔 수 있을 것으로 예상함.

### Q. SIGKILL이 발생하는 경우는 어떤 경우인가? (p72)

* 당시 생각한 Ctrl+C 는 SIGKILL이 아니라 SIGINT(Interrupt Signal)임.
  그렇게 생각되는 이유는 SIGINT에 handler가 등록되지 않은 경우,
  default handler가 해당 process를 종료시키기 때문임.
* SIGKILL은 대부분 명시적으로 호출했을 때만 발생함. (ex. kill -9 $PID)
  [참고 링크 (GNU signal 설명)](https://www.gnu.org/software/libc/manual/html_node/Termination-Signals.html)
* kill 명령어는 기본적으로 SIGTERM(종료 요청)을 대상 process에게 전송함.
  이는 어디까지나 **종료 요청**이므로, handler에서 종료를 방지할 수도 있음.
  (ex. 워드에서 수정 후 저장되지 않은 상태에서 종료 시 저장 여부를 물어보는 등)
* kill 명령어의 예시에서 나온 -9 옵션은 SIGKILL의 Portable number임.
  [참고 링크 (Wiki)](https://en.wikipedia.org/wiki/Signal_%28IPC%29#POSIX_signals)
  즉, kill 명령어는 process가 자발적으로 종료될 수 있도록 Signal을 보내는 것이며,
  특히 kill -9는 무조건 강제 종료하라는 뜻이다. (직접 handler를 등록할 수 없고, 무조건 종료되므로)
* 아마 shutdown, halt, reboot 등의 명령어도 처음에는 모든 process에게 SIGTERM을 전송하여 자발적 종료를 유도한 뒤,
  일정 시간 뒤에도 여전히 살아있는 process를 기다리다가 결국엔 SIGKILL로 완전 종료시킴.
  [shutdown 소스 참고](https://github.com/systemd/systemd/blob/f8bff7805ea1252c2421d07a92bf5b19f4f16aa7/src/shutdown/shutdown.c#L392-L396)

### Q. 캐시 친화력이 무슨 뜻인가? (p76)

* 현대 컴퓨터는 실제 접근 속도가 빠른 cache에서 수행함. 그 대신 비싸기 때문에 현실적으로 공간 제한이 있음.
* 메모리 접근하는 정보를 확인해보니, 시간에 따라 계속 사용하던 곳 근처를 사용하던 버릇이 있음. (Locality of reference)
* 이에 따라, cache에 일정 메모리 구역을 올려 놓으면, 그 구역의 메모리를 제대로 쓸 수 있게 됨. 이 단위가 사실상 page임.
* fork()나 clone()으로 생성된 task도 기존 task와 유사할 가능성이 높으므로, 이를 활용한다는 뜻임.

### Q. Scheduling 정책은 어떻게 결정되는가? (p79)

* sched\_setscheduler() 등의 함수를 통해 바꾼다고 했으므로, task가 어떤 정책으로 scheduling 받길 원하는지 결정하는 것으로 보임.
* 만약 scheduler가 직접 정책을 결정하고, 설명된 scheduling 정책 중 하나만을 선택하는 것이라면,
  rq 구조체의 FIFO & RR 관련 구조체와 DEADLINE 관련 구조체를 union으로 묶었을 것임. (메모리 절약)

### Q. 우선순위 FIFO & RR에서 우선순위대로 선택하면 낮은 우선순위는 starvation에 걸리지 않는가? (p80)

* 책에서 설명한 내용대로면 이론상 그게 맞음. 이를 방지하기 위한 방법 등이 전혀 설명되지 않음.
* 하지만 이런 설명이 전혀 없는 것으로 봤을 때, 실제 해당 현상이 나타나지 않는 것으로 보임.
* 우리가 생각하는 기준으로는 심각할 것 같지만, 컴퓨터의 동작시간 기준으론 매우 짧게 동작할 것이라 예상.
* 위의 sched\_setscheduler()와 같이 순간적으로 필요한 순간만 realtime으로 scheduling받고, 끝나면 다시 돌아가지 않을까 예상함.

## 토의 내용 (불확실)

### Q. 커널 컴파일 과정에서 objcopy가 하는 역할, 의미는 무엇인가? (p43)

* 정확하진 않은데 컴파일 과정에서 생기는 Symbol 정보 등을 지우고 순수 machine code만 남기는 것 아닐까?
* 실제 커널이 컴파일 되는 과정을 분석해봐야 정확히 이해할 수 있을 듯 함.

### Q. 리눅스가 지원한다는 Linux exec 도메인, BSD나 SVR4 exec 도메인은 무슨 뜻인가? (p69)

* 아마도 ELF, PE같은 실행파일의 동작을 위한 format 같은 것을 말하는 것이 아닐까?
  (재컴파일 하지 않고 BSD나 SVR4 커널에서 컴파일된 프로그램이라는 표현에서 예측)
