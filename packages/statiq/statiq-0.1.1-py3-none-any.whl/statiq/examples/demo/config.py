def my_upper_filter(value):
    return value.upper()


FILTERS = {"my_upper_filter": my_upper_filter}

GLOBALS = {"my_global": "my global value"}

STATIC_PATHS = [
    {
        "path": "static"
    }
]

STATIC_OUTPUT_PATH = "output"

