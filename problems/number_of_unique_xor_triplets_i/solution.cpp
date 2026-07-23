class Solution {
    public:
    int uniqueXorTriplets(vector<int>& nums) {
        int n = nums.size();
        if (n < 3) return n;
        int k = static_cast<int>(log2(n)) + 1;
        return 1 << k;
    }
};