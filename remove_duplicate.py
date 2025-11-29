# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

# brutforce Tc- O(2n) Sc -O(n)
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 2
        map = {}
        result = []
        for i in nums:
            if i in map:
                map[i] += 1 
            else:
                map[i] = 1
            if map[i] <= k:
                result.append(i)
        # in this problem need not to define any extra space so arranging num list again
        for i in range(len(result)):
            nums[i] = result[i]
        return len(result)
                
        
solution = Solution()
print(solution.removeDuplicates([1,1,1,2,2,3]))
# nums = [1,1,1,2,2,3]
# output = 5