#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 14:14:52 2024

@author: muxilin
"""

import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    # Calculate the number of total payments
    n = m * ppy
    
    # Calculate the coupon payment
    coupon = face * couponRate / ppy
    
    # Time periods
    t = np.arange(1, n + 1)
    
    # Discount factor per period
    discount_factor = (1 + y / ppy) ** t
    
    # Present value of coupon payments
    pv_coupons = coupon / discount_factor
    
    # Present value of face value
    pv_face = face / ((1 + y / ppy) ** n)
    
    # Total present value (bond price)
    bond_price = np.sum(pv_coupons) + pv_face
    
    # Cash flows
    cf = np.full(n, coupon)
    cf[-1] += face  # Add face value to the last payment
    
    # Present value of cash flows
    pv_cf = cf / discount_factor
    
    # Weight (w) and weighted time (w*t)
    w = pv_cf / bond_price
    w_t = w * t
    
    # Duration
    duration = np.sum(w_t)
    
    return duration

# Test values
y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1
