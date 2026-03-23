
import immune_find 
import immune_reinforce_find 
import matplotlib.pyplot as plt  
import matplotlib as mpl

mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['font.size'] = 8
mpl.rcParams['axes.linewidth'] = 1
mpl.rcParams['lines.linewidth'] = 1.2

plt.figure(figsize=(3.35,2.4))



immune_find.threshold_find(0.24,0.29,10,400,10000,0.3,1,0.05)
immune_reinforce_find.threshold_find(0.25,0.31,10,250,10000,0.3,1,0.05)

 
plt.xlabel('Initial immune proportion(%)')   
plt.ylabel('Equilibrium immune proportion(%)')  
plt.legend(loc='upper left')  
plt.savefig(r'E:\AAA\论文写作\A群体免疫\A优化模型\写作内容\投稿\英文投稿\英文\CHB\退修\imag\FIG5c.tif',
			 format="tif" ,
			 dpi=1000,
			 bbox_inches="tight",
			 pil_kwargs={"compression": "tif_lzw"})
plt.show()  #显示图形

