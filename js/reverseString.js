function reverse(str){
    if (!str || str.length < 2 || typeof str !== 'string'){
        return 'Invalid input';
    }
    strArray = str.split('');
    let reverseArray = [];
    for (let i = strArray.length; i > 0;i--){
        reverseArray.push(strArray[i-1]);
    }
    return reverseArray.join('');
}

console.log(reverse("Hello World!")); 