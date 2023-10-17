"""File with an example how to use handler for write messages to RabbitMQ"""
from api.handlers.__static__ import StaticMethodsHandler
from api.handlers.sync_conn import WriteHandler


def main():
    messages = (
        StaticMethodsHandler.create_message(body=f"message_{i + 1}")
        for i in range(10)
    )
    handler = WriteHandler(exchange='', routing_key='test')
    handler.send_message_collection(messages)


if __name__ == '__main__':
    main()
