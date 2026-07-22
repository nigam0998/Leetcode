#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
private:
    struct SparseTable {
        int n;
        int k;
        vector<vector<int>> st;

        SparseTable(const vector<int>& arr) {
            n = arr.size();
            if (n == 0) return;
            
            k = log2(n) + 1;
            st.assign(k, vector<int>(n, 0));

            for (int i = 0; i < n; ++i) {
                st[0][i] = arr[i];
            }

            for (int i = 1; i < k; ++i) {
                for (int j = 0; j + (1 << i) <= n; ++j) {
                    st[i][j] = max(st[i - 1][j], st[i - 1][j + (1 << (i - 1))]);
                }
            }
        }

        int query(int l, int r) {
            if (l > r || n == 0) return 0;
            int i = log2(r - l + 1);
            return max(st[i][l], st[i][r - (1 << i) + 1]);
        }
    };

public:
    vector<int> maxActiveSectionsAfterTrade(string s, vector<vector<int>>& queries) {
        int n = s.length();
        int ones = 0;
        for (char c : s) {
            if (c == '1') ones++;
        }

        vector<pair<int, int>> zero_groups;
        vector<int> zero_group_index(n, -1);

        for (int i = 0; i < n; ++i) {
            if (s[i] == '0') {
                if (i > 0 && s[i - 1] == '0') {
                    zero_groups.back().second++;
                } else {
                    zero_groups.push_back({i, 1});
                }
            }
            zero_group_index[i] = (int)zero_groups.size() - 1;
        }

        if (zero_groups.empty()) {
            return vector<int>(queries.size(), ones);
        }

        int num_groups = zero_groups.size();
        vector<int> adjacent_sums;
        for (int i = 0; i < num_groups - 1; ++i) {
            adjacent_sums.push_back(zero_groups[i].second + zero_groups[i + 1].second);
        }

        SparseTable st(adjacent_sums);
        vector<int> ans;
        ans.reserve(queries.size());

        for (const auto& q : queries) {
            int l = q[0];
            int r = q[1];

            int g_l = zero_group_index[l];
            int g_r = zero_group_index[r];

            int left_len = 0;
            if (s[l] == '0') {
                int start_pos = zero_groups[g_l].first;
                int length = zero_groups[g_l].second;
                left_len = length - (l - start_pos);
            }

            int right_len = 0;
            if (s[r] == '0') {
                int start_pos = zero_groups[g_r].first;
                right_len = r - start_pos + 1;
            }

            int active_sections = ones;

            // Case 1: Trade within the same boundary/adjacent zero groups
            if (s[l] == '0' && s[r] == '0' && g_l + 1 == g_r) {
                active_sections = max(active_sections, ones + left_len + right_len);
            } else {
                // Fully contained adjacent zero pairs start after g_l
                int start_adj = g_l + 1;
                int end_adj = (s[r] == '1') ? g_r : g_r - 1;

                if (start_adj < end_adj) {
                    int max_adjacent = st.query(start_adj, end_adj - 1);
                    active_sections = max(active_sections, ones + max_adjacent);
                }
            }

            // Case 2: Trade combining partial boundary left zero-group + adjacent full zero-group
            if (s[l] == '0' && g_l + 1 <= ((s[r] == '1') ? g_r : g_r - 1)) {
                active_sections = max(active_sections, ones + left_len + zero_groups[g_l + 1].second);
            }

            // Case 3: Trade combining partial boundary right zero-group + adjacent full zero-group
            if (s[r] == '0' && g_l < g_r - 1) {
                active_sections = max(active_sections, ones + right_len + zero_groups[g_r - 1].second);
            }

            ans.push_back(active_sections);
        }

        return ans;
    }
};