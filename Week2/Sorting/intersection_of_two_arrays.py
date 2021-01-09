def intersection(nums1,nums2):
    nums1.sort()
    nums2.sort()
    
    intersection = []
    
    i = 0
    j = 0
    
    while (i < len(nums1) and j < len(nums2)):
        if nums1[i]  > nums2[j]:
            j += 1
        
        elif nums1[i] < nums2[j]:
            i += 1
            
        else:
            if (len(intersection) == 0) or intersection[-1] != nums1[i]:
                intersection.append(nums1[i])
                
            i += 1
            j += 1
            
    return intersection

print(intersection([1,2,2,1],[2,2]))
