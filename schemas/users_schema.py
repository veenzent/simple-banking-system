from schemas.accounts_schema import Account


class User(Account):
    username: str
    full_name: str
    email: str
    balance: float = 0.0
    account_type: str
    # account_status: str
    # bvn_number: str
    # gender: str
    # date_of_birth: str
    # residential_address: str
    # phone_number: str
    # nationality: str
    # means_of_id: str
    # id_number: str
    # occupation: str

class UserCreate(User):
    pass


users: dict[str, User] = {}