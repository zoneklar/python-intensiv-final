"""
Asyncio läuft immer nur auf einem Thread!
Es gibt einen asynchronen Loop

aiohttp
"""

import asyncio
import aiohttp


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("Status:", response.status)
            html = await response.text()
            print(html)


if __name__ == "__main__":
    asyncio.run(download("https://python.org"))  # Eventloopo
