class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        # self. लगाना जरूरी है
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        # डॉट हटाया और self. लगाया
        return self.merge(left, right)
        
    # self आर्गुमेंट जोड़ा
    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            # len[i] को left[i] किया
            if left[i] <= right[j]:
                # let[i] को left[i] किया
                result.append(left[i])
                i += 1
            else:
                # result[j] को right[j] किया
                result.append(right[j])
                j += 1
                
        result.extend(left[i:])
        result.extend(right[j:])
        return result
          