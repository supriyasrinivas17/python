import time

my_time = int(input("Enter number of seconds: "))

for i in range(my_time ,0,-1):
    hours = int(i /3600)
    minutes = int(i % 60) %60
    seconds = i % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up!")
