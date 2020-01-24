class Node {
	constructor(value) {
		this.value = value;
		this.nextnode = null;
	}
}

// const reverse = head => {
// 	let current = head;
// 	let nextnode,
// 		previous = null;

// 	while (current) {
// 		[nextnode, current.next] = [current.next, previous];
// 		[previous, current] = [current, nextnode];
// 	}
// 	return previous;
// };

// const a = new Node(1);
// const b = new Node(2);
// const c = new Node(3);
// const d = new Node(4);

// a.nextnode = b;
// b.nextnode = c;
// c.nextnode = d;

// console.log(a);
// const x = reverse(a);
// console.log(x);

// const nth = (head, n) => {
// 	let left = head;
// 	let right = head;

// 	while (n--) {
// 		right = right.nextnode;
// 	}

// 	while (right.nextnode) {
// 		right = right.nextnode;
// 		left = left.nextnode;
// 	}

// 	console.log(left.value);
// 	console.log(right.value);
// 	return left;
// };

// nth(a, 1);

// const reverse = head => {
// 	let current = head;
// 	let previous = null;
// 	let next = null;

// 	while (current) {
// 		// 1
// 		// 2
// 		// 3
// 		next = current.nextnode; // saves the original order so we can traverse
// 		// next = 2
// 		// next = 3
// 		// next = null
// 		current.nextnode = previous; // builds new order
// 		// 1.nextnode = null
// 		// 2.nextnode = 1.null
// 		// 3.nextnode = 2.1.null
// 		previous = current; // sets previous to the new order we're building
// 		// previous = 1.null
// 		// previous = 2.1.null
// 		// previous = 3.2.1.null
// 		current = next; // changes what we're looking at to the next node in original list
// 		// current = 2
// 		// current = 3
// 		// current = null
// 	}
// 	return previous;
// };

// reverse(a);

class DoubleLinkedListNode {
	constructor(value) {
		this.value = value;
		this.next = null;
		this.previous = null;
	}
}

// let a = new DoubleLinkedListNode(1);
// let b = new DoubleLinkedListNode(2);
// let c = new DoubleLinkedListNode(3);

// a.next = b;
// b.previous = a;
// b.next = c;
// c.previous = b;

// console.log('pokemon');
// console.log(a);

const sumOfParts = n => {
	n_str = n.toString();

	if (n_str.length == 1) {
		return +n_str;
	}

	return +n_str.slice(0, 1) + sumOfParts(n_str.slice(1));
};

const reverse = s => {
	if (s.length === 1) {
		return s;
	}
	return s.slice(-1) + reverse(s.slice(0, -1));
};

// console.log(reverse('abc'));
