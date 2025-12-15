# ES6: data manipulation

## Requirements:
* All files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `node 20.x.x` and `npm 9.x.x`
* Allowed editors: vi, vim, emacs, Visual Studio Code
* All files should end with a new line
* Code should use the js extension
* All code will be tested using Jest and the command `npm run test`
* All code will be verified against lint using `ESLint`
* Code needs to pass all the tests and lint (verify the entire project with `npm run full-test`)
* All functions must be exported
        
## Tasks
### General information
__Number of tasks:__ 11<br/>
__Completed:__ 6<br/>
__Passed:__ TBA<br/>

### Overview
#### 0. Basic list of objects
Create function `getListStudents` that returns an array of objects. Each object should have the attributes `id` (Number), `firstName` (String), and `location` (String).<br/>
See file [`0-get_list_students.js`](./0-get_list_students.js)

#### 1. More mapping
Using the returned list from `getListStudents`, create `getListStudentIds` that returns an array of ids.<br/>
See file [`1-get_list_student_ids.js`](./1-get_list_student_ids.js)

#### 2. Filter
Using a list of students and the new function `getStudentsByLocation`, return an array of objects filtered by city.<br/>
See file [`2-get_students_by_loc.js`](./2-get_students_by_loc.js)

#### 3. Reduce
Calculate the sum of all students' IDs.<br/>
See file [`3-get_ids_sum.js`](./3-get_ids_sum.js)

#### 4. Combine
Using `map` and `filter`, update the grades of students from a specific city, setting their grade to 'N/A' is no information is passed in the arguments.<br/>
See file [`4-update_grade_by_city.js`](./`4-update_grade_by_city.js)

#### 5. Typed Arrays
The function `createInt8TypedArray` creates and returns a new `ArrayBuffer` with an `Int8` value at a specific position.<br/>
See file [`5-typed_arrays.js`](./5-typed_arrays.js)

#### 6. Set data structure
Create a function named `setFromArray` that accepts one `Array` element and returns a `Set`.<br/>
See file [`6-set.js`](./6-set.js)

#### 7. More set data structure
Create a function named `hasValuesFromArray` that accepts two arguments, a `Set` and an `Array`. It returns a boolean if all the elements in the array exist within the set.<br/>
See file [`7-has_array_values.js`](./7-has_array_values.js)

#### 8. Clean set
<br/>
See file [`8-clean_set.js`](./8-clean_set.js)

#### 9. Map data structure
Create a function named `groceriesList` that returns a map of groceries with the _name_ and _quantity_ items.<br/>
See file [`9-groceries_list.js`](./9-groceries_list.js)

#### 10. More map data structure
Creates function `updateUniqueItems` that returns an updated map. All items with initial quantity of 1 should have their quantity set to 100.<br/>
See file [`10-update_uniq_items.js`](./10-update_uniq_items.js)

