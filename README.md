# Python-socket-messaging-protocol

Python-socket-messaging-protocol is a simple Messaging protocol i wrote to help people learn how sockets work


# Installation

you can install Python-socket-messaging-protocol by writing the folowing command:

```bash
git clone https://github.com/xxhmode14/Python-socket-messaging-protocol.git
```
# Usage

to start the server, first get in the same directory as the python script and then write the folowing command:

```bash
python3 server.py
```
if that didn't work type this
```bash
python server.py
```

---------------------------------------


to connect into a server you need to change the script a litle bit.
see the bit where it say

```python
ip_addr = "127.0.0.1" # the server public ip address or keep it as is for a local server
port = 8888
```
change the ip_addr var to the server ip address and the port to the server port.

then, run this command:
```bash
python3 connect.py
```
if that didn't work type this
```bash
python connect.py
```

***if you want to close your current connection DO NOT exit out of the termenal because that will throw an error in the server side***

# note

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

