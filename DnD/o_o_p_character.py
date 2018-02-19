#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 19:11:38 2018

@author: CarlKing
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rnd

#%%
class NewCharacter:
    def __init__(self):
        races = ['dwarf',
                 'elf',
                 'halfling',
                 'human',
                 'dragonborn',
                 'gnome',
                 'half-elf',
                 'half-orc',
                 'tiefling'
                 ]
        
        classes = ['barbarian', 
                 'bard', 
                 'cleric', 
                 'druid', 
                 'fighter', 
                 'monk', 
                 'paladin', 
                 'ranger', 
                 'rogue', 
                 'sorcerer', 
                 'warlock', 
                 'wizard'
                 ]
        
        skills = ['Acrobatics',
                'Animal Handling',
                'Arcana',
                'Athletics',
                'Deception',
                'History',
                'Insight',
                'Intimidation',
                'Investigation',
                'Medicine',
                'Nature',
                'Perception',
                'Performance',
                'Persuasion',
                'Religion',
                'Sleight of Hand',
                'Stealth',
                'Survival',]
        
        saving_throws = ['Strength',
                'Dexterit',
                'Constitution',
                'Intelligence',
                'Wisdom',
                'Charisma']
        
        
        
        def race_selection():
            print('\nRaces: ')
            for race in races:
                print('\t' + race.title())
            selection = input('\nChoose your race: ').lower()
            print('\n')
            if selection not in races:
                print('Please select a valid race.')
                selection = race_selection()
            return selection
        
        def class_selection():
            print('\nClasses: ')
            for cl_ss in classes:
                print('\t' + cl_ss.title())
            selection = input('\nChoose your class: ').lower()
            print('\n')
            if selection not in classes:
                print('Please select a valid class.')
                selection = class_selection()
            return selection
        
        self.race = race_selection()
        self.cl_ss = class_selection()
                


    def roll_for_stats(self):
        rolls = [rnd.randint(1,6),rnd.randint(1,6),rnd.randint(1,6),rnd.randint(1,6)]
        rolls.sort()
        top_three = rolls[1:]
        score = sum(top_three)
        return(score)
    
    def get_stats(self):
        self.all_stats = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
        all_stats = self.all_stats
        self.rolled_stats = []
        for stat in all_stats:
            value = self.roll_for_stats()
            self.rolled_stats.append(value)
        self.rolled_stats.sort(reverse=True)
        
        self.base_stats = {}
        j = 0
        while j < len(all_stats):
            stat = all_stats[j]
            stat_value = int(input("Choose which value you want assigned to " + stat.title() + ':\n' 
                + str(self.rolled_stats) + ': '))
            if stat_value in self.rolled_stats:
                self.base_stats[stat] = stat_value
                self.rolled_stats.remove(stat_value)
                j += 1
            else:
                print('dont cheat')
    


carl = NewCharacter()
carl.get_stats()

package = 'races.' + carl.race
name = carl.race.title()
race = getattr(__import__(package, fromlist=[name]), name)

package = 'classes.' + carl.cl_ss
name = carl.cl_ss.title()
cl_ss = getattr(__import__(package, fromlist=[name]), name)



kaai = race(carl.base_stats)
kaai.base_stats
stats = carl.base_stats
carl.base_stats


