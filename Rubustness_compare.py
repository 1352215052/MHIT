
import Robustness_herd
import Rubustness_reinforce 
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

    



mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['font.size'] = 8
mpl.rcParams['axes.linewidth'] = 1
mpl.rcParams['lines.linewidth'] = 1.2
fig, ax = plt.subplots(figsize=(4,3))


def count_index(e_last):
	big_list=[]
	# semall_list=[]
	for i in e_last:
		if i >0.5:
			big_list.append(i)
		# else:
		# 	semall_list.append(i)
	big_index=round(len(big_list)/len(e_last),4)

	semall_index=round(1-big_index,4)
	return big_index,semall_index





e_last1=Robustness_herd.plot_fig1(10000,0.05,0.26,100,400,0.3,1)

e_last2=Rubustness_reinforce.plot_fig2(10000,0.05,0.26,100,250,0.3,1)

big1,semall1=count_index(e_last1)
big2,semall2=count_index(e_last2)

# print(e_last1)



a = np.array(e_last1)
b = np.array(e_last2)

# 计算统计量
def stats_summary(x):
    mean = np.mean(x)
    median = np.median(x)
    std = np.std(x, ddof=1)
    cv = std / mean
    se = stats.sem(x)
    ci = 1.96 * se
    return mean, median, std, cv, mean-ci, mean+ci

A = stats_summary(a)
B = stats_summary(b)

# # 整理数据
# df = pd.DataFrame({
#     "value": np.concatenate([a, b]),
#     "condition": ["Condition A"]*len(a) + ["Condition B"]*len(b)
# })


# 构造图例文字
text_A = (
    f"Without selective exposure\n"
    f"mean={A[0]:.3f}\n"
    f"median={A[1]:.3f}\n"
    f"std={A[2]:.3f}\n"
    f"CV={A[3]:.3f}\n"
    f"95%CI=[{A[4]:.3f},{A[5]:.3f}]\n"
	f"HI rate={big1}\n"
	f"No-HI rate={semall1}"

)

text_B = (
    f"With selective exposure\n"
    f"mean={B[0]:.3f}\n"
    f"median={B[1]:.3f}\n"
    f"std={B[2]:.3f}\n"
    f"CV={B[3]:.3f}\n"
    f"95%CI=[{B[4]:.3f},{B[5]:.3f}]\n"
	f"HI rate={big2}\n"
	f"No-HI rate={semall2}"
)

	# 添加文本框（固定在右上角）
ax.text(0.05, 0.95, text_A, 
		transform=ax.transAxes,
		fontsize=6,
		verticalalignment='top',
		horizontalalignment='left',
		bbox=dict(boxstyle='round', 
					facecolor='aliceblue', 
					alpha=0.9,
					edgecolor='gray',
					pad=0.5))

ax.text(0.65, 0.95, text_B, 
		transform=ax.transAxes,
		fontsize=6,
		verticalalignment='top',
		horizontalalignment='left',
		bbox=dict(boxstyle='round', 
					facecolor='aliceblue', 
					alpha=0.9,
					edgecolor='gray',
					pad=0.5))


plt.xlabel('Simulation runs')  
plt.ylabel('Equilibrium immune proportion(%)')  
plt.legend()  
plt.tight_layout()
plt.savefig(r'E:\AAA\论文写作\A群体免疫\A优化模型\写作内容\投稿\英文投稿\英文\CHB\退修\imag\FIG4a.tif',
			 format="tif" ,
			 dpi=1000,
			 bbox_inches="tight",
			 pil_kwargs={"compression": "tif_lzw"})
plt.show()  #显示图形
 
