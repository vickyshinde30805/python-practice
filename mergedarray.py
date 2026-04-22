from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    # Merge both arrays
    marray = nums1 + nums2
    
    # Sort the merged array
    marray.sort()
    
    r = len(marray)
    
    # Even length
    if r % 2 == 0:
        mid1 = marray[r//2 - 1]
        mid2 = marray[r//2]
        return (mid1 + mid2) / 2
    
    # Odd length
    else:
        return marray[r//2]


# 🔹 Driver Code (for VS Code)
if __name__ == "__main__":
    nums1 = list(map(int, input("Enter nums1 elements: ").split()))
    nums2 = list(map(int, input("Enter nums2 elements: ").split()))
    
    result = findMedianSortedArrays(nums1, nums2)
    print("Median:", result)