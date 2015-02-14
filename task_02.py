#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

INDEXSPANISH = inquisition.SPANISH.index('Spanish')

LEN_SPANISH = len('Spanish')

LEFT_SLICE = inquisition.SPANISH[0:INDEXSPANISH]

REGHT_SLICE = inquisition.SPANISH[INDEXSPANISH + LEN_SPANISH:]

FLEMISH = LEFT_SLICE + 'Flemish' + REGHT_SLICE
