import numpy as np
import pandas as pd


def make_json_serializable(obj):
    if isinstance(obj, dict):
        return {k: make_json_serializable(v) for k, v in obj.items()}

    elif isinstance(obj, list):
        return [make_json_serializable(item) for item in obj]

    elif isinstance(obj, tuple):
        return tuple(make_json_serializable(item) for item in obj)

    elif isinstance(obj, pd.DataFrame):
        return make_json_serializable(obj.to_dict(orient="records"))

    elif isinstance(obj, pd.Series):
        return make_json_serializable(obj.to_dict())

    elif isinstance(obj, np.integer):
        return int(obj)

    elif isinstance(obj, np.floating):
        return float(obj)

    elif isinstance(obj, np.bool_):
        return bool(obj)

    elif obj is None:
        return None

    return obj
