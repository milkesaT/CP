class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def count_waviness_up_to(X: int) -> int:
            if X < 100:
                return 0
            
            s = str(X)
            n = len(s)
            
            # Memoization table: (idx, p1, p2, is_tight, is_zero) -> (total_valid_numbers, total_waviness)
            memo = {}
            
            def dp(idx, p1, p2, is_tight, is_zero):
                # Base case: if we placed all digits, we return (1 valid number, 0 waviness from remaining positions)
                if idx == n:
                    return 1, 0
                
                state = (idx, p1, p2, is_tight, is_zero)
                if state in memo:
                    return memo[state]
                
                limit = int(s[idx]) if is_tight else 9
                total_numbers = 0
                total_waviness = 0
                
                for d in range(limit + 1):
                    next_tight = is_tight and (d == limit)
                    
                    if is_zero and d == 0:
                        # Case 1: Still trailing leading zeros
                        cnt, wav = dp(idx + 1, -1, -1, next_tight, True)
                        total_numbers += cnt
                        total_waviness += wav
                    else:
                        # Case 2: Placed a valid non-zero digit
                        # Check if the previous digit (p1) is a peak or a valley relative to p2 and current digit d
                        is_peak_or_valley = 0
                        if p2 != -1 and p1 != -1:
                            if (p2 < p1 > d) or (p2 > p1 < d):
                                is_peak_or_valley = 1
                        
                        cnt, wav = dp(idx + 1, d, p1, next_tight, False)
                        
                        total_numbers += cnt
                        # Total waviness = waviness of suffixes + (waviness added by p1 * number of suffixes)
                        total_waviness += wav + (is_peak_or_valley * cnt)
                
                memo[state] = (total_numbers, total_waviness)
                return memo[state]
            
            return dp(0, -1, -1, True, True)[1]
        
        # Principle of inclusion-exclusion (prefix sum method)
        return count_waviness_up_to(num2) - count_waviness_up_to(num1 - 1)
