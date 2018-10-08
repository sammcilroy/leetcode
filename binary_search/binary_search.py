class BinarySearch:
    
    def binary_search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = 0 # first index of nums
        last = len(nums)-1 # last index of nums
        
        target_found = False
        
        while first<=last and not target_found:
            mid = int((first+last)/2) # middle element of current list slice
            
            if nums[mid] == target: # if the middle element is equal to the target
                target_found = True # the target has been found
            else:
                if target < nums[mid]: # if the target is less than the middle value
                    last = mid-1 # set the last element to the previous (discard the top half of the slice)
                else:
                    first = mid+1 # else the target is greater than the middle value, 
                                  # set the first element to the element following the mid (discard the 
                                  # lower half of the list)
        if target_found:
            return nums.index(target)
        else:
            return -1

    def binary_search_recursive(self, nums, target, ofset=0):

        if len(nums) == 0:
            return -1 # Base Case, recursively call until length is 0, i.e. the target was never found
        else:
            mid = int(len(nums)/2)
            
            if nums[mid] == target:
                return nums.index(target) + ofset
            else:
                if target < nums[mid]:
                    return self.binary_search_recursive(nums=nums[:mid], target=target, ofset=ofset+len(nums[mid+1:]))
                else:
                    return self.binary_search_recursive(nums=nums[mid+1:], target=target, ofset=ofset+len(nums[:mid]))

    def search(self, nums, target, recursive=False):
        if recursive:
            return self.binary_search_recursive(nums=nums, target=target)
        else:
            return self.binary_search(nums=nums, target=target)

    
test = BinarySearch()
print(test.search(nums=[1,2,3,4,5,6,7,8,9,10], target=10, recursive=True))



