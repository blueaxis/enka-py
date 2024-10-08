import asyncio

from enkanetwork import EnkaNetworkAPI

client = EnkaNetworkAPI(debug=True)

async def main():
    client.set_assets_repository("blueaxis/enka-data")
    async with client:
        await client.update_assets()

asyncio.run(main())
