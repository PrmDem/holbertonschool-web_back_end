# Node JS Basics
The tasks found in this repository are meant as a first approach to Node JS, taking us from a simple I/O exercise to the creation and organisation of a complex server with Express.

## Requirements
Allowed editors: vi, vim, emacs, Visual Studio Code
All files will be interpreted/compiled on Ubuntu 20.04 LTS using node (version 20.x.x)
All files should end with a new line
Code should use the js extension
Code will be tested using Jest and the command `npm run test`
Code will be verified against lint using ESLint
Code needs to pass all the tests and lint (`npm run full-test`)
All functions/classes must be exported by using this format: `module.exports = myFunction`;
Following files must be shared on the repository: `package.json`, `babel.config.js`, `.eslintrc.js` and `database.csv`

## Tasks
### General information
__Number of tasks:__ 8<br/>
__Completed:__ 2<br/>
__Passed:__ TBA<br/>

### Overview
#### 0. Executing basic javascript with Node JS
Create the function `displayMessage` that prints a string argument in STDOUT.<br/>
See file [`0-console.js`](./0-console.js)

#### 1. Using Process stdin
Create a program where the user can input their name directly in the command line. Expected output:
```
Welcome to Holberton School, what is your name?
John
Your name is: John
This important software is now closing
```
See file [`1-stdin.js`](./1-stdin.js)

#### 2. Reading a file synchronously with Node JS
Using the provided `database.csv`, create a function `countStudents` that accepts a path argument and attempts to read the database synchronously.<br/>
If the database is not available, throw error "Cannot load the database". Otherwise, log the message "Number of students: `NUMBER_OF_STUDENTS`". Example output:
```
Number of students: 10
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
```
Blank lines at the end of the file must not be counted!<br/>
See file [`2-read_file.js`](./2-read_file.js)

