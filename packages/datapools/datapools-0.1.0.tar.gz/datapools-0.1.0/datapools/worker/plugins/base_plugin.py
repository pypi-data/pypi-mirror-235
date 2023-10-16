from typing import List, Union
from urllib.parse import urlparse

import httpx

from ...common.logger import logger
from ...common.storage import BaseStorage
from ...common.types import CrawlerBackTask, CrawlerContent


class BasePlugin:
    def __init__(self, storage: BaseStorage):
        self.storage = storage

    async def download(self, url):
        try:
            async with httpx.AsyncClient(
                max_redirects=5
            ) as client:  # TODO: 5 should be parameter
                r = await client.get(
                    url, follow_redirects=True
                )  # TODO: follow_redirects should be parameter
                return r.content

        except Exception as e:
            logger.error(f"failed get content of {url}: {e}")

    def parse_url(self, url):
        return urlparse(url)

    def is_supported(self, url):
        raise Exception("not implemented")

    async def process(
        self, url
    ) -> Union[CrawlerContent, CrawlerBackTask]:  # should yield
        raise Exception("not implemented")
