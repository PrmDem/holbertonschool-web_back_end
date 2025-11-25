# Python: Variable Annotations

## Requirements
* Allowed editors: vi, vim, emacs
* All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
* All files should start with `#!/usr/bin/env python3`, end with a new line, and be executable
* Code should use the pycodestyle style (version 2.5.)
* File length will be tested using wc
* All functions, modules, and classes should have a documentation

### General information
__Number of tasks:__ 10<br/>
__Completed:__ 10<br/>
__Passed:__ TBA<br/>

#### 0. Basic annotations - add
Takes floats `a` and `b` as arguments and returns their sum as a float.<br/>
See file [`0-add.py`](./0-add.py)
#### 1. Basic annotations - concat
Takes strings `str1` and `str2` as arguments and returns a concatenated string.<br/>
See file [`1-concat.py`](./1-concat.py)
#### 2. Basic annotations - floor
Takes a float `n` as argument and returns its floor.<br/>
See file [`2-floor.py`](./2-floor.py)
#### 3. Basic annotations - to string
Takes a float `n` as argument and returns the string representation of the float.<br/>
See file [`3-to_str.py`](./3-to_str.py)
#### 4. Define variables
Defines and annotates the following variables:<br/>
• `a`, an integer with a value of 1<br/>
• `pi`, a float with a value of 3.14<br/>
• `i_understand_annotations`, a boolean with a value of True<br/>
• `school`, a string with a value of “Holberton”<br/>
See file [`4-define_variables.py`](./4-define_variables.py)
#### 5. Complex types - list of floats
Takes a list of floats `input_list` as argument and returns their sum as a float.<br/>
See file [`5-sum_list.py`](./5-sum_list.py)
#### 6. Complex types - mixed list
Takes a list of integers and floats `mxd_lst` and returns their sum as a float.<br/>
See file [`6-sum_mixed_list.py`](./6-sum_mixed_list.py)
#### 7. Complex types - string and int/float to tuple
Takes a string `k` and an int OR float `v` as arguments and returns a tuple.<br/>
See file [`7-to_kv.py`](./7-to_kv.py)
#### 8. Complex types - functions
Takes a float `multiplier` as argument and returns a function that multiplies a float by `multiplier`.<br/>
See file [`8-make_multiplier.py`](./8-make_multiplier.py)
#### 9. Let's duck type an iterable object
The goal of this task is to annotate the parameters and return values of the function, to get the expected return (`{'lst': typing.Iterable[typing.Sequence], 'return': typing.List[typing.Tuple[typing.Sequence, int]]}`)
See file [`9-element_length.py`](./9-element_length.py)