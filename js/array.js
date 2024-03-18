class Myarray {
  constructor() {
    this.length = 0;
    this.data = {};
  }

  get(index) {
    return this.data[index];
  }

  push(item) {
    this.data[this.length] = item;
    this.length++;
    return this.length;
  }
  pop() {
    const lastItem = this.data[this.length - 1];
    delete this.data[this.length - 1];
    this.length--;
    return lastItem
  }

}

let b = new Myarray();

console.log(b.push(3));
console.log(b.push("Item"));
console.log(b.pop())
console.log(b);
