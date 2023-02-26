import asyncio

import server.server_main as server
import client.client_main as client
import sys

def main():
    if '-S' in sys.argv or '--server' in sys.argv:
        asyncio.run(server.run_server())
    elif '-C' in sys.argv or '--client' in sys.argv:
        asyncio.run(client.run_client())
    else:
        # No flag provided
        choice = input('Run client or server? (C/S): ')
        if choice.lower() == 'c':
            asyncio.run(client.run_client())
        elif choice.lower() == 's':
            asyncio.run(server.run_server())
        else:
            print('Invalid choice, enter C or S\nExiting...')

if __name__ == '__main__':
    main()