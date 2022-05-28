import requests, sched, time

# Creating an instance of the
# scheduler class
scheduler = sched.scheduler(time.time, 
                            time.sleep)

def print_event(message):
    print(message)

# time delay (second)
# priority
# function to execute
# function parameters
event_1 = scheduler.enter(1, 1, 
                     print_event, ('Event 1', ))

event_2 = scheduler.enter(10, 2, print_event, ('Event 2', ))

scheduler.run()


# Run forever, but
i = 0
while i < 10:
    print('Hello')
    time.sleep(2)
    i += 1

