import os
import sys
import threading
fifo_A_to_B = "fifo_A_to_B"
fifo_B_to_A = "fifo_B_to_A"
role = sys.argv[1] if len(sys.argv) > 1 else None
if role not in ["A", "B"]:
    print("Usage: python chat.py [A|B]")
    sys.exit(1)
if not os.path.exists(fifo_A_to_B):
    os.mkfifo(fifo_A_to_B)
if not os.path.exists(fifo_B_to_A):
    os.mkfifo(fifo_B_to_A)
if role == "A":
    input_fifo = fifo_B_to_A
    output_fifo = fifo_A_to_B
else:
    input_fifo = fifo_A_to_B
    output_fifo = fifo_B_to_A
def read_messages():
    with open(input_fifo, "r") as fifo_in:
        while True:
            line = fifo_in.readline()
            if not line:
                continue
            if line.strip() == "exit":
                print("\nPeer has exited. Exiting chat.")
                s._exit(0)
                print("\nPeer:", line.strip())
reader_thread = threading.Thread(target=read_messages, daemon=True)
reader_thread.start()
with open(output_fifo, "w") as fifo_out:
    while True:
        message = input("You: ")
        fifo_out.write(message + "\n")
        fifo_out.flush()
        if message.strip() == "exit":
            break