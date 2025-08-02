from collections import Counter

class Solution(object):
    def minCost(self, basket1, basket2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        total = count1 + count2
        for fruit, freq in total.items():
            if freq % 2 != 0:
                return -1
        swap_from_basket1 = []
        swap_from_basket2 = []

        for fruit in total:
            diff = count1[fruit] - count2[fruit]
            if diff > 0:
                swap_from_basket1.extend([fruit] * (diff // 2))
            elif diff < 0:
                swap_from_basket2.extend([fruit] * (-diff // 2))
        swap_from_basket1.sort()
        swap_from_basket2.sort(reverse=True)
        global_min = min(min(basket1), min(basket2))
        total_cost = 0

        for a, b in zip(swap_from_basket1, swap_from_basket2):
            total_cost += min(min(a, b), 2 * global_min)

        return total_cost
