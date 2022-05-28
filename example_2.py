# Asynchronous
import time
from timeloop import Timeloop
from datetime import timedelta

#timeloop

tl = Timeloop()

@tl.job(interval=timedelta(seconds=5))
def sample_job_every_5s():
    print ("5s job current time : {}".format(time.ctime()))

tl.start()

i = 0
while i < 10:
    print('Hello')
    time.sleep(2)
    i += 1

# Runs on the main thread every second to check if there's a keyboard interrupt
while True:
  try:
    time.sleep(1)
  except KeyboardInterrupt:
    tl.stop()
    break

