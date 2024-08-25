import numpy
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        nums=[]
        while j!=len(nums2) and i!=len(nums1):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i+=1
            else:
                nums.append(nums2[j])
                j+=1
        while i!=len(nums1):
            nums.append(nums1[i])
            i+=1
        while j!=len(nums2):
            nums.append(nums2[j])
            j+=1
        return float(numpy.median(nums))
        
        