import os

r,w=os.pipe()
pid=os.fork()
if pid ==0:
    os.close(w)
    data=os.read(r,12)
    print(f'Filho recebeu: {data.decode()}')
    os.close(r)
else:
    os.close(r)
    os.write(w,b"Mensagem do pai para filho")
    os.close(w)