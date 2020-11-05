# -*- coding: utf-8 -*-
"""
Script to generate arithmetic exercises.
"""

import random
from reportlab.pdfgen import canvas

def add_sub_expr(min_num, max_num):
    """
    Generate addition expression with operands in [min_num, max_num) and sum 
    less than max_num, or subtraction expression with operands in [min_num,
    max_num).
    """
    num_list = range(min_num, max_num)
    (a, b) = (max_num, max_num + 1)
    op = ' + ' if random.choice([0,1])==0 else ' - '
    if op == ' + ':
        # exit condition: a, b are in [min_num, max_num) and a + b <= max_num
        while a + b > max_num:
            (a, b) = random.choices(num_list, k=2)
    else:
        # exit condition: a, b are in [min_num, max_num) and a >= b
        while b - a > 0:
            (a, b) = random.choices(num_list, k=2)
    return str(a) + op + str(b) + ' = '

n_pages = 5
f = canvas.Canvas('worksheet.pdf')
min_num = 5
max_num = 30

for i in range(0, n_pages):
    f.setLineWidth(1)
    f.setFont('Helvetica', 20)
    for j in range(0, 15):
        f.drawString(70, 80+45*j, add_sub_expr(min_num, max_num))
        f.drawString(320, 80+45*j, add_sub_expr(min_num, max_num))
    f.drawString(50, 780, 'Name:______________')
    f.drawString(320, 780, 'Date:______________')
    f.showPage()
    
f.save()
