import asyncio
from playwright.async_api import async_playwright
import auto_tag.rt_operations as ops
from auto_tag.ticket import Ticket
import time


async def main():
    start = time.time()
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page1 = await context.new_page()
        # read username and password from credentials.txt
        with open("credentials.txt", "r") as f:
            username = f.readline().strip()
            password = f.readline().strip()
        await ops.login(page1, username, password)
        ids = await ops.get_tickets(page1)
        tasks = []
        for id in ids:
            page = await context.new_page()
            ticket = Ticket(id, page)
            task = asyncio.create_task(ticket.scan())
            tasks.append(task)
        res = await asyncio.gather(*tasks)
        print(res)
    end = time.time()
    print(f'Time used: {end - start}')


if __name__ == '__main__':
    asyncio.run(main())