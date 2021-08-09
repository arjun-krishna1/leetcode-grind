# https://leetcode.com/problems/triangle-judgement/
SELECT x, y, z,
    # use triangle inequality theorem
    # if the sum of any two line segments is always greater than the third line segment
    # in a set of three line segments
    # the three line segments can form a triangle
    IF(
        x + y > z AND
        y + z > x AND
        z + x > y,
        "Yes",
        "No"
    ) AS triangle
FROM triangle;
