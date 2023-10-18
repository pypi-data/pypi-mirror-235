import asyncio

from kelvin.app.client import KelvinApp
from kelvin.message import KRNAssetDataStream, Number


async def main() -> None:
    # Creating instance of Kelvin App Client
    app = KelvinApp()

    # Connect the App Client
    await app.connect()

    # Custom Loop
    while True:
        # Publish Data (Number) -> 50.0
        await app.publish(Number(resource=KRNAssetDataStream("<asset_name>", "<output_name>"), payload=50.0))
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
