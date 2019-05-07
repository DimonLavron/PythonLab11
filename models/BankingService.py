class BankingService():
    def __init__(self, currency=None, client=None, clerk=None, date_of_beginning_service="01.01.1970", service_term_in_month=0, service_fee=0.0):
        self.currency = currency
        self.client = client
        self.clerk = clerk
        self.date_of_beginning_service = date_of_beginning_service
        self.service_term_in_month = service_term_in_month
        self.service_fee = service_fee

    def __str__(self):
        return str(self.__dict__)
