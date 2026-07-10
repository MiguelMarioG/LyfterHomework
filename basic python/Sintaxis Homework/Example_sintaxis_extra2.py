time_sec = 0
total_sec = 0

time_sec = int(input("Enter the time in seconds: "))

if(time_sec < 600):
    total_sec = 600 - time_sec
    print (f"the remaining time in seconds to reach 10 minutes is {total_sec}")
elif(time_sec == 600):
    print (f"The time in seconds of {time_sec} is equivalent to 10 minutes.")
elif(time_sec > 600):
    print (f"The time in seconds of {time_sec} is bigger then 10 minutes.")
