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

var middleNode = function (head) {
    let workHead = head;
    // 紀錄開頭以方便回到head
    let listLen = 0
    while (workHead != null) {
        workHead = workHead.next;
        listLen = listLen + 1;
    }

    const middleIndex = Math.floor(listLen / 2)

    workHead = head;
    let currentIndex = 0;
    while (currentIndex < middleIndex) {
        workHead = workHead.next;
        currentIndex = currentIndex + 1;
    }

    return workHead;
};