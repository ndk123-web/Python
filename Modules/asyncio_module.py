import asyncio

async def fetch():
    print('Fetching ......')
    await asyncio.sleep(2)
    print('Fetched Data')

async def process():
    print('Processing...')
    await asyncio.sleep(1)
    print('Processed')

async def main():
    ans = await asyncio.gather(fetch(),process())

asyncio.run(main())