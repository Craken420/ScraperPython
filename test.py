import asyncio
from scraper import scrap_amazon_affiliate

async def main():
    productos = await scrap_amazon_affiliate()
    print("Productos encontrados:")
    for p in productos:
        print("-", p)

asyncio.run(main())
