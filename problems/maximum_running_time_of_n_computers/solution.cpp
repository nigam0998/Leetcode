class Solution {
    public:
    long long maxRunTime(int n, vector<int>& batteries) {
        long long left = 0;
        long long right = 0;

        for (int b : batteries)
        right += b;

        right /= n;

        while (left < right) {
            long long mid = (left + right + 1) / 2;

            long long power = 0;

            for (int b : batteries)
            power += min((long long)b, mid);

            if (power >= mid * n)
            left = mid;
            else
            right = mid - 1;
        }

        return left;
    }
};