/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function (root) {

    // 如果為空的樹or沒有子葉了也不用做反轉
    if (root === null || (root.right === null && root.left === null)) {
        return root;
    }
    var tempNode = root.left;
    // 子葉也需要反轉
    root.left = invertTree(root.right);
    root.right = invertTree(tempNode);

    return root;

};