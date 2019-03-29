/* 
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.



Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
*/

class ListNode {
  constructor(val, next = null) {
    this.val = val;
    this.next = next;
  }
}

let list = new ListNode(1);
list.next = new ListNode(2);
list.next.next = new ListNode(3);
list.next.next.next = new ListNode(4);

const swapPairs = head => {
  let dummy = new ListNode(0);
  let previousNode = dummy;

  while (head && head.next) {
    let trailingNodes = head.next.next;

    previousNode.next = head.next;
    previousNode = head;

    head.next.next = head;
    head = trailingNodes;
  }

  if (head) {
    previousNode.next = head;
    head.next = null;
  } else previousNode.next = null;

  return dummy.next;
};

console.log(swapPairs(list));
