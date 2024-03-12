/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
    if (list1 == null && list2 == null) {
        return list1;
    }

    if (list1 == null && list2 != null) {
        return list2;
    }

    var headNewList = new ListNode(0);
    var newList = headNewList;

    while (list1 != null && newList != null && list2 != null) {

        if (parseInt(list1.val) < parseInt(list2.val)) {
            newList.next = list1;
            list1 = list1.next;
        } else {
            newList.next = list2;
            list2 = list2.next;
        }
        newList = newList.next;
    }

    if (list2 == null) {
        newList.next = list1;
    }

    if (list1 == null) {
        newList.next = list2;
    }

    return headNewList.next;
};
