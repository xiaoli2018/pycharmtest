# -*- coding:utf-8 -*-
__author__ = 'heng'

from reportlab.graphics.shapes import Drawing,String
from reportlab.graphics import renderPDF

d = Drawing(100,100)
s = String(50,50,'hello',textAnchor='middle')

d.add(s)

renderPDF.drawToFile(d,'hello.pdf','a simple pdf file')


