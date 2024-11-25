# Microservice A

## How to request data
  First, create JSON data containing the two dates and values for the call. The first date should be called 'date1', the second should be called 'date2'.
  The date should be ins string format as "MM-DD-YYYY".
  For the value corresponding to the first date, call it 'value1', and for the value corresponding to the second date, call it 'value 2'.
  The values should be passed as floats or integers.
  Using ZeroMQ, call send_string with the socket and pass the JSON as a parameter. Use json.dumps before passing it to convert it to string format.

  ### Socket Info
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

  ### Example Call
    data = {
      "date1": "3-1-2010",
      "date2": "3-7-2017",
      "value1": 2000,
      "value2": 5000
    }
    socket.send_string(json.dumps(data))

## How to recieve data
  After sending data, use the recv_string() function to recieve the CAGR as a string. The CAGR will be in percent format, but will not contain a percent symbol.

  ### Example Call
    cagr = socket.recv_string()
    print(f"{cagr}%")

## UML Sequence Diagram
  <img width="564" alt="image" src="https://github.com/user-attachments/assets/11010139-1869-4417-8637-9e05edabf781">

