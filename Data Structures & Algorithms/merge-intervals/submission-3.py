class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        if not intervals:
            return []


        intervals.sort(key = lambda x:x[0])


        st = []
        st.append(intervals[0])

        for i in range(1 , len(intervals)):

            if st[-1][1] >= intervals[i][0]:
                st[-1][1] = max(st[-1][1] , intervals[i][1])
            else:
                st.append(intervals[i])

        return st