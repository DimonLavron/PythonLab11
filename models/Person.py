class Person():
    def __init__(self, first_name="", surname=""):
        self.first_name = first_name
        self.surname = surname

    def __str__(self):
        return srt(self.__dict__())
