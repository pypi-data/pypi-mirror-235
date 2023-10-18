import json
import cloudpickle
import base64
from pydantic import BaseModel


def remove_pydantic_validators(obj):
    """
    This will define parse_obj and __dict__ for types we decide to support
    Note: due to Pydantic limitations, we can't pickle classes with validators
    https://github.com/cloudpipe/cloudpickle/issues/408

    :param unpickled_input: The input to add type converters to
    :type unpickled_input: Any
    :return: The input with type converters added
    :rtype: Any
    """
    if issubclass(type(obj), BaseModel):
        for field in obj.__fields__.values():
            field.validators = []
    elif isinstance(obj, list):
        return [remove_pydantic_validators(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: remove_pydantic_validators(value) for key, value in obj.items()}
    return obj


def serialize(obj):
    try:
        # Special case for pydantic objects
        obj = remove_pydantic_validators(obj)

        serialized_obj = cloudpickle.dumps(obj)
        return base64.b64encode(serialized_obj).decode("utf-8")
    except Exception as e:
        raise Exception(f"Error in serialization: {str(e)}")


def deserialize(serialized_obj):
    try:
        obj = base64.b64decode(serialized_obj)
        return cloudpickle.loads(obj)
    except Exception as e:
        raise Exception(f"Error in deserialization: {str(e)}")


def encode(obj):
    try:
        return json.dumps(obj)
    except Exception as e:
        raise Exception(f"Error in encoding: {str(e)}")


def decode(encoded_obj):
    try:
        return json.loads(encoded_obj)
    except Exception as e:
        raise Exception(f"Error in decoding: {str(e)}")
