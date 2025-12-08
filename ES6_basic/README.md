# ES6: basics

## Requirements
* Files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `node 20.x.x` and `npm 9.x.x`
* Allowed editors: vi, vim, emacs, Visual Studio Code
* All files should end with a new line
* Code should use the `js` extension
* Code will be tested using `Jest Testing Framework`
* Code will be analyzed using linter `ESLint` and provided specifics
* All functions must be exported

## Tasks
### General information
__Number of tasks:__ 13<br/>
__Completed:__ 12<br/>
__Passed:__ TBA<br/>

### Overview
#### 0. Const or let?
Given two functions that use 'var' variables, replace with 'const' and 'let' appropriately.<br/>
See file [`0-constants.js`](./0-constants.js)

#### 1. Block Scope
Modify the variables inside a provided function `taskBlock` so they don't get overwritten.<br/>
See file [`1-block-scoped.js`](./1-block-scoped.js)

#### 2. Arrow functions
Rewrite a provided function to use ES6’s arrow syntax.<br/>
See file [`2-arrow.js`](./2-arrow.js)

#### 3. Parameter defaults
Condense the internals of a provided function to 1 line without changing any names.<br/>
See file [`3-default-parameter.js`](./3-default-parameter.js)

#### 4. Rest parameter syntax for functions
Using `rest parameter syntax`, modify the provided function to return the number of arguments passed to it.<br/>
See file [`4-rest-parameter.js`](./4-rest-parameter.js)

#### 5. The wonders of spread syntax
Using `spread syntax`, concatenate 2 arrays and each character of a string by adding one line the provided function.<br/>
See file [`5-spread-operator.js`](./5-spread-operator.js)

#### 6. Take advantage of template literals
Rewrite the return statement to use a template literal to substitute the defined variables.<br/>
See file [`6-string-interpolation.js`](./6-string-interpolation.js)

#### 7. Object property value shorthand syntax
Modify the provided function’s `budget` object to use the `value` shorthand syntax.<br/>
See file [`7-getBudgetObject.js`](./7-getBudgetObject.js)

#### 8. No need to create empty objects before adding in properties
Rewrite the provided function to use ES6 computed property names on the returned object.<br/>
See file [`8-getBudgetCurrentYear.js`](./8-getBudgetCurrentYear.js)

#### 9. ES6 method properties
Rewrite the provided function to use method properties.<br/>
See file [`9-getFullBudget.js`](./9-getFullBudget.js)

#### 10. For...of Loops
Rewrite the provided function to use ES6’s `for...of` operator.<br/>
See file [`10-loops.js`](./10-loops.js)

#### 11. Iterator
Write the function `createEmployeesObject(departmentName, employees)` where `departmentName` is a string and `employees`and array of strings.<br/>
The function should return an object with the following format:
```
{
     $departmentName: [
          $employees,
     ],
}
```
See file [`11-createEmployeesObject.js`](./11-createEmployeesObject.js)

#### 12. Let's create a report object
Using the return from `createEmployeesObject`, new function `createReportObject` should return an object containing the key `allEmployees` and a method property called `getNumberOfDepartments`.<br/>
`allEmployees` is a key that maps to an object containing the department name and a list of all the employees in that department.<br/>
See file [`12-createReportObject.js`](./12-createReportObject.js)
