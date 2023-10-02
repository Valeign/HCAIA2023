#!/usr/bin/env python3

class Complex:
    def _init_(self, real, img):
        self.r = real
        self.i = img
    
    def __str__(self):
        return str(self.r), "+ i", str(self.i)
    
    def __add__(self, c):
        return Complex(self.r +c.r+self,i + c.i)
