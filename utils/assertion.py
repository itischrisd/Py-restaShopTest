def assert_equals(actual, expected):
    assert actual == expected, f"Expected {expected}, but got {actual}"


def assert_contains(collection, element):
    assert element in collection, f"Expected {element} to be in {collection}"
