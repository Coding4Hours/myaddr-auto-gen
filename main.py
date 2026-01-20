import asyncio
import zendriver as zd
from wonderwords import RandomWord

r = RandomWord()

IP = input("IP: ")
NUM_LINKS = int(input("How many links: "))


async def create_link(browser, index):
    NAME = f"{r.word()}123"

    page = await browser.get("https://myaddr.tools/claim")

    search_box = await page.select("input[id='name-input']")
    await search_box.send_keys(NAME)

    await asyncio.sleep(3)
    button = await page.select("button[type='submit']")
    await button.click()

    await asyncio.sleep(1)
    text_field = await page.select("#key-input")
    key_text = await text_field.apply("el => el.value")

    await page.get(f"https://myaddr.tools/update?key={key_text}&ip={IP}")

    print(
        f"https://{NAME}.myaddr.tools\nhttps://{NAME}.myaddr.io\nhttps://{NAME}.myaddr.dev"
    )


async def main():
    browser = await zd.start()

    try:
        for i in range(NUM_LINKS):
            print(f"{i + 1}/{NUM_LINKS}")
            await create_link(browser, i)

    except Exception as e:
        print(e)
    finally:
        await browser.stop()


if __name__ == "__main__":
    asyncio.run(main())
