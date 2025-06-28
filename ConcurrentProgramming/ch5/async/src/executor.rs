use crate::task::Task;
use crate::spawner::Spawner;

use std::sync::Arc;
use std::sync::mpsc::{sync_channel, Receiver, SyncSender};
use std::task::Context;
use futures::task::waker_ref;

pub struct Executor {
    sender: SyncSender<Arc<Task>>,
    receiver: Receiver<Arc<Task>>,
}

impl Executor {
    pub fn new() -> Self {
        let (sender, receiver) = sync_channel(1024);
        Executor {
            sender: sender.clone(),
            receiver,
        }
    }

    pub fn get_spawner(&self) -> Spawner {
        Spawner {
            sender: self.sender.clone(),
        }
    }

    pub fn run(&self) {
        while let Ok(task) = self.receiver.recv() {
            let mut future = task.future.lock().unwrap();
            let waker = waker_ref(&task);
            let mut ctx = Context::from_waker(&waker);

            let _ = future.as_mut().poll(&mut ctx);
        }
    }
}