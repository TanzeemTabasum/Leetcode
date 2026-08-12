#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;

        int start_node = -1;

        // 1. Check if 'nums' is a cyclic shift of [0...n-1] (State S_i)
        // S_i is defined by nums[j] = (i + j) % n
        int potential_i = nums[0];
        bool is_Si = true;
        for (int j = 0; j < n; ++j) {
            if (nums[j] != (potential_i + j) % n) {
                is_Si = false;
                break;
            }
        }
        if (is_Si) start_node = potential_i;

        // 2. Check if 'nums' is a reversed cyclic shift (State R_k)
        // R_k is defined by nums[j] = (k - j + n) % n
        if (start_node == -1) {
            int potential_k = nums[0];
            bool is_Rk = true;
            for (int j = 0; j < n; ++j) {
                if (nums[j] != (potential_k - j + n) % n) {
                    is_Rk = false;
                    break;
                }
            }
            if (is_Rk) start_node = n + potential_k;
        }

        // If the configuration is not reachable via rotations/reflections, return -1
        if (start_node == -1) return -1;
        // If it's already sorted (S_0)
        if (start_node == 0) return 0;

        // 3. BFS on the 2n possible states
        // Nodes 0 to n-1: S_0 to S_{n-1}
        // Nodes n to 2n-1: R_0 to R_{n-1}
        queue<pair<int, int>> q;
        q.push({start_node, 0});
        
        vector<int> dist(2 * n, -1);
        dist[start_node] = 0;

        while (!q.empty()) {
            auto [u, d] = q.front();
            q.pop();

            if (u == 0) return d; // Target S_0 reached

            int next_rot, next_rev;
            if (u < n) { // Currently in state S_u
                next_rot = (u + 1) % n;           // Rotate Left
                next_rev = n + (u - 1 + n) % n;   // Reverse
            } else { // Currently in state R_k where k = u - n
                int k = u - n;
                next_rot = n + (k - 1 + n) % n;   // Rotate Left
                next_rev = (k + 1) % n;           // Reverse
            }

            for (int v : {next_rot, next_rev}) {
                if (dist[v] == -1) {
                    dist[v] = d + 1;
                    q.push({v, d + 1});
                }
            }
        }

        return -1;
    }
};