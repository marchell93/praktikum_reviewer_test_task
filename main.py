# TODO в коде буду использовать абревиатуры pep8 EXXX, где XXX - целые числа
# TODO вам необходимо прогуглить данные конструкцию, для закрепления материала
import datetime as dt
# TODO в коде не используется данный импорт, его нужно убрать
import json
# TODO pep8 E302, перед началом описания класса должно быть 2 пустые строки
class Record:
    def __init__(self, amount, comment, date=''):
        # TODO pep8 E225, до и после знака '=' должны быть пробелы
        self.amount=amount
        # TODO строка > 79 символов, необходимо сделать перенос строки
        self.date = dt.datetime.now().date() if not date else dt.datetime.strptime(date, '%d.%m.%Y').date()
        # TODO pep8 E225, до и после знака '=' должны быть пробелы
        self.comment=comment
# TODO pep8 E302, перед началом описания класса должно быть 2 пустые строки
class Calculator:
    def __init__(self, limit):
        self.limit = limit
        # TODO pep8 E225, до и после знака '=' должны быть пробелы
        self.records=[]
    # TODO pep8 E301, перед началом описания метода должна быть 1 пустая строка
    def add_record(self, record):
        self.records.append(record)
    # TODO pep8 E301, перед началом описания метода должна быть 1 пустая строка
    def get_today_stats(self):
        # TODO pep8 E225, до и после знака '=' должны быть пробелы
        today_stats=0
        # TODO 1) название переменной не должно начинаться с большой буквы pep8
        # TODO 2) в данном случае у нас есть class Record, а мы пытаемся
        # TODO сделать из него переменную, так нельзя делать
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                today_stats = today_stats+Record.amount
        return today_stats
    # TODO pep8 E301, перед началом описания метода должна быть 1 пустая строка
    def get_week_stats(self):
        # TODO pep8 E225, до и после знака '=' должны быть пробелы
        week_stats=0
        today = dt.datetime.now().date()
        for record in self.records:
            # TODO 1) перед record.date 2 пробела, должен быть 1
            # TODO 2) pep8 E225, до и после знаков '<' и '>='
            #  должны быть пробелы
            # TODO 3) строка > 79 символов, необходимо сделать перенос строки
            if (today -  record.date).days <7 and (today -  record.date).days >=0:
                # TODO pep8 E225, до и после знака '+=' должны быть пробелы
                week_stats +=record.amount
        return week_stats
# TODO pep8 E302, перед началом описания класса должно быть 2 пустые строки
class CaloriesCalculator(Calculator):
    # TODO здесь лучше использовать Docstring, а не комментарий
    # TODO и над текстом нужно поработать, данный метод ничего не получает
    # TODO он только возвращает используя оператор return
    def get_calories_remained(self): # Получает остаток калорий на сегодня
        # TODO 1) Не правильно называться переменную одной буквой
        # TODO другой человек, кто будет читать твой код не поймет, что в этой
        # TODO переменной храниться, да и через время ты сам забудешь)))
        # TODO назови так, чтобы было понятно всем, что в ней
        # TODO 2) pep8 E225, до и после знака '=' должны быть пробелы
        x=self.limit-self.get_today_stats()
        if x > 0:
            # TODO Строка > 79 символов, необходимо сделать перенос строки
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {x} кКал'
        else:
            return 'Хватит есть!'
# TODO pep8 E302, перед началом описания класса должно быть 2 пустые строки
class CashCalculator(Calculator):
    # TODO 1) pep8 E225, до и после знака '=' должны быть пробелы
    # TODO 2) при использовании комментариев необходимо делать отступ от
    #  работающей строки в 2 пробела pep8 261,
    #  а внутри комментария от # до описания 1 пробел pep8 262.
    USD_RATE=float(60) #Курс доллар США.
    EURO_RATE=float(70) #Курс Евро.
    # TODO 1) pep8 E301, перед началом описания метода должна
    #  быть 1 пустая строка,
    # TODO 2) нужно убрать USD_RATE=USD_RATE, EURO_RATE=EURO_RATE,
    #  так как данные константы находяться в глобальной видимости
    #  класса CashCalculator, следовательно, передавать их в метод не нужно
    def get_today_cash_remained(self, currency, USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        # TODO pep8 E225, до и после знака '=' должны быть пробелы
        currency_type=currency
        cash_remained = self.limit - self.get_today_stats()
        # TODO pep8 E225, до и после знака '==' должны быть пробелы
        if currency=='usd':
            cash_remained /= USD_RATE
            # TODO pep8 E225, до и после знака '=' должны быть пробелы
            currency_type ='USD'
        # TODO pep8 E225, до и после знака '==' должны быть пробелы
        elif currency_type=='eur':
            cash_remained /= EURO_RATE
            # TODO pep8 E225, до и после знака '=' должны быть пробелы
            currency_type ='Euro'
        # TODO pep8 E225, до и после знака '==' должны быть пробелы
        elif currency_type=='rub':
            # TODO знак '==' является оператором сравнения и используется,
            #  в основном, в условных конструкция (if-else и т.д.),
            #  в данном случае ты ошибься, здесь нам необходимо разделить
            #  на 1.00 (cash_remained /= 1.00)
            cash_remained == 1.00
            # TODO pep8 E225, до и после знака '==' должны быть пробелы
            currency_type ='руб'
        if cash_remained > 0:
            # TODO 3) строка > 79 символов, необходимо сделать перенос строки
            return f'На сегодня осталось {round(cash_remained, 2)} {currency_type}'
        elif cash_remained == 0:
            return 'Денег нет, держись'
        elif cash_remained < 0:
            # TODO 3) строка > 79 символов, необходимо сделать перенос строки
            return 'Денег нет, держись: твой долг - {0:.2f} {1}'.format(-cash_remained, currency_type)
    # TODO данный метод описан в родительском классе и данная запись
    #  перезаписывается метод родительского класса, следовательно, эти строки
    #  необходимо удалить, чтобы наше приложение работало корректно
    def get_week_stats(self):
        super().get_week_stats()

# TODO отсутствует блок if __name__ == '__main__': как ты проверил,
#  что твой код рабочий?
