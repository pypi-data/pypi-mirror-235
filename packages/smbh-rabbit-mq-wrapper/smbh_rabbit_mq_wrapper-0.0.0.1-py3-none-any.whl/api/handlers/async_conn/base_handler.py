import asyncio
from dataclasses import dataclass
from typing import Optional

import aio_pika
from aio_pika.abc import AbstractConnection, AbstractChannel, AbstractExchange, AbstractQueue

from api.handlers.__static__ import StaticMethodsHandler


@dataclass
class RabbitMQData:
    connection: AbstractConnection
    exchange: AbstractExchange
    channel: AbstractChannel
    queue: AbstractQueue


class BaseHandler:
    url: str
    config: dict
    rabbit_mq_data: Optional[RabbitMQData]

    def __init__(self, url: str, loop: asyncio.BaseEventLoop, config: dict):
        self.url = url
        self.loop = loop
        self.config = config

    @property
    async def connection(self):
        return await aio_pika.connect(self.url, loop=self.loop)

    async def __aenter__(self):
        conn = await self.connection
        channel = await conn.channel()

        queue = await channel.declare_queue(self.config.get('queue', 'default'))
        exchange = await channel.declare_exchange(self.config.get('exchange', 'default'))

        await queue.bind(exchange=exchange, routing_key=queue.name)

        self.rabbit_mq_data = RabbitMQData(connection=conn, channel=channel, queue=queue, exchange=exchange)
        return self.rabbit_mq_data

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.rabbit_mq_data.queue.unbind(
            exchange=self.rabbit_mq_data.exchange,
            routing_key=self.rabbit_mq_data.queue.name
        )

        await self.rabbit_mq_data.connection.close()
        self.rabbit_mq_data = None
