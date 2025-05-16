"""
Asyncio läuft immer nur auf einem Thread!
Es gibt einen asynchronen Loop

aiohttp
"""

import requests
import asyncio
import aiohttp


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("Status:", response.status)
            html = await response.text()
            print(html)


async def count(sleeptime):
    print("----:", sleeptime)
    await asyncio.sleep(sleeptime)
    # requests.get("http://example.com")
    print("----:", sleeptime)


async def main():
    """Haupt-Coroutine"""
    await asyncio.gather(count(4), count(1), count(1))
    print("Corotinen sind durch")


if __name__ == "__main__":
    asyncio.run(main())
