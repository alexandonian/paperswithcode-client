from typing import List, Optional


from paperswithcode.models.page import Page
from paperswithcode.models.model import Model


class Dataset(Model):
    """Dataset object.

    Attributes:
        id (str): Dataset ID.
        name (str): Dataset name.
        full_name (str, optional): Dataset full name.
        url (str, optional): URL for dataset download.
    """

    id: str
    name: str
    full_name: Optional[str]
    url: Optional[str]


class DatasetCreateRequest(Model):
    """Task object.

    Attributes:
        name (str): Dataset name.
        full_name (str, optional): Dataset full name.
        url (str, optional): Dataset url.
    """

    name: str
    full_name: Optional[str] = None
    url: Optional[str] = None


class DatasetUpdateRequest(Model):
    """Evaluation table row object.

    Attributes:
        name (str, optional): Dataset name.
        url (str, optional): Dataset url.
    """

    name: Optional[str] = None
    url: Optional[str] = None


class Datasets(Page):
    """Object representing a paginated page of datasets.

    Attributes:
        count (int): Number of elements matching the query.
        next_page (int, optional): Number of the next page.
        previous_page (int, optional): Number of the previous page.
        results (List[Dataset]): List of datasets on this page.
    """

    results: List[Dataset]
