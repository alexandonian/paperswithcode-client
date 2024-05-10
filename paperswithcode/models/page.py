from typing import Optional

from paperswithcode.models.model import Model


class Page(Model):
    """Page model.

    Attributes:
        count (int): Number of elements matching the query.
        next_page (int, optional): Number of the next page.
        previous_page (int, optional): Number of the previous page.
    """

    count: int
    next_page: Optional[int]
    previous_page: Optional[int]
