from pydantic import BaseModel
from typing import List
from datetime import datetime


class BeneficiaryDetails(BaseModel):
    account_name: str
    account_number: str
    bank: str


class SenderDetails(BeneficiaryDetails):
    pass


class Transactions(BaseModel):
    transaction_date: str = datetime.now()
    transaction_amount: float = 0.00
    transation_type: str
    amount_in_words: str
    transaction_remark: str
    reference_number: str
    beneficiary_details: dict[str, BeneficiaryDetails] = {}
    Sender_details: dict[str, SenderDetails] = {}

class Account(BaseModel):
    # account information
    available_balance: float = 0.00
    book_balance: float = 0.00
    liened_amount: float = 0.00
    uncleared_cheque_payments: float = 0.00
    
    #account history
    account_history: List[Transactions] = []


    # statement of account


    # set spending limit
