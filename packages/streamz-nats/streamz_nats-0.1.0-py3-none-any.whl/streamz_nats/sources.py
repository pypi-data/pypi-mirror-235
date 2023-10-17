"""
Create custom streamz sources.

Classes:

    from_nats
"""
from ast import Call
import asyncio
import logging
import time
import weakref
from typing import Union, Callable

import nats
from numpy import isin
from py import log
from streamz import Stream, Source
from tornado import gen


@Stream.register_api(staticmethod)
class from_nats(Source):  # pylint: disable=C0103
    """ Accepts messages from nats

    Examples
    --------
    >>> import nats
    >>> from streamz import Stream
    >>> s = Stream.from_nats(
    ...     'nats://localhost:6650',
    ...     ['my-topic'],
    ...     subscription_name='my-sub'
    ...     )
    >>> decoder = s.map(lambda x: x.decode())
    >>> L = decoder.sink_to_list()
    """
    def __init__(
            self,
            service_url: Union[str, list[str]],
            topics: Union[str, list[str]],
            callback: Union[Callable, None] = None,
            poll_interval=0.1,
            **kwargs):
        self.service_url = service_url
        if isinstance(topics, list):
            self.topics: str = '|'.join(topics)
        else:
            self.topics = topics
        if callback is None:
            callback = self._process_message
        self._cb = self._process_message
        self.poll_interval = poll_interval

        super().__init__(**kwargs)

    async def _process_message(self, message):
        self.emit(message.data.decode(), asynchronous=True)

    async def _run(self):
        # # Opt 1. With coroutine
        # #  Will not return any message until max_msgs is reached
        # while True:
        #     try:
        #         self.consumer = await self.client.subscribe(self.topics, max_msgs=5)
        #         # print(self.consumer.next_msg())
        #         tasks = [self._cb(msg)
        #                 async for msg in self.consumer.messages]
        #         # These three options seems to be equivalent, not sure which is best
        #         # await asyncio.gather(*tasks, return_exceptions=True)
        #         # Should raise timeout error wen all the tasks are not gathered in time
        #         # await asyncio.wait_for(asyncio.gather(*tasks, return_exceptions=True), timeout=self.poll_interval)
        #         # Should not raise timeout error and split the tasks into done and pending
        #         await asyncio.wait(tasks, timeout=self.poll_interval)
        #         logging.info("done")
        #     except asyncio.TimeoutError:
        #         logging.info("timeout")
        #         break
        # # Opt 2.a Without coroutine in while loop
        # #  Will return messages if they arrive in time
        # self.sub = await self.client.subscribe(
        #                 self.topics,
        #                 cb=self._cb)
        # await asyncio.sleep(self.poll_interval)
        # # Will deliver remaining messages
        # await self.sub.drain()
        # # # Will not deliver remaining messages
        # # await self.sub.unsubscribe()
        # # logging.info("done")
        # Opt 3. Synchronous
        async for msg in self.sub.messages:
            await self._cb(msg)
            await asyncio.sleep(self.poll_interval)
      
    async def run(self):
        self.client = await nats.connect(self.service_url)
        # # Opt 2.b Without coroutine out of loop - will return all messages
        # self.sub = await self.client.subscribe(
        #                 self.topics,
        #                 cb=self._cb)
        # while not self.stopped:
        #     await asyncio.sleep(self.poll_interval)
        # # Opt 2.a Without coroutine in while loop
        # while not self.stopped:
        #     await self._run()
        # Opt 3. Synchronous
        self.sub = await self.client.subscribe(self.topics)
        while not self.stopped:
            await self._run()

    # TODO: drain client on stop
    # async def _stop(self):
    #     await self.sub.unsubscribe()
    #     await self.client.drain()
        
    # def stop(self):
    #     """set self.stopped, which will cause polling to stop after next run"""
    #     if not self.stopped:
    #         asyncio.run(self._stop())
    #         self.stopped = True
