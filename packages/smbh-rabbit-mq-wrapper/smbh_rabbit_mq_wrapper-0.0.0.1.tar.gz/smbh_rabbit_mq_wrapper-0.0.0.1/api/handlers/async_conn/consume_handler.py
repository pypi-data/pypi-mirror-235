from api.handlers.__static__ import StaticMethodsHandler
from api.handlers.async_conn import BaseHandler
from config.logger import logger_listener


class ConsumeHandler(BaseHandler, StaticMethodsHandler):
    async def consume(self):
        if self.rabbit_mq_data is None:
            raise ValueError("method ConsumeHandler.consume should be called in with context")

        logger_listener.info('Start Consume')
        async with self.rabbit_mq_data.queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process() as mess:
                    content = self.load_message(mess.body)
                    logger_listener.info(f"{content} are read")
