# Python: Async

## Requirements
* Allowed editors: vi, vim, emacs
* All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
* All files should start with `#!/usr/bin/env python3`, end with a new line, and be executable
* Code should use the pycodestyle style (version 2.5.)
* File length will be tested using wc
* All functions, modules, and classes should have a documentation
* All functions and coroutines must be type-annotated

### General information
__Number of tasks:__ 5<br/>
__Completed:__ 5<br/>
__Passed:__ 5<br/>

#### 0. The basics of async
Using the `random` module, passes an integer argument (`max_delay`, default value = 10) to the function `wait_random`. This function waits for a random delay (between 0 and `max_delay` included seconds) before returning that delay as a float.<br/>
See file [`0-basic_async_syntax.py`](./0-basic_async_syntax.py)
#### 1. Let's execute multiple coroutines at the same time with async
Based off `wait_random`, the async routine `wait_n` takes 2 _int_ arguments: `n` and `max_delay`. Spawns `wait_random` _n_ times with the specified max_delay and returns the list of delays as float values. <br/>
The list of the delays should be in ascending order, without using `sort()`.<br/>
See file [`1-concurrent_coroutines.py`](./1-concurrent_coroutines.py)
#### 2. Measure the runtime
Measures the runtime of `wait_n` using the `time` module, and returns this value divided by `n`.<br/>
See file [`2-measure_runtime.py`](./2-measure_runtime.py)
#### 3. Tasks
The non-async function `task_wait_random` takes a `max_delay` integer and returns an `asyncio.Task`.<br/>
See file [`3-tasks.py`](./3-tasks.py)
#### 4. Tasks
The `wait_n` function is modified to incorporate `task_wait_random`, becoming `task_wait_n`.<br/>
See file [`4-tasks.py`](./4-tasks.py)