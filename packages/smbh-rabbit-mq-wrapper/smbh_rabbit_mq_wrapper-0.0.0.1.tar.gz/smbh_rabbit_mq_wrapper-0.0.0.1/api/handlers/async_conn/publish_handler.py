from typing import Iterable, Union

import aio_pika

from api.handlers.__static__ import StaticMethodsHandler
from api.handlers.async_conn import BaseHandler
from config.logger import logger_listener
from sync_rabbit_mq.dataclasses import MessageContent


class PublishHandler(BaseHandler, StaticMethodsHandler):
    async def publish(self, content: str | MessageContent):
        if self.rabbit_mq_data is None:
            raise ValueError("method ConsumeHandler.consume should be called in with context")

        if isinstance(content, str):
            content = self.create_message(body=content)

        await self.rabbit_mq_data.exchange.publish(
            message=aio_pika.Message(
                body=self.dump_message(content)
            ), routing_key=self.rabbit_mq_data.queue.name
        )
        logger_listener.info(f"{content} are send")

    async def publish_collection(self, messages: Iterable[Union[MessageContent, str]]):
        if self.rabbit_mq_data is None:
            raise ValueError("method ConsumeHandler.consume should be called in with context")

        for message in messages:
            await self.publish(message)
