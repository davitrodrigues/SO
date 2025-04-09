import os 
import sys
for i in range(5):
    pid=os.fork()

    if pid==0:
        print('FILHO')
        sys.exit(5)
    else:
        os.wait()
        print('pai')