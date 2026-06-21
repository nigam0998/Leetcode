class Solution {
    public:
    int minGenerations(vector<vector<int>>& points, vector<int>& target) {
        auto encode = [](int x, int y, int z) {
            return x * 49 + y * 7 + z;
        };

        int targetCode = encode(target[0], target[1], target[2]);

        unordered_set<int> seen;
        vector<array<int,3>> all;

        for (auto &p : points) {
            int code = encode(p[0], p[1], p[2]);

            if (code == targetCode)
            return 0;

            seen.insert(code);
            all.push_back({p[0], p[1], p[2]});
        }

        if (all.size() < 2)
        return -1;

        int generation = 0;

        while (true) {
            generation++;

            vector<array<int,3>> newPoints;

            int n = all.size();

            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    if (all[i] == all[j]) continue;

                    int x = (all[i][0] + all[j][0]) / 2;
                    int y = (all[i][1] + all[j][1]) / 2;
                    int z = (all[i][2] + all[j][2]) / 2;

                    int code = encode(x, y, z);

                    if (!seen.count(code)) {
                        if (code == targetCode)

                        return generation;

                        seen.insert(code);
                        newPoints.push_back({x, y, z});
                    }
                }
            }

            if (newPoints.empty())
            return -1;

            for (auto &p : newPoints)
            all.push_back(p);

            if (seen.size() == 343)
            return -1;
        }
    }
};