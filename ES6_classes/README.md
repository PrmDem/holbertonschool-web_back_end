# ES6: classes

## Requirements
* All files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `node 20.x.x` and `npm 9.x.x`
* Allowed editors: vi, vim, emacs, Visual Studio Code
* All files should use the `js` extension and end with a new line
* Code will be tested using Jest and the command `npm run test`
* Code will be verified against lint using ESLint
* Code needs to pass all the tests and lint. The entire project can be verified with `npm run full-test`.

## Tasks
### General information
__Number of tasks:__ 11<br/>
__Completed:__ 11<br/>
__Passed:__ 10<br/>

### Overview
#### 0. You used to attend a place like this at some point
Implement a class named `ClassRoom` with the prototype `export default class ClassRoom`. It should accept one attribute named `maxStudentsSize` (Number) and assigned to `_maxStudentsSize`<br/>
See file [`0-classroom.js`](./0-classroom.js)
#### 1. Let's make some classrooms
Implement a function named initializeRooms. It should return an array of 3 ClassRoom objects with the sizes 19, 20, and 34 (in this order).<br/>
See file [`1-make_classrooms.js`](./1-make_classrooms.js)
#### 2. A Course, Getters, and Setters
Using `getters` and `setters`, create the class `HolbertonCourse` that takes arguments `name` (str), `length` (number), and `students` (array of strings). The type of input must be verified for all three attributes, which will be stored in the `_<attr>` format.<br/>
See file [`2-hbtn_course.js`](./2-hbtn_course.js)
#### 3. Methods, static methods, computed methods names..... MONEY
Implements the `Currency` class with two string constructor attributes: `code` and `name`. The type of input must be verified for all three attributes, which will be stored in the `_<attr>` format. `Getters` and `setters` must be used for attributes implementation. A method named `displayFullCurrency` will return the attributes in the following format: `name (code)`.<br/>
See file [`3-currency.js`](./3-currency.js)
#### 4. Pricing
Implement class `Pricing` with constructor attributes `amount` (Number) and `currency` (Currency), in the same way as the Currency class (which will be imported).<br/>
Implement method `displayFullPrice` that returns the attributes in the format `amount currency_name (currency_code)`.
Implement a static method named `convertPrice`, accepting two number arguments: `amount` and `conversionRate`. It should return the amount multiplied by the conversion rate.<br/>
See file [`4-pricing.js`](./4-pricing.js)
#### 5. A Building
Similarly to the previous tasks, implement the class `Building`, with Number constructor attribute `sqft`. Classes extended from `Building` should implement a method named `evacuationWarningMessage`. If they do not, an error should be thrown with the message `"Class extending Building must override evacuationWarningMessage"`.<br/>
See file [`5-building.js`](./5-building.js)
#### 6. Inheritance
Implement a class named `SkyHighBuilding` that extends from `Building` and override the `evacuationWarningMessage` method.<br/>
See file [`6-sky_high.js`](./6-sky_high.js)
#### 7. Airport
Implements class `Airport` with string constructor attributes `code` and `name`. The default string description of the class should be the airport's `code`.<br/>
See file [`7-airport.js`](./7-airport.js)
#### 8. Primitive - Holberton Class
Implement class `HolbertonClass` with constructor attributes `size` (number) and `location` (string). When the class is cast into a number it returns `size`, and when cast into a string it returns `location`.<br/>
See file [`8-hbtn_class.js`](./8-hbtn_class.js)
#### 9. Hoisting
Fix the provided code so that it properly displays a list of students.<br/>
See file [`9-hoisting.js`](./9-hoisting.js)
#### 10. Vroom
Implement a class `Car` with string constructor attributes `brand`, `motor`, and `color`. Add method `cloneCar` that returns a new object of the class.<br/>
See file [`10-car.js`](./10-car.js)