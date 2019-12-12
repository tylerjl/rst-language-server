from inspect import getdoc  # , getmro

try:
    from typing import TypedDict
except ImportError:
    from typing_extensions import TypedDict


class RoleInfo(TypedDict):
    element: str
    name: str
    description: str
    module: str


class DirectiveInfo(TypedDict):
    element: str
    name: str
    description: str
    klass: str
    required_arguments: int
    optional_arguments: int
    has_content: bool
    options: dict


def get_role_json(name, role) -> RoleInfo:
    return {
        "element": "role",
        "name": name,
        "description": getdoc(role) or "",
        "module": f"{role.__module__}",
    }


def get_directive_json(name, direct) -> DirectiveInfo:
    data = {
        "element": "directive",
        "name": name,
        # TODO this can also return docutils base class docstring, which is too verbose
        "description": getdoc(direct) or "",
        "klass": f"{direct.__module__}.{direct.__name__}",
        "required_arguments": direct.required_arguments,
        "optional_arguments": direct.optional_arguments,
        "has_content": direct.has_content,
        "options": {k: str(v.__name__) for k, v in direct.option_spec.items()}
        if direct.option_spec
        else {},
    }
    return data