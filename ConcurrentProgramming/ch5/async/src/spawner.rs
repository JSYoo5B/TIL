use crate::task::Task;

use std::sync::{Arc, Mutex};
use std::sync::mpsc::SyncSender;
use futures::FutureExt;

pub struct Spawner {
    pub sender: SyncSender<Arc<Task>>,
}

impl Spawner {
    pub fn spawn(&self, task: impl Future<Output = ()> + 'static + Send) {
        let future = task.boxed();
        let task = Arc::new(Task {
            future: Mutex::new(future),
            sender: self.sender.clone(),
        });
        
        self.sender.send(task).unwrap();
    }
}