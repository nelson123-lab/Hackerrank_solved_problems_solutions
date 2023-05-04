class Solution:
    def merge(self, nums1,nums2) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while nums1 and nums2:
            l, r = 0, 0
            while l< len(nums1) and r < len(nums2):
                if nums1[l] == 0:
                    nums1[l] = nums2[r]
                    r += 1
                elif nums1[l] <= nums2[r]:
                    l += 1
                else:
                    nums1.insert(l, nums2[r])
                    r += 1
            return nums1[:-1]
        
a = Solution()
print(a.merge([1,2,3,0,0,0], nums2 = [2,5,6]))

# list1 = [1,2,3, 0, 0, 0]
# list2 = [3, 4, 5, 6, 7, 8, 9]
# new = list1 + list2
# res = [i for i in new if i != 0]
# print(res)