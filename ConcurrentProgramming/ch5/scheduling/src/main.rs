use crate::executor::Executor;
use crate::hello::Hello;

mod executor;
mod task;
mod spawner;
mod hello;

fn main() {
    let executor = Executor::new();
    executor.get_spawner().spawn(Hello::new());
    executor.run();
}
