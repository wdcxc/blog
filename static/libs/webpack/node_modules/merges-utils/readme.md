# merge-utils
## Install
```bash
$ npm install merges-utils
```
## Usage
### right values cover left
```javascript
var merge = require('merges-utils')
var a = {
    'a': 123, 'b': 456,
    'c': {
        'd': [123, 34],
        'e': { 'f': 123, 'g': true }
    },
    'd': true
}
var b = {
    'a': 998, 'b': 466,
    'c': {
        'd': [133, 35],
        'e': { 'f': 126, 'g': false }
    }
}
var c = {
    'd': false,
}
var res = merge([a, b, c])
console.log(res)
/* result:
{ a: 998, b: 466,
  c: { d: [ 133, 35 ], e: { f: 126, g: false } },
  d: false }
 */
```
### diy merge method
```javascript
var merge = require('merges-utils')
var a = {
    'a': 123, 'b': 456,
    'c': {
        'd': [123, 34],
        'e': { 'f': 123, 'g': true }
    },
    'd': true
}
var b = {
    'a': 998, 'b': 466,
    'c': {
        'd': [133, 35],
        'e': { 'f': 126, 'g': false }
    }
}
var c = {
    'd': false,
}
var res = merge([a, b, c], {
    'a': true,
    'c': {
        'd': true
    }
})
console.log(res)
/*
{ a: 123, b: 466,
  c: { d: [ 123, 34 ], e: { f: 126, g: false } },
  d: false }
 */
```
### n-level always keep former values
```javascript
var merge = require('merges-utils')
var a = {
    'a': 123, 'b': 456,
    'c': {
        'd': [123, 34],
        'e': { 'f': 123, 'g': true }
    },
    'd': true
}
var b = {
    'a': 998, 'b': 466,
    'c': {
        'd': [133, 35],
        'e': { 'f': 126, 'g': false }
    }
}
var c = {
    'd': false,
}
var res = merge([a, b, c], {}, 2)
console.log(res)
/*
{ a: 123, b: 456,
  c: { d: [ 123, 34 ], e: { f: 123, g: true } },
  d: true }
 */
```
```javascript
var merge = require('merges-utils')
var a = {
    'a': 123, 'b': 456,
    'c': {
        'd': [123, 34],
        'e': { 'f': 123, 'g': true }
    },
    'd': true
}
var d = {
    'c': {
        'e': {'f': 126, 'g': false}
    }
}
var res = merge([a, d], {
    'c': {
        'e': { 'g': true },
        'd': true
    }
},2)
console.log(res)
/*
{ a: 123,
  b: 456,
  c: { d: [ 123, 34 ], e: { f: 126, g: true } },
  d: true }
 */
```
### others
```javascript
var merge = require('../lib/index.js')
var res = merge([{'a': {'b': 1, 'd': {'e': 12}}}, {'a': {'c': 1, 'd': 12}}] )
console.log(res);
/*
{ a: { b: 1, d: { e: 12 }, c: 1 } }
 */
```
## options
```javascript
function merge([obj1, obj2, ...],{
    'key1': true,
    /*
    Keep the leftmost value
    example:
    var res = merge([{'a': 100}, {'a': 200}], { 'a': true })
    result:
    {'a': 100}
    */
    'key2': false,
    /*
    Keep the rightmost value.
    example:
    var res = merge([{'a': 100}, {'a': 200}], { 'a': false})
    or
    var res = merge([{'a': 100}, {'a': 200}])
    result:
    {'a': 200}
    */
},
level
/*
    Keep the left value of the previous n layer
    Option exception
    example:
    var res1 = merge([{'a': 100, 'b': {'c': 1}}, {'a': 200, 'b': {'c': 2}}], {}, 1)
    var res2 = merge([{'a': 100, 'b': {'c': 1, 'd': 1}}, {'a': 200, 'b': {'c': 2, 'd': 2}}], {'b': { 'c': false}}, 1)
    result:
    res1 = { 'a': 100, 'b': { 'c': 1}}
    res2 = { 'a: 100, 'b': { 'c': 2, d: 2 } }
*/
)
```
