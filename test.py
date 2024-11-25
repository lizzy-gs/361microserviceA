import zmq as z
import json
import time

context = z.Context()
socket = context.socket(z.REQ)
socket.connect("tcp://localhost:5555")

data = {
    "date1": "3-1-2010",
    "date2": "3-7-2017",
    "value1": 2000,
    "value2": 5000
}

print("Sending JSON")
socket.send_string(json.dumps(data))
time.sleep(1)
print("Receiving...")
cagr = socket.recv_string()
print(f"Received CAGR: {cagr}%")