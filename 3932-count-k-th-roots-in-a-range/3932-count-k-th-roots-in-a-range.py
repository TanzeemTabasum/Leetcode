class Solution(object):
    def countKthRoots(self, l, r, k):
        """
        :type l: int
        :type r: int
        :type k: int
        :rtype: int
        """
        # Edge case: everything is a 1st power
        if k == 1:
            return max(0, r - l + 1)
            
        # Helper function to find the largest integer x such that x^k <= target
        def floor_kth_root(target):
            if target < 0:
                return -1
            if target == 0:
                return 0
                
            # Initial boundaries using an approximate power estimate
            low = 0
            high = int(target ** (1.0 / k)) + 2 
            ans = 0
            
            while low <= high:
                mid = (low + high) // 2
                if mid ** k <= target:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return ans

        # Count = (roots up to r) - (roots up to l - 1)
        right_count = floor_kth_root(r)
        left_count = floor_kth_root(l - 1)
        
        return max(0, right_count - left_count)