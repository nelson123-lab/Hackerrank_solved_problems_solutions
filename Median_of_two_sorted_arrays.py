def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        if length %2 != 0:
            return sorted(nums1+nums2)[(length//2)]
        else:
            return (sorted(nums1+nums2)[(length//2)-1] + sorted(nums1+nums2)[(length//2)])/2
