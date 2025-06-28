use std::pin::Pin;
use std::task::{Context, Poll};

pub struct Hello {
    state: StateHello,
}

enum StateHello {
    HELLO,
    WORLD,
    END,
}

impl Hello {
    pub fn new() -> Self {
        Hello {
            state: StateHello::HELLO,
        }
    }
}

impl Future for Hello {
    type Output = ();

    fn poll(mut self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<()> {
        match (*self).state {
            StateHello::HELLO => {
                print!("Hello, ");
                (*self).state = StateHello::WORLD;
                cx.waker().wake_by_ref();
                Poll::Pending
            }
            StateHello::WORLD => {
                println!("World!");
                (*self).state = StateHello::END;
                cx.waker().wake_by_ref();
                Poll::Pending
            }
            StateHello::END => {
                Poll::Ready(())
            }
        }
    }
}