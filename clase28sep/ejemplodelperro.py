#!/usr/bin/env

class Dog:
    
    familia = 'canine'   #Atributo de clase
    
    def __init__(self, name):
        self.name = name
        
        self.tricks=[]
        
    def add_trick(self, trick):
        self.tricks.append(trick)
