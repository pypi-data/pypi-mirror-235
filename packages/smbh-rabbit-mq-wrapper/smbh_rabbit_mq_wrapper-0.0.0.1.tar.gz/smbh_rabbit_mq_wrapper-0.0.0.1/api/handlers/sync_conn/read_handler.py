from api.handlers.sync_conn.base_handler import BaseHandler
from config.logger import logger_listener


class ReadHandler(BaseHandler):
    def read_messages(self):
        self.channel.basic_consume(
            on_message_callback=self.static_methods.on_message_middleware,
            queue=self.routing_key
        )
        try:
            self.channel.start_consuming()
        except Exception as err:
            self.channel.stop_consuming()
            with logger_listener.catch():
                raise err
