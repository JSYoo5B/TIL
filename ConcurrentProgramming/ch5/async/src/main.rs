use crate::executor::Executor;
use crate::hello::Hello;

mod executor;
mod task;
mod spawner;
mod hello;

fn main() {
    let executor = Executor::new();
    executor.get_spawner().spawn(async{
        let h = Hello::new();
        h.await;
    });
    executor.run();
}
