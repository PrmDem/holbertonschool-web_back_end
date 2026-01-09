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
__Number of tasks:__ 9<br/>
__Completed:__ 9<br/>
__Passed:__ 9<br/>

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

#### 3. Reading a file asynchronously with Node JS
Same task as above, except this time it's asynchronous and returns a promise.<br/>
See file [`3-read_file_async.js`](./3-read_file_async.js)

#### 4. Create a small HTTP server using Node's HTTP module
Create a small HTTP server using the http module. It should listen on port 1245 and display "Hello Holberton School!" in the page body for any endpoint as plain text.<br/>
See file [`4-http.js`](./4-http.js)

#### 5. Create a more complex HTTP server using Node's HTTP module
Similar to task 4, except when the URL path is `/`, it should display Hello Holberton School! in the page body. When the URL path is `/students`, it should display "This is the list of our students" followed by the content used in tasks 2 & 3.<br/>
See file [`5-http.js`](./5-http.js); remaining issue: extra blank line after listing students per field.

#### 6. Create a small HTTP server using Express
This time, to create our 'app' server (still using port 1245), we will be using Express.<br/>
See file [`6-http_express.js`](./6-http_express.js)

#### 7. Create a more complex HTTP server using Express
Similar to task 5, but using Express this time.<br/>
See file [`7-http_express.js`](./7-http_express.js)

#### 8. Organize a complex HTTP server using Express
Instead of implementing an entire server in one file, we learn how to organise it over several directories and files.<br/>
See directory [`full_server`](./full_server)