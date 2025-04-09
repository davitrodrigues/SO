import os 
import sys
import time
for i in range(5):
    pid=os.fork()

    if pid==0:
        print(i+6)
        sys.exit(5)
    else:
        print(i+1)
        time.sleep(1)
        os.wait()
        
        