#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 15:16:51 2018

@author: CarlKing
"""
class Human:
    def __init__(self, base_stats):
        self.base_stats = base_stats
        for stat in self.base_stats:
            self.base_stats[stat] += 1