#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    c1 = Customer(name='Emiley')
    c2 = Customer(name='Connor')
    c3 = Customer(name='Melana')

    co1 = Coffee(name='Mocha')
    co2 = Coffee(name='Flat White')
    co3 = Coffee(name='Iced Coffee')

    o1 = Order(customer=c1, coffee=co1, price=2.0)
    o2 = Order(customer=c1, coffee=co1, price=2.0)
    o3 = Order(customer=c1, coffee=co2, price=3.0)

    o4 = Order(customer=c2, coffee=co3, price=4.0)

    # co1.orders() #should return list w/ 2 orders
    # c1.orders()

    ipdb.set_trace()
