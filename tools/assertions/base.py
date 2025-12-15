

def assert_status_code(actual: int, expected: int):
    assert actual==expected, (
        f'Не корректный статус код.'
        f'Полученный статус код {expected}.'
        f'Актуальный статус код {actual}'
    )