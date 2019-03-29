/*
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Could you do this in one pass?
*/

class ListNode {
  constrictor(val) {
    this.val = val;
    this.next = null;
  }
}

let list = new ListNode(1);
list.next = new ListNode(2);
list.next.next = new ListNode(3);

const removeNthFromEnd = (head, n) => {
  const preHead = { next: head };

  let left = preHead;
  let right = head;

  while (n--) right = right.next;

  while (right) {
    left = left.next;
    right = right.next;
  }
  left.next = left.next.next;

  return preHead.next;
};

console.log(removeNthFromEnd(list, 1));
