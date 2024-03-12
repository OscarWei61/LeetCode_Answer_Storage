/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {

    if (head == null) {
        return false;
    }

    if (head.next == null || head.next.next == null) {
        return false;
    }

    let slowNode = head.next;
    let fastNode = head.next.next;

    while (slowNode != fastNode) {
        if (slowNode.next == null || fastNode.next == null) {
            return false;
        }

        slowNode = slowNode.next;
        fastNode = fastNode.next.next;

        if (slowNode == null || fastNode == null) {
            return false;
        }
    }

    return true
};