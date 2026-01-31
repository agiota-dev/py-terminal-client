import asyncio
import json
import websockets
from ui import print_note, console
from time import sleep

class NostrClient:
    def __init__(self, relays):
        self.relays = relays
        self.index = 1
        self.tasks = []
    
    async def getting_notes(self, relay_url):
        try:
            async with websockets.connect(relay_url) as ws:
                console.print(f"[bold cyan]Connected to {relay_url}[/bold cyan]")

                await ws.send(
                    json.dumps([
                        "REQ",
                        "subid1",
                        {"kinds": [1]}
                    ])
                )

                async for msg in ws:
                    try:
                        data = json.loads(msg)
                        if data[0] == "EVENT":
                            event = data[2]
                            if event["kind"] == 1:
                                content = event["content"]
                                if content:
                                    print_note(self.index, content)
                                    self.index += 1
                                    sleep(2)
                    except Exception:
                        continue
        except Exception as e:
            console.print(f"[red]Error connecting to {relay_url}: {e}[/red]")

    async def start(self):
        self.tasks = [self.getting_notes(url) for url in self.relays]
        await asyncio.gather(*self.tasks)