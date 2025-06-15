use std::sync::{Arc, Mutex};
use std::thread;

fn some_func(lock: Arc<Mutex<u64>>) {
    let mut val= lock.lock().unwrap();
    *val += 1;
    println!("val: {}", *val);
}

fn main() {
    // Number of threads to create - change this value to increase/decrease threads
    const NUM_THREADS: usize = 20;

    // Create the initial mutex
    let initial_lock = Arc::new(Mutex::new(0));

    let mut threads = Vec::with_capacity(NUM_THREADS);

    for _ in 0..NUM_THREADS {
        let lock_clone = initial_lock.clone();
        threads.push(thread::spawn(move || {
            some_func(lock_clone);
        }));
    }

    for thread in threads {
        thread.join().unwrap();
    }
}
