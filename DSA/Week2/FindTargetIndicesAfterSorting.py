class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        indexArray = []
        count = [index for (index, num) in enumerate(sorted(nums)) if num == target]
        return count
            