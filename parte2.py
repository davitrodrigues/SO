import os
import sys
import time

pid=os.fork()
if pid==0:
    pid2=os.fork()
    if pid2==0:
        time.sleep(2)
        print('Neto: executando')
        sys.exit(0)
    else:
        os.wait()
        time.sleep(2)
        print('Filho: finalizando após o neto')
        sys.exit(0)
else:
    os.wait()
    time.sleep(2)
    print('PAI: todos os processos finalizaram')