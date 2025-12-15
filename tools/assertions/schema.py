from typing import Any
from jsonschema import validate
from jsonschema.validators import Draft202012Validator

def validate_json_schema(isinstance: Any, schema: dict) -> None:
    validate(
        instance=isinstance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )