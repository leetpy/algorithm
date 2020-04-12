
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 保存已经遍历的 num: index
        sum_map = {}
        for idx, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in sum_map.keys():
                return [sum_map.get(num2), idx]
            else:
                sum_map[num1] = idx

