from enum import Enum

class TypeOfDeposit(Enum):
    WITH_REPLENISHMENT = 1
    WITH_PARTIAL_REMOVAL = 2
    WITHOUT_REMOVAL_AND_REPLENISHMENT = 3
