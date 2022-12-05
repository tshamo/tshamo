#import my_module as mm
#from my_module import find_index as fi, test as t
#from my_module import * #not advicable

import sys
#sys.path.append('/Users/taulant.shamo/PycharmProjects/pythonProjectAndy/My_Modules')
# OR better: update .bash_profile add export PYTHNPATH="/Users/taulant.shamo/PycharmProjects/pythonProjectAndy/My_Modules"

from my_module import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']

#index = mm.find_index(courses, 'CompSci')
#index = fi(courses, 'CompSci')
index = find_index(courses, 'CompSci')

print(index)
#print(t)
print(test)
#print(sys.path)     # path to look for modules