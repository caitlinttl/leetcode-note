




import datetime
print("-----test python-----")
startdate = datetime.datetime.now()

# ------------------------------

answers = [1,1,2,6,7,3,2,4,3,2,6,7,8]
ans = Solution().numRabbits(answers)
print(ans)

# ------------------------------

enddate = datetime.datetime.now()
print(f'Elapse of time: {enddate - startdate} ms')

