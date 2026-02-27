sec = input("Enter seconds: ")

intsecs = int(sec)

if(intsecs < 0):
    print("time can't be smaller than 0 seconds")
    quit();

hours = intsecs // 3600
minutes = (intsecs % 3600) // 60
seconds = intsecs % 60
print(str(intsecs)+ " seconds is " + str(hours) + " hours, " + str(minutes) + " minutes, and " + str(seconds) + " seconds")

