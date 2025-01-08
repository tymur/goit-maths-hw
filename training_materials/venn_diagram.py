import matplotlib.pyplot as plt
from matplotlib_venn import venn3


set1 = set([2,4,6,8,10,12,14,16,18,20,22,24,26,28])
set2 = set([5,10,15,20,25])
set3 = set([4,9,16,25])


venn3([set1, set2, set3], ('Парні', 'Кратні 5', 'Повні квадрати'))


plt.show()
