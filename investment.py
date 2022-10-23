#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 09:41:02 2022

@author: Admin
"""


def investment(X,Year,Z):
    i = 0
    Worth = 0
    while i < 1:
        if Year =='1':
            Worth = X * Z * 12
            i += 1
            return Worth 
        elif Year == '5':
            Worth = X * Z * 60
            i += 1
            return Worth
        elif Year == '10':
            Worth =  X * Z * 120
            i += 1
            return Worth
        elif Year == '15':
            Worth = X * Z * 180
            i += 1
            return Worth
        else:
            return print('error 1')
            
    print(Worth)
 
def Main():
    invest = float(input('How much would you like to invest?\n'))
    time = input('What growth would you like to see 1, 5, 10, or 15 Years\n')
    growth = float(input('What is the Divident payout?\n'))
    
    i = 0
    while i < 1:
         
        divident_break = input('Is this a monthly, quarterly, bi-annual, or annual paying stock?\n')
        if divident_break == "monthly":
            print(investment(invest, time, growth))
            i += 1
        elif divident_break == "quarterly":
            per_month = growth/3
            print(investment(invest, time, per_month))
            i += 1
        elif divident_break == "bi-annual":
            per_month = growth/6
            print(investment(invest, time, per_month))
            i += 1
        elif divident_break == "annual":
            per_month = growth/12
            print(investment(invest, time, per_month))
            i += 1
        else:
            print('Invalid entry, please try again \n')
            i = 0
        
        
        
Main()


