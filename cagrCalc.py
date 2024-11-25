import zmq as z
import json
from datetime import date, datetime

context = z.Context()
socket = context.socket(z.REP)
socket.bind("tcp://*:5555")

while True:

    print("Waiting for message...")
    message = socket.recv_string()
    data = json.loads(message)
    print("JSON received, calculating CAGR...")

    date1 = data.get("date1")
    date2 = data.get("date2")
    startValue = data.get("value1")
    endValue = data.get("value2")

    parsedDate1 = datetime.strptime(date1, "%m-%d-%Y").date()
    parsedDate2 = datetime.strptime(date2, "%m-%d-%Y").date()

    diff = parsedDate2 - parsedDate1
    numDays = diff.days

    cagr = round((((endValue / startValue) ** (365 / numDays)) - 1) * 100, 2)

    print(f"Sending {cagr}%")
    socket.send_string(str(cagr))