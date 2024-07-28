"""
1.) start -> on click by default
2.) state subject time
3.) store in file

"""

while(True):
    task=input("Enter Task:")
    if (task =="q"):
        break
    time=input("Time Slot:")
    f1 = open("Tasks.txt","a")
    f1.write(f"{task} - {time}\n")
    f1.close()
