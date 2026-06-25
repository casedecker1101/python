import json
import pandas as pd

def normalize_dataset(data):
    """Return a list of dict rows suitable for csv.DictWriter."""
    
    # Case 1: JSON is a list of objects
    if isinstance(data, list):
        if not data:
            raise ValueError("JSON file contains an empty list.")
        if not all(isinstance(row, dict) for row in data):
            raise ValueError("JSON list must contain only objects.")
        return pd.json_normalize(data).to_dict(orient="records")

    # Case 2: JSON is a dict
    if isinstance(data, dict):

        # Case 2a: Single object → flatten it
        if all(not isinstance(value, list) for value in data.values()):
            return pd.json_normalize(data).to_dict(orient="records")

        # Case 2b: Wrapped list → flatten the list
        for value in data.values():
            if isinstance(value, list):
                if not value:
                    raise ValueError("JSON contains an empty records list.")
                if not all(isinstance(row, dict) for row in value):
                    raise ValueError("Wrapped JSON list must contain only objects.")
                return pd.json_normalize(value).to_dict(orient="records")

    raise ValueError("Unsupported JSON structure.")

