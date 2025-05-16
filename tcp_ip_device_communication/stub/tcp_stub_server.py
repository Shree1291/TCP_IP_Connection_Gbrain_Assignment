# stub/tcp_stub_server.py
import asyncio
import sys

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Connection from {addr}")

    try:
        while True:
            data = await reader.read(100)
            if not data:
                break
            message = data.decode()
            print(f"Received from {addr}: {message}")
            response = f"ACK: {message}"
            writer.write(response.encode())
            await writer.drain()
    except ConnectionResetError:
        print(f"Connection lost with {addr}")
    finally:
        writer.close()
        await writer.wait_closed()

async def main(port):
    server = await asyncio.start_server(handle_client, '127.0.0.1', port)
    print(f"Stub TCP server running at ('127.0.0.1', {port})")
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9000
    asyncio.run(main(port))
