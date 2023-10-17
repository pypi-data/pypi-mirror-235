import asyncio

from api.handlers.async_conn.publish_handler import PublishHandler


async def example(_loop):
    handler = PublishHandler(
        url="amqp://guest:guest@localhost:55001/", loop=_loop, config={
            "queue": "some_queue", "exchange": "some_exchange",
        }
    )

    async with handler:
        await handler.publish_collection((f"message_{i + 1}" for i in range(10)))


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(example(loop))
    loop.close()
