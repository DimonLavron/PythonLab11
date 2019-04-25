from models.BankingService import BankingService

class Remittance(BankingService):
    def __init__(self, currency=None, client=None, clerk=None, date_of_beginning_service="01.01.1970", service_term_in_month=0, service_fee=0.0, receiver=None, type_of_remittance=None):
        super().__init__(currency, client, clerk, date_of_beginning_service, service_term_in_month, service_fee)
        self.receiver = receiver
        self.type_of_remittance = type_of_remittance

    def __str__(self):
        return "Remittance: " + str(self.__dict__)
