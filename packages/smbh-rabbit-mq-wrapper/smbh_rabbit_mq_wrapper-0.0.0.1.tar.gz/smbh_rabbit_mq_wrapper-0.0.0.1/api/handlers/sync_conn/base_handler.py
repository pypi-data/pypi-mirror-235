import os

import pika
from pika.adapters.blocking_connection import BlockingChannel

from api.handlers.__static__ import StaticMethodsHandler


class BaseHandler:
    channel: BlockingChannel
    exchange: str
    routing_key: str

    rmq_url_connection_str = f'amqp://{os.environ.get("RMQ_USER")}:{os.environ.get("RMQ_PASS")}@' \
                             f'{os.environ.get("RMQ_HOST")}:{os.environ.get("RMQ_PORT")}/'

    rmq_parameters = pika.URLParameters(rmq_url_connection_str)
    rmq_connection = pika.BlockingConnection(rmq_parameters)

    # create field to override in children classes (if it will be necessary)
    static_methods: StaticMethodsHandler = StaticMethodsHandler()

    def __init__(self, routing_key, exchange=''):
        self.exchange = exchange
        self.routing_key = routing_key

        self.channel = self.rmq_connection.channel()
        self.channel.queue_declare(queue=self.routing_key)
