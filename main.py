from managers.BankingServiceManager import BankingServiceManager
from models.Credit import Credit
from models.Deposit import Deposit
from models.Remittance import Remittance
from models.Currency import Currency
from models.Person import Person
from models.TypeOfCredit import TypeOfCredit
from models.TypeOfDeposit import TypeOfDeposit
from models.TypeOfRemittance import TypeOfRemittance

credit1 = Credit(Currency.EUR, Person("Dima", "Lavrishyn"), Person("Ivan", "Petrov"), "12.01.2019", 12, 12.5, 9.8, TypeOfCredit.CONSUMER)
deposit1 = Deposit(Currency.RUB, Person("Ruslan", "Trest"), Person("Ivan", "Petrov"), "25.10.2017", 36, 5.4, 11.3, TypeOfDeposit.WITH_REPLENISHMENT)
credit2 = Credit(Currency.UAH, Person("Alina", "Klochko"), Person("Artem", "Sudakov"), "31.07.2018", 18, 7.5, 6.4, TypeOfCredit.MORTGAGE)
remittance1 = Remittance(Currency.USD, Person("Nataliia", "Karpova"), Person("Artem", "Sudakov"), "24.02.2016", 42, 11.7, Person("Petro", "Karpov"), TypeOfRemittance.INTERNATIONAL)
deposit2 = Deposit(Currency.EUR, Person("Viktoriia", "Shtank"), Person("Vasyl", "Lyubomyrov"), "05.10.2017", 24, 15.0, 14.1, TypeOfDeposit.WITH_PARTIAL_REMOVAL)
deposit3 = Deposit(Currency.USD, Person("Bogdan", "Tsvetkov"), Person("Vasyl", "Lyubomyrov"), "11.04.2017", 20, 8.3, 10.8, TypeOfDeposit.WITHOUT_REMOVAL_AND_REPLENISHMENT)
credit3 = Credit(Currency.RUB, Person("Olena", "Gavrylyuk"), Person("Melisa", "Harchenko"), "19.05.2016", 44, 11.3, 16.1, TypeOfCredit.CAR)
remittance2 = Remittance(Currency.UAH, Person("Ilona", "Varan"), Person("Melisa", "Harchenko"), "20.02.2019", 6, 4.5, Person("Yulia", "Malahova"), TypeOfRemittance.UKRAINIAN)

list_of_services = [credit1, deposit1, credit2, remittance1, deposit2, deposit3, credit3, remittance2]

manager = BankingServiceManager(list_of_services)

print(manager.get_available_credits())
print(manager.get_available_deposits())
print(manager.get_available_credits_sorted_by_service_fee())
print(manager.get_available_deposits_sorted_by_service_term())

list_of_services = manager.sort_by_service_fee(list_of_services, True)
print(list_of_services)
list_of_services = manager.sort_by_service_fee(list_of_services, False)
print(list_of_services)
