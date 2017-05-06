# -*- coding: utf-8 -*-

u"""Используя ООП, разработать систему, которая расчитвала бы
    прибыль авиакампании. Использовать сущности Авиакампания,
    Рейс, Самолет, Билет, ЧленЭкипажа"""

__author__ = "Shybkoi"


class AirCompany(object):
    u"""
    класс авиакомпании
    """
    def __init__(self, name):
        self.name = name
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def calc_profit(self):
        profit = 0
        for item in self.flights:
            profit += item.calc_fligth_profit()
        return profit


class Flight(object):
    u"""
    класс Рейс, в котором консолидируем всю информацию
    о рейсе и расчитываем все расходы и доходы от рейса
    """
    def __init__(self, **kwargs):
        self.title = kwargs['title']
        self.rout_length = kwargs['length']
        self.aircraft = kwargs['aircraft']
        self.crew = []
        self.tickets = []

    def add_staff(self, staff):
        self.crew.append(staff)

    def add_tickets(self, ticket):
        self.tickets.append(ticket)

    def calc_fligth_profit(self):
        outcome = 0
        income = 0
        for item in self.crew:
            outcome += item.salary
        outcome += self.rout_length * self.aircraft.calc_avg_consuption()
        for item in self.tickets:
            income += item.income()
        return income - outcome


class AirCraft(object):
    u"""
    класс Самолет
    avg_speed - крейсерская скорость км/ч
    consuption - расход топлива кг/ч
    """
    def __init__(self, model, fuel_price, avg_speed, consuption):
        self.model = model
        self.fuel_price = fuel_price
        self.avg_speed = avg_speed
        self.consuption = consuption

    def calc_avg_consuption(self):
        try:
            res = self.consuption/self.avg_speed * self.fuel_price
        except ZeroDivisionError:
            res = 0
        return res

class Staff(object):
    u"""
    класс ЧленКоманды
    """
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary


class Ticket(object):
    u"""класс Билет"""
    def __init__(self, ticket_class, amount, price):
        self.ticket_class = ticket_class
        self.price = price
        self.amount = amount

    def income(self):
        return self.price * self.amount


def main():
    company = AirCompany("Rapid Airlines")

    plane1 = AirCraft("Boeing 737", 1, 795, 2600)
    plane2 = AirCraft("Airbus 320", 1, 840, 2500)

    flight1 = Flight(title="Kiev - Paris", length=2020, aircraft=plane1)
    flight2 = Flight(title="Kiev - Paris", length=2020, aircraft=plane2)
    flight3 = Flight(title="London - Madrid", length=1260, aircraft=plane1)

    emplo1 = Staff("Orlando Bloom", "pilot", 800)
    emplo2 = Staff("Micky Mouse", "pilot", 700)
    emplo3 = Staff("Penelope Cruz", "steward", 200)
    emplo4 = Staff("Monica Bellucci", "steward", 200)

    ticket1 = Ticket("business", 50, 200)
    ticket2 = Ticket("business", 30, 240)
    ticket3 = Ticket("standart", 80, 120)
    ticket4 = Ticket("standart", 100, 100)

    flight1.add_staff(emplo1)
    flight1.add_staff(emplo3)
    flight1.add_staff(emplo4)
    flight2.add_staff(emplo1)
    flight2.add_staff(emplo2)
    flight2.add_staff(emplo4)
    flight3.add_staff(emplo1)
    flight3.add_staff(emplo2)
    flight3.add_staff(emplo3)
    flight3.add_staff(emplo4)

    flight1.add_tickets(ticket1)
    flight1.add_tickets(ticket3)

    flight2.add_tickets(ticket2)
    flight2.add_tickets(ticket3)

    flight3.add_tickets(ticket4)

    company.add_flight(flight1)
    company.add_flight(flight2)
    company.add_flight(flight3)

    print("Total {} profit is {:.2f}".format(company.name, company.calc_profit()))


if __name__ == "__main__":
    main()





