from models.BankingService import BankingService

class Deposit(BankingService):
    def __init__(self, currency=None, client=None, clerk=None, date_of_beginning_service="01.01.1970", service_term_in_month=0, service_fee=0.0, interest_rate=0.0, type_of_deposit=None):
        super().__init__(currency, client, clerk, date_of_beginning_service, service_term_in_month, service_fee)
        self.interest_rate = interest_rate
        self.type_of_deposit = type_of_deposit

    def __str__(self):
        return "Deposit: " + srt(self.__dict__())
