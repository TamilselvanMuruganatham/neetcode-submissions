class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len=len(nums1)+len(nums2)
        nums3=[]
        i=0
        j=0
        while i <len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                nums3.append(nums1[i])
                i+=1
            else:
                nums3.append(nums2[j])
                j+=1
        while i < len(nums1):
            nums3.append(nums1[i])
            i+=1
        while j<len(nums2):
            nums3.append(nums2[j])
            j+=1

        median=  (total_len//2,(total_len//2)-1)  if total_len%2==0 else (total_len//2,)

        ans=sum(nums3[x] for x in median)
        if len(median)!=2:
            return ans
        else:
            return ans/2

