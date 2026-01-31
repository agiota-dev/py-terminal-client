import asyncio
from client import NostrClient
from relays import RELAY_URLS
from ui import console


async def main():
    client = NostrClient(RELAY_URLS)

    try:
        await client.start()
    except KeyboardInterrupt:
        console.print("\n[bold red]Saindo...[/bold red]")
        await asyncio.sleep(0.1)

if __name__ == "__main__":
    asyncio.run(main())