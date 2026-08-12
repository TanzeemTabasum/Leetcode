class Solution(object):
    def smallestUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Large prime numbers to avoid hash collisions
        MOD = 2**63 - 1
        BASE = 100003  # Should be greater than max value in nums (10^5)

        def has_unique_subarray_of_length(length):
            # Compute the hash value of the first window of given length
            current_hash = 0
            base_power = 1
            
            for i in range(length):
                current_hash = (current_hash * BASE + nums[i]) % MOD
                if i > 0:
                    base_power = (base_power * BASE) % MOD
            
            # Map to store hash frequencies and their first seen ending index
            # to double check against true collisions if necessary
            hash_counts = {}
            hash_counts[current_hash] = 1
            
            # Record hashes for all other sliding windows of this length
            hash_sequence = [current_hash]
            
            for i in range(length, n):
                # Slide the window: remove the oldest element, add the new element
                current_hash = (current_hash - nums[i - length] * base_power) % MOD
                current_hash = (current_hash * BASE + nums[i]) % MOD
                current_hash = (current_hash + MOD) % MOD # Handle negative values safely
                
                hash_counts[current_hash] = hash_counts.get(current_hash, 0) + 1
                hash_sequence.append(current_hash)
            
            # Check if any subarray hash appeared exactly once
            for h in hash_sequence:
                if hash_counts[h] == 1:
                    return True
            return False

        # Binary search for the minimum possible unique subarray length
        low = 1
        high = n
        ans = n
        
        while low <= high:
            mid = (low + high) // 2
            if has_unique_subarray_of_length(mid):
                ans = mid       # mid is a valid length, try to find a smaller one
                high = mid - 1
            else:
                low = mid + 1   # mid is too small, look for larger lengths
                
        return ans