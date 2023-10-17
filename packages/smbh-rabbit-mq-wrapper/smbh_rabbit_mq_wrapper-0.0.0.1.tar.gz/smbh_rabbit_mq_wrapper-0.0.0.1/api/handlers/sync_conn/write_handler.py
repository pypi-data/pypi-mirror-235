from typing import Iterable

from api.handlers.sync_conn.base_handler import BaseHandler
from sync_rabbit_mq.dataclasses import MessageContent
from config.logger import logger_listener


class WriteHandler(BaseHandler):

    def send_message(self, content: str | MessageContent):
        if isinstance(content, str):
            content = self.static_methods.create_message(body=content)

        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key=self.routing_key,
            body=self.static_methods.dump_message(content)
        )
        logger_listener.info(f"Message {content} are send")

    def send_message_collection(self, messages: Iterable[MessageContent]):
        for message in messages:
            self.send_message(message)
