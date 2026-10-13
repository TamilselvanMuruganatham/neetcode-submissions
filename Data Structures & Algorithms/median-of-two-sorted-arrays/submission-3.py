class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        nums1_len=len(nums1)
        nums2_len=len(nums2)
        total_len=nums1_len+nums2_len

        required_candidates=[ (total_len//2)-1,total_len//2  ]   if total_len%2==0 else [total_len//2]
        len_required_candidates=len(required_candidates)
        values=0
        i=0
        j=0
        index=0
        
        while i<nums1_len and j<nums2_len and required_candidates:
            if nums1[i]<nums2[j]:
                if index==required_candidates[0]:
                    values+=nums1[i]
                    required_candidates.pop(0)
                i+=1
            else:
                if index==required_candidates[0]:
                    values+=nums2[j]
                    required_candidates.pop(0)
                j+=1
            index+=1

        while i<nums1_len and required_candidates:
            if index==required_candidates[0]:
                values+=nums1[i]
                required_candidates.pop(0)
            i+=1
            index+=1
        while j<nums2_len and required_candidates:
            if index==required_candidates[0]:
                values+=nums2[j]
                required_candidates.pop(0)
            j+=1
            index+=1
        
        return values/len_required_candidates
            


