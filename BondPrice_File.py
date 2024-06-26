#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 14:12:57 2024

@author: muxilin
"""

import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    # Calculate the number of total payments
    n = m * ppy
    
    # Calculate the coupon payment
    coupon = face * couponRate / ppy
    
    # Discount factor per period
    discount_factor = (1 + y / ppy) ** np.arange(1, n + 1)
    
    # Present value of coupon payments
    pv_coupons = coupon / discount_factor
    
    # Present value of face value
    pv_face = face / ((1 + y / ppy) ** n)
    
    # Total present value (bond price)
    bond_price = np.sum(pv_coupons) + pv_face
    
    return bond_price



# Test values

y = 0.03
face = 2000000
couponRate = 0.04
m = 10

