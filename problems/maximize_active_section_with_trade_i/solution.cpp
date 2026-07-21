#include <string>
#include <vector>
#include <algorithm>
class Solution {
public:
    int maxActiveSectionsAfterTrade(std::string s) {
        int n = s.length();
        int total_ones = 0;
        std::vector<std::pair<char, int>> segments;
        int i = 0;
        while (i < n) {
            int j = i;
            while (j < n && s[j] == s[i]) {
                j++;
            }
            if (s[i] == '1') {
                total_ones += (j - i);
            }
            segments.push_back({s[i], j - i});
            i = j;
        }
        int ans = total_ones;
        int m = segments.size();
        for (int k = 1; k < m - 1; k++) {
            if (segments[k].first == '1' && segments[k - 1].first == '0' && segments[k + 1].first == '0') {
                int left_zeros = segments[k - 1].second;
                int right_zeros = segments[k + 1].second;
                ans = std::max(ans, total_ones + left_zeros + right_zeros);
            }
        }
        return ans;
    }
};