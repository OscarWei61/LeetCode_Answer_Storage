/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function (head) {
    if (head == null) {
        return head;
    }

    if (head.next == null) {
        return head;
    }

    newListNode = new ListNode(0);
    var newListHead = newListNode
    while (head != null && head.next != null) {
        prev = head;
        currrentNode = head.next;
        if (head.next.next == null) {
            nextDealNode = null;
        } else {
            nextDealNode = head.next.next;
        }
        prev.next = nextDealNode;
        currrentNode.next = prev;
        newListHead.next = currrentNode;
        head = head.next;
        newListHead = newListHead.next.next;
    }

    return newListNode.next;
};