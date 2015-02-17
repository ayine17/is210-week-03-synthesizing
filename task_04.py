#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""

NEWS = 'Hi {friend}! I have {0} news! I won the raffle with number {1:06d}!'
FNAME = 'Pat'
NTYPE = '*amazing*'
RNUM = 42

"""RNUM = '{RNUM:{fill}{width}}'.format(NRUM=123, fill='0', width=6)
RNUM= '{0:06}'.format(NRUM)
"""

EMAIL = NEWS.format(NTYPE, RNUM, friend=FNAME)
