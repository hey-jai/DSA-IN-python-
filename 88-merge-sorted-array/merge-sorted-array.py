class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # Pointers
        i = m + n - 1  # Last index of nums1
        m_ptr = m - 1  # Last valid element in nums1
        n_ptr = n - 1  # Last element in nums2
        
        # Compare from right to left
        while m_ptr >= 0 and n_ptr >= 0:
            if nums1[m_ptr] > nums2[n_ptr]:
                nums1[i] = nums1[m_ptr]
                m_ptr -= 1
            else:
                nums1[i] = nums2[n_ptr]
                n_ptr -= 1
            i -= 1
            
        # If elements are left in nums2, copy them
        while n_ptr >= 0:
            nums1[i] = nums2[n_ptr]
            n_ptr -= 1
            i -= 1
   
        