def merge_lists(nums1, m, nums2, n):
    pointerNum1:int = m-1
    pointerNum2:int = n-1
    for index in range (len(nums1)-1, -1, -1):
        if (pointerNum1 < 0):
            nums1[index] = nums2[pointerNum2]
            pointerNum2 -= 1
        elif (pointerNum2 < 0):
            nums1[index] = nums1[pointerNum1]
            pointerNum1 -= 1
        elif (nums1[pointerNum1] >= nums2[pointerNum2]):
            nums1[index] = nums1[pointerNum1]
            pointerNum1 -= 1
        elif (nums1[pointerNum1] < nums2[pointerNum2]):
            nums1[index] = nums2[pointerNum2]
            pointerNum2 -= 1
    return nums1

# Arrays de prueba 1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
response = merge_lists(nums1, m, nums2, n)
print(response)

# Arrays de prueba 2
nums1 = [1,2,3,0,0,0,0]
m = 3
nums2 = [-4,2,3,9]
n = 4
response = merge_lists(nums1, m, nums2, n)
print(response)