"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

import math

# ask for User's age
maxBPM = 220 - int(input("What is your age?"))
maxRate = int(.85*maxBPM)
minRate = int(.65*maxBPM)
print(f"You should keep your Heart Rate between {minRate} and {maxRate} to maintain a healthy workout.")