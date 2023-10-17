import logging
from dataclasses import dataclass, field
from logging import Logger
from typing import Tuple

from robot.api import Collector, XmlNode, Context

__logger__ = logging.getLogger(__name__)


@dataclass()
class CssCollector(Collector[XmlNode, XmlNode]):
    css_selector: str
    logger: Logger = field(default=__logger__, compare=False)

    async def __call__(self, context: Context, item: XmlNode) -> Tuple[Context, XmlNode]:
        try:
            return context, item.find_by_css(self.css_selector)
        except Exception as ex:
            raise Exception(f'Fail to apply css selector "{self.css_selector}" on {type(item)}', ex)
