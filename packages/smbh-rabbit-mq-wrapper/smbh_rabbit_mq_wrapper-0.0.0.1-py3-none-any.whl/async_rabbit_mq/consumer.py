import asyncio

from api.handlers.async_conn.consume_handler import ConsumeHandler


async def example(_loop):
    handler = ConsumeHandler(
        url="amqp://guest:guest@localhost:55001/", loop=_loop, config={
            "queue": "some_queue", "exchange": "some_exchange",
        }
    )

    async with handler:
        await handler.consume()

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(example(loop))
    loop.close()
