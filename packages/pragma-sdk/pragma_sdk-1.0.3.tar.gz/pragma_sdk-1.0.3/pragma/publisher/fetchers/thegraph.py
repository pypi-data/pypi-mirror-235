import asyncio
import logging
import time
from typing import List

import requests
from aiohttp import ClientSession

from pragma.core.assets import PragmaAsset, PragmaSpotAsset
from pragma.core.entry import GenericEntry
from pragma.publisher.types import PublisherInterfaceT

logger = logging.getLogger(__name__)


class TheGraphFetcher(PublisherInterfaceT):
    BASE_URL: str = "https://api.thegraph.com/subgraphs/name/"
    SOURCE: str = "THEGRAPH"

    publisher: str

    def __init__(self, assets: List[PragmaAsset], publisher):
        self.assets = assets
        self.publisher = publisher

    async def _fetch_pair(
        self, asset: PragmaSpotAsset, session: ClientSession
    ) -> GenericEntry:
        if asset["source"] == "AAVE":
            url_slug = "aave/protocol-v2"
            query = (
                f"query "
                f"{{reserves(where: {{id: \"{asset['detail']['asset_address']}\"}}) "
                f"{{name isActive isFrozen {asset['detail']['metric']}}}}}"
            )
            input_decimals = 27
        else:
            raise ValueError(
                f"Unknown asset name, do not know how to query The Graph for {asset['name']}"
            )

        async with session.post(
            self.BASE_URL + url_slug, json={"query": query}
        ) as resp:
            result_json = await resp.json()
            result = result_json["data"]["reserves"][0]

            return self._construct(asset, result, input_decimals=input_decimals)

    def _fetch_pair_sync(self, asset: PragmaSpotAsset) -> GenericEntry:
        if asset["source"] == "AAVE":
            url_slug = "aave/protocol-v2"
            query = (
                f"query {{reserves(where: "
                f"{{id: \"{asset['detail']['asset_address']}\"}}) "
                f"{{name isActive isFrozen {asset['detail']['metric']}}}}}"
            )
            input_decimals = 27
        else:
            raise ValueError(
                f"Unknown asset name, do not know how to query The Graph for {asset['name']}"
            )

        resp = requests.post(self.BASE_URL + url_slug, json={"query": query})
        result_json = resp.json()
        result = result_json["data"]["reserves"][0]
        return self._construct(asset, result, input_decimals=input_decimals)

    async def fetch(self, session: ClientSession) -> List[GenericEntry]:
        entries = []
        for asset in self.assets:
            if asset["type"] != "ONCHAIN":
                logger.debug("Skipping The Graph for non-on-chain asset %s", asset)
                continue
            entries.append(asyncio.ensure_future(self._fetch_pair(asset, session)))
        return await asyncio.gather(*entries, return_exceptions=True)

    def fetch_sync(self) -> List[GenericEntry]:
        entries = []
        for asset in self.assets:
            if asset["type"] != "ONCHAIN":
                logger.debug("Skipping The Graph for non-on-chain asset %s", asset)
                continue
            entries.append(self._fetch_pair_sync(asset))
        return entries

    def _construct(self, asset, result, input_decimals=27) -> GenericEntry:
        key = asset["key"]

        if result["name"] != asset["detail"]["asset_name"]:
            raise ValueError("invalid json")
        if not result["isActive"] is True:
            raise ValueError("invalid json")
        if not result["isFrozen"] is False:
            raise ValueError("invalid json")

        value = float(result[asset["detail"]["metric"]])
        value_int = int(value * (10 ** (asset["decimals"] - input_decimals)))
        timestamp = int(time.time())

        logger.info("Fetched data %s for %s from The Graph", value_int, key)

        return GenericEntry(
            key=key,
            value=value_int,
            timestamp=timestamp,
            source=self.SOURCE,
            publisher=self.publisher,
        )
