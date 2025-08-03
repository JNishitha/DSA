class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        """
        :type fruits: List[List[int]]
        :type startPos: int
        :type k: int
        :rtype: int
        """
        n = len(fruits)
        maxFruits = 0
        total = 0
        left = 0

        for right in range(n):
            total += fruits[right][1]
            while left <= right:
                left_pos = fruits[left][0]
                right_pos = fruits[right][0]
                min_steps = min(
                    abs(startPos - left_pos) + (right_pos - left_pos),  
                    abs(startPos - right_pos) + (right_pos - left_pos)  
                )

                if min_steps <= k:
                    break
                total -= fruits[left][1]
                left += 1

            maxFruits = max(maxFruits, total)

        return maxFruits