from models.Credit import Credit
from models.Deposit import Deposit

class BankingServiceManager():
    def __init__(self, banking_services):
        self.banking_services = banking_services

    def get_available_credits(self):
        return list(filter(lambda service: isinstance(service, Credit), self.banking_services))

    def get_available_deposits(self):
        return list(filter(lambda service: isinstance(service, Deposit), self.banking_services))

    def get_available_credits_sorted_by_service_fee(self):
        return sorted(self.get_available_credits(), key = lambda service: service.service_fee)

    def get_available_deposits_sorted_by_service_term(self):
        return sorted(self.get_available_deposits(), key = lambda service: service.service_term_in_month)

    def sort_by_service_fee(self, services, reverse):
        return sorted(services, key = lambda service: service.service_fee, reverse = reverse)
