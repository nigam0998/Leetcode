class Solution {
    public:
    int tilt = 0;
    int sum(TreeNode* root) {
        if (root == NULL)
        return 0;

        int left = sum(root->left);
        int right = sum(root->right);

        tilt += abs(left - right);

        return left + right + root->val;
    }

    int findTilt(TreeNode* root) {
        sum(root);
        return tilt;
    }
};