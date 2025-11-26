# Python: Async Comprehension

## Requirements
* Allowed editors: vi, vim, emacs
* All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
* All files should start with `#!/usr/bin/env python3`, end with a new line, and be executable
* Code should use the pycodestyle style (version 2.5.)
* File length will be tested using wc
* All functions, modules, and classes should have a documentation
* All functions and coroutines must be type-annotated

### General information
__Number of tasks:__ 3<br/>
__Completed:__ TBA<br/>
__Passed:__ TBA<br/>

#### 0. Async Generator
The coroutine `async_generator` will loop 10 times, waiting a second each time, then yield a random number between 0 and 10.<br/>
See file [`0-async_generator.py`](./0-async_generator.py)
#### 1. Async Comprehensions
Collects and returns async_generator's 10 numbers by using async comprehension.<br/>
See file [`1-async_comprehension.py`](./1-async_comprehension.py)
#### 2. Run time for four parallel comprehensions
Using `asyncio.gather`, the `measure_runtime` coroutine executes `async_comprehension` four times in parallel and returns the total runtime.<br/>
See file [`2-measure_runtime.py`](./2-measure_runtime.py)