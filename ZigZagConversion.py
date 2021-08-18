class Solution:
    """
    https://leetcode.com/problems/zigzag-conversion/
    GIVEN
        INPUT
            s: string
            numRows: int
            
        OUTPUT
            input is a zigzag pattern
            output is just left to right
    """
    def convert(self, s: str, numRows: int) -> str:            
        if len(s) <= numRows or numRows == 1:
            return s

        tip_dist = 2*numRows - 2

        row = 0

        res = ''

        while row < numRows:
            if row != 0 and row != numRows - 1:
                steps = (tip_dist - 2*row, 2*row)
            else:
                steps = (tip_dist, tip_dist)

            step_idx = 0

            loc = row

            while loc < len(s):
                res += s[loc]
                loc += steps[step_idx]

                if step_idx == 1:
                    step_idx = 0
                else:
                    step_idx = 1

            row += 1

        return res
            
        
