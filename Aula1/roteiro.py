import os
import sys
import time

pid=os.fork()

if pid==0:
    print('Processo filho: executando sua parte')
    sys.exit(0)
else:
    print('Processo Pai: executando sua parte')
