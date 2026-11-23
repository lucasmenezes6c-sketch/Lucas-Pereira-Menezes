import asyncio

async def baixar_dados(site , tempo):
    (f"Iniciando download de {site}...")
    await asyncio.sleep(tempo)
    print(f"Download de {site} concluído!")

async def main():
    await asyncio.gather(
        baixar_dados("Site A", 2),
        baixar_dados("Site B", 1),
        baixar_dados("Site C", 3)
    )

asyncio.run(main())