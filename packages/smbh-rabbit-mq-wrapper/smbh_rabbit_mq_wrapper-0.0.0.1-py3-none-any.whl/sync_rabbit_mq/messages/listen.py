"""File with an example how to use handler for read messages from RabbitMQ"""

from api.handlers.sync_conn import ReadHandler


def main():
    handler = ReadHandler(exchange='', routing_key='test')
    handler.read_messages()


if __name__ == '__main__':
    main()
