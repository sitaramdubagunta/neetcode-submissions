class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        st = []
        

        intervals.sort(key = lambda x:x[1])
        st.append(intervals[0])
        cnt = 0
        for i in range(1 , len(intervals)):
            

            if  st[-1][1] > intervals[i][0]:

                cnt += 1
                

            else:
                st.append(intervals[i])


        return cnt
                