
import immune_find 
import immune_echo_find 
import matplotlib.pyplot as plt  
import matplotlib as mpl


mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['font.size'] = 8
mpl.rcParams['axes.linewidth'] = 1
mpl.rcParams['lines.linewidth'] = 1.2

plt.figure(figsize=(3.35,2.4))



immune_find.threshold_find(0.24,0.3,5,400,10000,0.3,1,0.05)
immune_echo_find.threshold_find(0.29,0.39,5,400,10000,0.3,1,0.05,0.6)

 
plt.xlabel('Initial immune proportion(%)')   
plt.ylabel('Equilibrium immune proportion(%)')  
plt.legend(loc='upper left')  
plt.show()  #显示图形

