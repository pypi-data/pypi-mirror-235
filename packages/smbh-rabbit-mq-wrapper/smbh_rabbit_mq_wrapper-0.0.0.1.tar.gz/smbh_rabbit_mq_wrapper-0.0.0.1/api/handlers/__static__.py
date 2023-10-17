import pickle

from pika import BasicProperties

from sync_rabbit_mq.dataclasses import MessageType, MessageContent
from config.logger import logger_listener


class StaticMethodsHandler:
    @staticmethod
    def create_message(body: str = "", mess_type: str = MessageType.info) -> MessageContent:
        return MessageContent(body=body, type=mess_type)

    @staticmethod
    def load_message(content: bytes) -> MessageContent:
        return pickle.loads(content)

    @staticmethod
    def dump_message(mess: MessageContent) -> bytes:
        return pickle.dumps(mess)

    def on_message_middleware(self, channel, method, properties: BasicProperties, body):
        content = self.load_message(body)
        # logger_listener.info(f"Message routing_key={method.routing_key} are read")

        match content.type:
            case MessageType.info:
                self.on_message_info(method, properties, content)
            case MessageType.action:
                self.on_message_action(method, properties, content)

        channel.basic_ack(method.delivery_tag)

    @staticmethod
    def on_message_info(method, properties: BasicProperties, content: MessageContent):
        logger_listener.info(f'Message with tag "info" are read {content}')

    @staticmethod
    def on_message_action(method, properties: BasicProperties, content: MessageContent):
        logger_listener.info(f'Message with tag "action" are read {content}')
