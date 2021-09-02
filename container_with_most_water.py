class Solution(object):
    '''
    GIVEN
    INPUT
        height: integer of non-negative integers (0 or positive)
            each represents a point at coord (i, ai)
    assume lines have minimal volume, don't have to subtract hteir volume when they are in a container
    
    example
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    height[1] = 8
    height[8] = 7
    width = 8 - 1 = 7
    height = min(height[1], height[8]) = min(8, 7) = 7
    area = height*width = 7*7 = 49
    
    brute force
    two nested loops
    get area of each combination
    see if max
    if so return
    
    optimization: two pointer approach
    start two pointers, one at 0 and another at last element
    max area as the area of that location
    
    while left is less than right:
        find the side with the shorter height
            find the next closest height with a larger height
        if better area update area
        
    return max area
    '''
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(height) - 1
        
        get_area = lambda: (right - left)*min(height[right], height[left])
        
        max_area = get_area()
        
        while left < right:
            # if the right pointer is limiting, find a better option for it
            if height[right] < height[left]:
                old_height = height[right]
                while left < right and height[right] <= old_height:
                    right -= 1
            else:
                old_height = height[left]
                while left < right and height[left] <= old_height:
                    left += 1
            max_area = max(max_area, get_area())
        
        return max_area                
                
