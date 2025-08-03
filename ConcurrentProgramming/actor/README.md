# 액터

해당 내용은 [7가지 동시성 모델](https://www.hanbit.co.kr/store/books/look.php?p_code=B3745244799)의 액터 부분을 참고하여 정리했다.

기본적으로 erlang 기반의 elixir를 바탕으로 설명한다.

## 액터 모델의 핵심

전체적으로 객체지향과 유사한 패러다임이지만, 아래와 같은 주요 특징을 가진다.

1. 액터는 다른 액터들과 동시에 동작을 수행한다.  
    객체처럼 수동적으로 동작하는 것이 아니고, 자체적으로 돌아간다.  
    참고로 동시 - 병렬의 관계에서 동시 동작만 명시한다.
2. 객체는 메서드를 호출하여 메시지 전달이란 추상적 동작을 구체화 한다.  
    하지만 액터는 정말로 메시지 전달을 구체적으로 수행한다.  
    (메서드 호출 전까지는 동시 실행되지 않지만, 메시지 송/수신은 동시 실행)
3. 액터는 상태를 캡슐화 하고, 메시지를 전달하는 방식으로 의사소통한다.  
    액터 자체는 가변 상태를 사용하긴 하지만, 공유되는 부분은 제거한다.

액터는 아래 3가지 동작을 할 수 있어야 한다.

1. 메시지를 받을 수 있어야 한다.
2. 메시지를 전송할 수 있어야 한다.
3. 액터를 새로 생성할 수 있어야 한다.

## 메시지와 메일박스

엘릭서에서 메시지는 아래와 같이 일련의 값으로 이뤄진 튜플을 전송한다.

```elixir
{:foo, "this", 42}
```

제일 앞은 키워드(메시지 종류), 그 뒤에 붙는 값는 각 키워드에 추가로 필요한 데이터다.

```elixir
defmodule Talker do
  def loop do
    receive do
      {:greet, name} -> IO.puts("Hello #{name}")
      {:praise, name} -> IO.puts("#{name}, you're amazing")
      {:celebrate, name, age} -> IO.puts("Here's to another #{age} years, #{name}")
      {:shutdown} -> exit(:normal)
    end
    loop
  end
end  
```

액터는 loop만 구현하여, 그 안에서 각 메시지를 받으면 어떤 동작을 수행해야 하는지 정의한다.

자세히 보면 코드에서 loop는 메시지를 받아서 처리하고, loop 자신을 다시 호출하여 재귀적으로 반복을 일으킨다. (재귀가 반복으로 전환되는 부분은 함수형에서는 반복의 일부이며, 절차형의 구현에서는 꼬리재귀 최적화를 생각하면 된다.)

액터를 실행시키는 코드는 아래와 같이 액터를 생성하고, 메시지를 보낸다.

```elixir
Process.flag(:trap_exit, true)
pid = spawn(&Talker.loop/0)
send(pid, {:greet, "Huey"})
send(pid, {:praise, "Dewey"})
send(pid, {:celebrate, "Louie", 16})
send(pid, {:shutdown})

receive do
  {:EXIT, ^pid, reason} -> IO.puts("Takler has exited (#{reason})")
end
```

위와 같이 메시지를 보낼 때 비동기 방식으로 전달하며, 액터가 바로 메시지를 받지 않고, 메일박스에 전달한다. 메일박스는 일종의 큐다.

메일박스는 원칙적으로 액터마다 하나씩 들고 있어야 한다. (뒤에 언급되지만, 액터는 문제가 생기면 실패시키고 재성성시키므로, 메일박스가 하나로 통일되면 시스템 전체 장애로 이어질 수 있다.)

상태를 가지는 액터는 아래와 같이 작성할 수 있다.

```elixir
defmodule Counter do
  def loop(count) do
    receive do
      {:next} ->
        IO.puts("Current count: #{count}")
        loop(count + 1)
    end
  end
end

counter = spawn(Counter, :loop, [1])
send(counter, {:next})
send(counter, {:next})
send(counter, {:next})
```

액터가 메시지 기반으로 처리하는 것도 알았고, 상태를 가지는 액터를 만드는 법도 알았다.

하지만 액터를 사용하기 위해 모든 메시지를 다 외우는 것은 힘들다. spawn하기 위한 생성자도 알아야 한다. 그래서 보통 아래와 같이 API를 제공한다. (동작 자체는 메서드와 비슷해 보이지만, 원래 해야 하는 메시지 전달을 적절히 추상화했다는 사실을 이해해야한다.)

```elixir
defmodule Counter do
  def start(count) 애
    spawn(__MODULE__, :loop, [count])
  end
  def next(counter) do
    send(counter, {:next}
  end
  def loop(count) do
    receive do
      {:next} ->
        IO.puts("Current count: #{count}")
        loop(count + 1)
    end
  end
end

counter = Counter.start(42)
Counter.next(counter)
```

액터의 통신은 비동기라고 했지만, 액터들을 사용할 때 동기적으로 프로그래밍 해야 한다면, 액터가 응답을 보낼 때 까지 기다리게 할 수 있다.

```elixir
defmodule Counter do
  def start(count) 애
    spawn(__MODULE__, :loop, [count])
  end
  
  def next(counter) do
    ref = make_ref()
    send(counter, {:next, self(), ref})
    receive do
      {:ok, ^ref, count} -> count
    end
  end
  
  def loop(count) do
    receive do
      {:next, sender, ref} ->
        send(sender, {:ok, ref, count})
        loop(count + 1)
    end
  end
end
```
