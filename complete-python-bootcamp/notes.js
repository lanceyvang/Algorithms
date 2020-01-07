class Node {
    constructor(value){
        this.value = value;
        this.next = null;
    }
}

let reverse = (head) => {
    let current = head;
    let nextnode = null;
    let previous = null;

    while (current) {
        [nextnode,current.next] = [current.next,previous];
        [previous,current] = [current,nextnode];
    }
    return previous;
};

let a = new Node(1)
let b = new Node(2)
let c = new Node(3)

a.next = b
b.next = c

console.log(a)
const x = reverse(a)
console.log(x)