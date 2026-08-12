class Solution(object):
    def passwordStrength(self, password):
        """
        :type password: str
        :rtype: int
        """
        strength = 0
        seen = set()
        
        for ch in password:
            
            # Count each distinct character only once
            if ch not in seen:
                seen.add(ch)
                
                if 'a' <= ch <= 'z':
                    strength += 1
                
                elif 'A' <= ch <= 'Z':
                    strength += 2
                
                elif '0' <= ch <= '9':
                    strength += 3
                
                elif ch in "!@#$":
                    strength += 5
        
        return strength