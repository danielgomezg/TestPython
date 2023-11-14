import datetime

class Dateformat():

    @classmethod
    def convertDate(cls, date):
        return datetime.datetime.strftime(date, '%d/%m/%Y')