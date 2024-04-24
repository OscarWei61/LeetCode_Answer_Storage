/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
var removeElements = function (head, val) {

    if (head === null) {
        return head;
    }

    tempNode = new ListNode();
    tempNode.next = head;
    currentNode = tempNode;

    while (currentNode !== null && currentNode.next != null) {
        if (currentNode.next.val == val) {
            currentNode.next = currentNode.next.next;
        } else {
            currentNode = currentNode.next;
        }
    }

    return tempNode.next;
};