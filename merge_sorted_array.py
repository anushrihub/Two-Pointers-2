# https://leetcode.com/problems/merge-sorted-array/



# brutforce Tc- O((m+n)log(m+n)) Sc- O(1)
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        j = 0
        for i in range(m ,m +n):
            nums1[i] = nums2[j]
            j += 1
        nums1.sort()
        return nums1

    
solution = Solution()
print(solution.merge([1,2,3,0,0,0],3,[2,5,6],3))
            