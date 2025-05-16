# test/test_multiple_tcp_devices.py

import unittest
from devices.tcp_device import TCPDevice
import asyncio

class TestMultipleTCPDevices(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.devices = [
            TCPDevice("127.0.0.1", 9001),
            TCPDevice("127.0.0.1", 9002),
            TCPDevice("127.0.0.1", 9003)
        ]
        for device in self.devices:
            await device.connect()

    async def asyncTearDown(self):
        for device in self.devices:
            await device.close()

    async def test_multiple_device_write_and_response(self):
        for i, device in enumerate(self.devices):
            response = await device.write(f"Message from Device {i+1}")
            print(f"[Device {i+1}] Received: {response}")
            self.assertTrue(response.startswith("ACK"))

    async def test_multiple_device_independent_communication(self):
        # Each device sends a unique message and receives expected ACK
        messages = ["Alpha", "Bravo", "Charlie"]
        for device, msg in zip(self.devices, messages):
            response = await device.write(msg)
            self.assertEqual(response, f"ACK: {msg}")

if __name__ == '__main__':
    unittest.main()
