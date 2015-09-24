#!/usr/bin/env python

import os
from sys import path

class PepperUI:
  def button(self, img, x, y):
    print "Your new pepper button"

pepperUI = PepperUI()
close_btn = pepperUI.button("img", 1, 2)
