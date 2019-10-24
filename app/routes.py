from dataclasses import dataclass, field
from typing import Callable, AnyStr, Dict
from app.views.processes import process
from app.views.category import category
from app.views.categories import categories
from app.views.up import up


@dataclass
class Route:
    url: AnyStr
    view: Callable
    optional_params: Dict = field(default_factory=dict)


ROUTES = (
    Route('/up', up),
    Route('/categories', categories, dict(methods=['POST', 'GET'])),
    Route('/categories/<int:category_id>', category, dict(methods=['GET', 'PUT', 'DELETE'])),
    Route('/processes/<string:process_id>', process, dict(methods=['GET'])),
)
