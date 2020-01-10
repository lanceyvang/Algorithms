class Node {
	constructor(value) {
		this.value = value;
		this.nextnode = null;
	}
}

const reverse = head => {
	let current = head;
	let nextnode,
		previous = null;

	while (current) {
		[nextnode, current.next] = [current.next, previous];
		[previous, current] = [current, nextnode];
	}
	return previous;
};

const a = new Node(1);
const b = new Node(2);
const c = new Node(3);
const d = new Node(4);

a.nextnode = b;
b.nextnode = c;
c.nextnode = d;

// console.log(a);
// const x = reverse(a);
// console.log(x);

const nth = (head, n) => {
	let left = head;
	let right = head;

	while (n--) {
		right = right.nextnode;
	}

	while (right.nextnode) {
		right = right.nextnode;
		left = left.nextnode;
	}
	return left;
};

nth(a, 1);
