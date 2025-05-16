import asyncio
from devices.base_protocol import BaseDeviceProtocol

class TCPDevice(BaseDeviceProtocol):
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port
        self.reader = None
        self.writer = None

    async def connect(self):
        self.reader, self.writer = await asyncio.open_connection(self.ip, self.port)

    async def read(self) -> str:
        data = await self.reader.readline()
        return data.decode().strip()

    async def write(self, message: str) -> str:
        self.writer.write((message + "\n").encode())
        await self.writer.drain()
        data = await self.reader.readline()
        return data.decode().strip()

    async def close(self):
        self.writer.close()
        await self.writer.wait_closed()

