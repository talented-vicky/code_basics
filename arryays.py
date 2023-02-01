# first exercise

expense = {'January': 2200, 'February': 2350, 'March': 2600, 'April': 2130, 'May': 2190}
# extra money spent in Feb compared to January
a = expense['February'] - expense['January']
# total xpenses in first quarter
b = expense['January'] + expense['February'] + expense['March']
# find month where expense was exactly 2000
for check in expense:
    if expense[check] == 2000:
        print(check)
# add an expense of 1980 to your june monthly expense list
expense['June'] = 1980
# getting a refund of 2005 of an item purchased in april, correct list
expense['April'] = expense['April'] - 2005
