# TCP/IP Device Communication 
# 🔌 TCP/IP Device Communication 

This project is designed for a **manufacturing plant** environment where multiple devices need to be connected using different communication protocols (starting with TCP/IP). It supports reading and writing data in real-time across devices using IP and Port configurations.

---

## ✅ Features

- ✅ TCP/IP communication using IP address & port
- ✅ Communicate with **multiple devices simultaneously**
- ✅ Easily extendable for future protocols (like MQTT, Modbus, HTTP)
- ✅ TCP/IP **stub server** for local testing
- ✅ Unit tests to validate communication logic

---

## Requirements

- Python 3.8+
- pip


## 🚀 How to Run the Project

## Step 1: Start TCP Stub Servers (Simulating Devices)

In **separate terminal windows**, start one stub per device:

```bash
# Terminal 1
python stub/tcp_stub_server.py 9001

# Terminal 2
python stub/tcp_stub_server.py 9002

# Terminal 3
python stub/tcp_stub_server.py 9003
```

## Step 2: Run the Main Application

```bash
python main.py
```

## Step 3: Run Unit Tests

```bash
python -m unittest discover test
```

## Add a New Protocol

To support a new protocol, inherit from `BaseDeviceProtocol` in `devices/base_protocol.py`.
