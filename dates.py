#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Print number of days and weeks since your surgery."""

from datetime import date

previous_date = date(2015, 5, 28)
todays_date = date.today()
delta = todays_date - previous_date
print "It's been %s days (%.1f weeks) since May 28, 2015." % (delta.days, delta.days/7.)
