class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            j=-1
            try:
                j = nums.index(target - nums[i],i+1)
            except:
                pass
            if(j!=-1):
                return [i,j]
        