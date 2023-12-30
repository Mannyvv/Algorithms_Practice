const array = [1, 2, 3, 4, 5]


console.log("Map Function: ", array.map((item) => item + 2))

console.log("Reduce Function: ", array.reduce((accumlator, item) => accumlator + item))
console.log("Reduce Function with start: ", array.reduce((accumlator, item) => accumlator + item, 20))
console.log("Filter Function: ", array.filter(item => item < 5))