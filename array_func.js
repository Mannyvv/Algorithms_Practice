const nums = [1, 2, 3, 4, 5]


// Performs a function on each element and returns new array
console.log("Map Function: ", nums.map((item) => item + 2))

// Reduces array to a single element and returns it with a start 
console.log("Reduce Function: ", nums.reduce((accumlator, item) => accumlator + item))

// Reduces array to a single element and returns it with a start
console.log("Reduce Function with start: ", nums.reduce((accumlator, item) => accumlator + item, 20))

// Returns new array with elements that pass(return true) an assertion
console.log("Filter Function: ", nums.filter(item => item < 5))

// Run a function for each item in the array, but not on the item itself
//Note console.log returns undefined
console.log("forEach Function: ", nums.forEach(item => console.log("Hi")))

const nums2 = [[0, 1], [2, 1], [4, 5]]

// Reduces array to a single object and returns it, but starts from the right(end of array)
console.log("Reduce Right Function: ", nums2.reduceRight((accumlator, item) => accumlator.concat(item)))

//Returns true if A single element in array passes(returns true) an assertion, otherwise false
console.log("Some Function: ", nums.some((item) => item / 4 == 1))

//Returns true if EVERy single element in array passes(returns true) an assertion, otherwise false
console.log("Every Function: ", nums.every((item) => {
    console.log(typeof item)
    return typeof item == "number"
}))
