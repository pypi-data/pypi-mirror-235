import asyncio
import traceback
from hashlib import md5
from typing import List

import httpx
from bs4 import BeautifulSoup

from ....common.logger import logger
from ....common.types import (
    CrawlerBackTask,
    CrawlerContent,
    DatapoolContentType,
)
from ..base_plugin import BasePlugin


class ImageshackPlugin(BasePlugin):
    def __init__(self, storage):
        super().__init__(storage)

    def is_supported(self, url):
        u = self.parse_url(url)
        logger.info(f"imageshack {u=}")
        return u.netloc == "imageshack.com"

    async def process(self, url) -> CrawlerContent:
        logger.info(f"imageshack::process({url})")
        async with httpx.AsyncClient() as client:
            logger.info(f"loading url {url}")

            r = await client.get(url)
            # logger.info( f'got Response {r}')
            r = r.text
            # logger.info( f'text: {r}')
            logger.info(f"got url content length={len(r)}")

            soup = BeautifulSoup(r, "html.parser")

            # 1.search for photo LINKS and return them as new tasks
            links = soup.body.find_all("a", attrs={"class": "photo"})

            for l in links:
                yield CrawlerBackTask(url="https://imageshack.com" + l["href"])

            # 2. search for photo IMAGES
            img = soup.find("img", attrs={"id": "lp-image"})
            if img:
                logger.info(f'found image {img["src"]}')

                url = "https://imageshack.com" + img["src"]
                content = await self.download(url)
                if content:
                    storage_id = md5(url.encode()).hexdigest()

                    try:
                        await self.storage.put(storage_id, content)

                        # TODO: test only, should be parsed instead
                        tag_id = "0d085523-cd77-42b4-9e6f-4a5643d53385"

                        yield CrawlerContent(
                            tag_id=tag_id,
                            type=DatapoolContentType.Image,
                            storage_id=storage_id,
                            url=url,
                        )
                    except Exception as e:
                        logger.error(f"failed put to storage {e}")
                        logger.error(traceback.format_exc())

                    await asyncio.sleep(2)

                else:
                    logger.error(f"failed download image")

    # async def imageshack_plugin():
    #     #try:
    #         q = CrawlerUrlsQuery(
    #             filter = CrawlerUrlsFilter(processed_datetime = 0),
    #             sort = [SortOrder(name = 'datetime')]
    #         )
    #         while( True ):
    #             await asyncio.sleep(2)

    #             urls = await bck.datapools_db.get_crawler_urls( q )
    #             for u in urls:
    #                 if u[ 'url' ].lower().find( 'https://imageshack.com/' ) != -1:
    #                     logger.info( f'parsing imageshack url {u["url"]}')
    #                     parsed_urls = await parse_imageshack_url( u[ 'url' ] )

    #                     logger.info( f'{parsed_urls=}')
    #                     tags = await bck.openlicense_tags_db.select( OpenlicenseTagSelectQuery(filter=OpenlicenseTagFilter(user_id=str(u[ 'user_id']) )))
    #                     tag_id = tags[0]['id']

    #                     #mark url as processed
    #                     await bck.datapools_db.update_crawler_url( u[ 'id' ], {'processed_datetime': time.time() } )

    #                     for url in parsed_urls:
    #                         await bck.datapools_db.add_crawled_content({
    #                             'datapool_id': 1,    #imageshack
    #                             'tag_id': tag_id,
    #                             'url': url,
    #                             'content': '',  #TODO: image title?
    #                             'media': DatapoolContentsType.Image,
    #                             'nsfw': False,
    #                             'meta': {}, #TODO: image size?
    #                             'score': 0.5,
    #                             'weight': 0.5,
    #                             'incentive': 100
    #                         })
    #                 else:
    #                     logger.info( 'not imageshack url, skipped')
    #     #except Exception as e:
    #         #logger.error( f'Exception in pseudo_imageshack_crawler: {e}')
