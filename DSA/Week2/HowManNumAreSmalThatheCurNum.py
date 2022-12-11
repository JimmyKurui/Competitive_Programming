class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        i=0; countArr=0;
        for i in range(len(nums)):
            j=i+1; 
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    countArr[i].append()
        return countArr        