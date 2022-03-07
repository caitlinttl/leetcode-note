
        

import datetime
print("-----test python-----")
startdate = datetime.datetime.now()

# ------------------------------

strs = [5,5,10,10,20]
answers = [1,1,2,6,7,3,2,4,3,2,6,7,8]
ans = Solution().lemonadeChange(strs)
print(ans)

# ------------------------------

enddate = datetime.datetime.now()
print(f'Elapse of time: {enddate - startdate} ms')

