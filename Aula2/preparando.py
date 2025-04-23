import os 

SERVER_FIFO = "/tmp/rpc_req_fifo"
CLIENT_FIFO = f"/tmp/rpc_resp_{os.getpid()}"

if os.path.exists(SERVER_FIFO):
    os.remove(SERVER_FIFO)
os.mkfifo(SERVER_FIFO, mode=0o600) # 0o600 = octal para atribuir permissões
if os.path.exists(CLIENT_FIFO):
    os.remove(CLIENT_FIFO)
os.mkfifo(CLIENT_FIFO, mode=0o600)

with open(SERVER_FIFO, "w") as server:
    server.write(f"{CLIENT_FIFO}|multiplicacao|4,7\n")
    server.flush()


with open(CLIENT_FIFO, "r") as response:
    result = response.readline().strip()
 # você deve alterar aqui para adicionar a lógica da operação
    print("Resultado da operação:", result)