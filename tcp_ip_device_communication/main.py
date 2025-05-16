# main.py
import asyncio
from devices.tcp_device import TCPDevice

async def communicate_with_device(ip: str, port: int):
    device = TCPDevice(ip, port)
    try:
        await device.connect()
        await device.write("Hello")
        response = await device.read()
        print(f"[{ip}:{port}] Received: {response}")
        await device.close()
    except Exception as e:
        print(f"[{ip}:{port}] Error: {e}")

async def main():
    # List of multiple unique devices with different IP and Port
    devices = [
        ("127.0.0.1", 9001),
        ("127.0.0.1", 9002),
        ("127.0.0.1", 9003)
    ]
    
    tasks = [
        communicate_with_device(ip, port)
        for ip, port in devices
    ]
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
