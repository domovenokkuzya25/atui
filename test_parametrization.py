import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_number(number: int) -> None:
    print(f'Number: {number}')
    assert number > 0

@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected

@pytest.mark.parametrize("os", ["windows", "linux", "macos", "debian"])
@pytest.mark.parametrize("browser", ["firefox", "chromium", "webkit"])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0


@pytest.fixture(params=['firefox', 'chromium', 'webkit'])
def browser(request: SubRequest):
    return request.param

def test_open_browser(browser: str):
    print(f'Running test on browser: {browser}')

@pytest.mark.parametrize("user", ['Alice', 'Zara'])
class TestOperation:
    @pytest.mark.parametrize("account", ['Credit card', 'Debit card'])
    def test_user_with_operations(self, user: str, account: str):
        print(f'User with operations: {user}')

    def test_user_without_operations(self, user: str):
        print(f'User without operations: {user}')



users = {
    '+700012554': 'user with money on bank account',
    '+7021312554': 'user with money on bank account',
    '+70054': 'user with operations on bank account'

}

# def format_phone_number(phone_number: str) -> str:
#     return f'{phone_number}: {users[phone_number]}'

@pytest.mark.parametrize(
    "phone_number",
    users.keys(),
    # ids=format_phone_number
    ids=lambda phone_number:    f'{phone_number}: {users[phone_number]}'
)
def test_identifiers(phone_number: str):
    ...
