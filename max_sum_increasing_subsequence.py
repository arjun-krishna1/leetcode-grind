'''
# Link: https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/
## Self-feedback
- I didn't come up with the algorithm myself
- But I was able to implement the algorithm into code after watching video but before looking at code
  - Coming up with the algorithm is the hard part
  - I could do the easy part but not the hard part
  - I need to be able to come up with the algorithm myself
- Why didn't I come up with the algorithm?
  - I didn't think about it in a Dynamic Programming kind of way
## How to think in Dynamic Programming:
- how can this complex problem be broken down into simpler subproblems which are easier to solve?
  - are there overlapping simpler sub-problems (things that are recalculated over and over?)
  - are you optimizing something where the optimal total solution can be obtained by using the optimal solutions of its subproblems?
  - e.g. the increasing subsequence of an entire array (complex problem)
    - optimizing maximum sum of subsequence
    - you want maxSumIncreasingSubsequence(arr) <- this is the complex problem
    - simpler subproblem is maxSumIncreasingSubsequence(arr[:-1])
    - given answer to simpler subproblem to maxSumIncreasingSubsequence(arr[:-1])
    - if the last element of that subsequence is less than arr[-1] add arr[-1] to the greatest subsequence and its sum
    - else iterate through arr[:-i] until you find a subsequence that could include arr[-1]
    - i.e. where arr[-i] < arr[-1]
    - return subsequence and max sum of result(arr[:-i]) + arr[-1] or just result(arr[:-1])
'''

def maxSumIncreasingSubsequence(arr):
	# hold the max sum, and its subsequence of each 
	# entry in array
    sums = [[i, [i]] for i in arr]
	# hold the entry with the greatest subsequence sum
	res = sums[0]
	
	# consider each entry in arr as a part of the greatest subsequence
	for i in range(len(arr)):
		# consider adding the entry to all possible subsequences
		# already generated
		for j in range(i):
			# get the new sum if this entry is added to this subsequence
			new_sum = sums[j][0] + arr[i]
			
			# this element can be added to the subsequence
			# and it results in a greater subarray sum
			if arr[i] > arr[j] and new_sum > sums[i][0]:
				# update this entry with new sum and subarray
				sums[i] = [
							new_sum,
							sums[j][1] + [arr[i]]
						  ]
				
		# this sum is greater than the previous result's sum
		if sums[i][0] > res[0]:
			res = sums[i]
		
	# return the subsequence with the greatest total sum
	return res
