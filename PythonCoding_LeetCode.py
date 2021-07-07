class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        Given an n x n matrix where each of the rows and columns are sorted in ascending order, 
        return the kth smallest element in the matrix.
        Note that it is the kth smallest element in the sorted order, 
        not the kth distinct element.
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Overall: O(k * len(matrix)) = O(nk)
        kth_smallest = 0
        while k > 0:
            curr_smallest_matrix = [matrix[i][0] for i in range(len(matrix))] # smallest of each smallest inside the big matrix ==> O(len(matrix))
            kth_smallest = min(curr_smallest_matrix)
            indx = curr_smallest_matrix.index(kth_smallest)
            del matrix[indx][0] # remove that smallest
            if (len(matrix[indx]) == 0):
                del matrix[indx] # the if statement is b/c [[], [10, 11, 13], [12, 13, 15]]
            k -= 1
            #print(matrix)
        return kth_smallest
