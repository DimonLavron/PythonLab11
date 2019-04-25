from models.BankingService import BankingService

class Credit(BankingService):
    def __init__(self, currency=None, client=None, clerk=None, date_of_beginning_service="01.01.1970", service_term_in_month=0, service_fee=0.0, interest_rate=0.0, type_of_credit=None):
        super().__init__(currency, client, clerk, date_of_beginning_service, service_term_in_month, service_fee)
        self.interest_rate = interest_rate
        self.type_of_credit = type_of_credit

    def __str__(self):
        return "Credit: " + str(self.__dict__)
