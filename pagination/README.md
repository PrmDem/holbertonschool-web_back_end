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
__Completed:__ 4<br/>
__Passed:__ 4<br/>

#### 0. Simple helper function
The function `index_range` takes two integer arguments: `page` and `page_size`. It should return `start` and `end` indexes in a **tuple of size two**. The first page is page **1**, and the returned indexes correspond to the indexes of the elements to display.<br/>
See file [`0-simple_helper_function.py`](./0-simple_helper_function.py)
#### 1. Simple pagination
Based off the previous function and a provided Server class, the method `get_page` takes two integer arguments: `page`, with default value 1, and `page_size` with default value 10.<br/>
Using a provided `.csv` file (a list of names) and `assert` to verify both arguments are `int > 0`, we can use `index_range` to find the correct indexes to paginate the dataset correctly, then return the appropriate page (i.e. the correct list of rows).<br/>
If the input arguments are out of range for the dataset, returns an empty list.
See file [`1-simple_pagination.py`](./1-simple_pagination.py)
#### 2. Hypermedia pagination
Based off the previous file, implement a `get_hyper` method that takes the same arguments and defaults as `get_page` and returns a dictionary containing the following key-value pairs:<br/>
* `page_size`: the length of the returned dataset page
* `page`: the current page number
* `data`: the dataset page (equivalent to the return from [task 1](#1-simple-pagination))
* `next_page`: number of the next page, `None` if no next page
* `prev_page`: number of the previous page, `None` if no previous page
* `total_pages`: the total number of pages in the dataset as an integer
See file [`2-hypermedia_pagination.py`](./2-hypermedia_pagination.py)
#### 3. Deletion-resilient hypermedia pagination
The `get_hyper_index` method takes two integer arguments: `index` with a `None` default value and `page_size` with default value of 10.<br/>
It returns a dictionary with the following key-value pairs:<br/>
* `index`: index of the first item in the current page. For example if requesting page 3 with page_size 20, and no data was removed from the dataset, the current index should be 60.
* `next_index`: index of the first item after the last item on the current page.
* `page_size`: size of the current page
* `data`: page resulting from the query
**Expected behaviour:**<br/>
A query of `index 0, page_size 10` should return rows indexed 0 to 9 included.<br/>
If index 10 is queried next but rows 3, 6 and 7 were deleted, rows indexed 10 to 19 included should still be returned.<br/>
See file [`3-hypermedia_del_pagination.py`](./3-hypermedia_del_pagination.py)