# Pagination
Or: the Art of not Overloading your Pages, Servers, and Users with Endless Information.<br/>

## Requirements
* Allowed editors: vi, vim, emacs
* All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
* All files should start with `#!/usr/bin/env python3` and end with a new line
* Code should use the pycodestyle style (version 2.5.)
* File length will be tested using wc
* All functions, modules, and classes should have a documentation
* All functions and coroutines must be type-annotated

### General information
__Number of tasks:__ 4<br/>
__Completed:__ 1<br/>
__Passed:__ N/A<br/>

#### 0. Simple helper function
The function `index_range` takes two integer arguments: `page` and `page_size`. It should return `start` and `end` indexes in a **tuple of size two**. The first page is page **1**, and the returned indexes correspond to the indexes of the elements to display.<br/>
See file [`0-simple_helper_function.py`](./0-simple_helper_function.py)