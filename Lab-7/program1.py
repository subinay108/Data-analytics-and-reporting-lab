# Implement a Pie-chart using python
import matplotlib.pyplot as plt
import numpy as np

mcu = {
    'Avengers': 2924,
    'Iron Man': 2424,
    'Captain America': 2238,
    'Thor': 1940,
    'Black Panther': 1300,
    'Guardians of the Galaxy': 1637,    
}

earnings = mcu.values()
franchises = mcu.keys()

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(list(allvals))))
    return f'{pct:.1f}%\n (${absolute:d} M)'

wedges, texts, autotexts = plt.pie(
    earnings, 
    autopct=lambda pct: func(pct, earnings),
    textprops=dict(color='w'))

plt.title('Earnings Percentage By Franchise')

plt.legend(
    wedges,
    franchises,
    title='Franchises', 
    loc='center left', 
    bbox_to_anchor=(1, 0, 0.5, 1))
plt.show()