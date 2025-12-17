# ES6 - Promises

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
__Number of tasks:__ 10<br/>
__Completed:__ 10<br/>
__Passed:__ 10<br/>

### Overview
#### 0. Keep every promise you make and only make promises you can keep
Return a Promise using prototype function `getResponseFromAPI()`.<br/>
See file [`0-promise.js`](./0-promise.js)

#### 1. Don't make a promise...if you know you can't keep it
The function `getFullResponseFromAPI(success)`, which takes a Boolean parameter, returns a promise depending on the value of `success`.<br/>
If `success` is `true`, the promise is resolved by passing `{status: 200, body: 'Success'}`. Otherwise, the promise is rejected with an error object and the message "_The fake API is not working currently_".
See file [`1-promise.js`](./1-promise.js)

#### 2. Catch me if you can!
Append three handlers to function `handleResponseFromAPI(promise)`: one for `Promise.resolve()`, one for `Promise.reject()`, and a console.log "_Got a response from the API_" for every resolution.<br/>
See file [`2-then.js`](./2-then.js)

#### 3. Handle multiple successful promises
Using functions `uploadPhoto` and `createUser` from `utils.js` (a provided file), resolve the returned promises through the function `handleProfileSignup()`. This function logs return body of the resolved promises to the console, or "_Signup system offline_" if an error occurs.<br/>
See file [`3-all.js`](./3-all.js)

#### 4. Simple promise
The function `signUpUser(firstName, lastName)` returns a resolved promise with object `{ firstName: value, lastName: value }`.<br/>
See file [`4-user-promise.js`](./4-user-promise.js)

#### 5. Reject the promises
Create the function `uploadPhoto` which accepts one argument: `fileName` (string). The function should return a `Promise` rejecting with an `Error` and the string "_$fileName cannot be processed_"<br/>
See file [`5-photo-reject.js`](./5-photo-reject.js)

#### 6. Handle multiple promises
Function `handleProfileSignup` calls `signUpUser` ([4-user-promise.js](./4-user-promise.js)) and `uploadPhoto` ([5-photo-reject.js](./5-photo-reject.js)), passing them its own string arguments (`firstName`, `lastName` and `fileName`). It then returns an array in the following format:
```
[
    {
      status: status_of_the_promise,
      value: value or error returned by the Promise
    },
    ...
  ]
```
See file [`6-final-user.js`](./6-final-user.js)

#### 7. Load balancer
The function `loadBalancer` accepts two Promise arguments (`chinaDownload` and `USDownload`) and returns the value of the first Promise to resolve.<br/>
See file [`7-load_balancer.js`](./7-load_balancer.js)

#### 8. Throw an error
`divideFunction` accepts two Number arguments, `numerator` and `denominator`. When `denominator` is 0, throw a new error with the message "_cannot divide by 0_". Otherwise return the numerator divided by the denominator.<br/>
See file [`8-try.js`](./8-try.js)

#### 9. Throw error / try catch
Function `guardrail` accepts one Function argument, `mathFunction`, and returns an array `queue`.<br/>
Upon execution of `mathFunction`, append the returned value to the queue –even if it's an error message– as well as the message "_Guardrail was processed_". Example:
```
[
  1000,
  'Guardrail was processed',
]
```
See file [`9-try.js`](./9-try.js)