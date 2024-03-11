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
 * @return {number}
 */
var maxDepth = function (root) {

    return findNode(root);

    function findNode(node) {
        if (node == null) {
            return 0;
        }

        var nodeLeftDepth = 1;
        var nodeRightDepth = 1;

        if (node.left != null) {
            nodeLeftDepth = nodeLeftDepth + findNode(node.left);
        }

        if (node.right != null) {
            nodeRightDepth = nodeRightDepth + findNode(node.right);
        }

        if (nodeLeftDepth > nodeRightDepth) {
            return nodeLeftDepth;
        } else {
            return nodeRightDepth;
        }
    }
};