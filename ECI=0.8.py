import numpy as np  
import matplotlib.pyplot as plt  
from matplotlib.animation import FuncAnimation  
import random,math
import matplotlib as mpl


def seed_create(seed_num,s,e):
	#第一步：初始化100个初始值为（0,3）之间的节点
	seed_list = [random.randint(0,3) for _ in range(seed_num)]  
	# seed_list=[random.randint(0,8)]
	# print(seed_list)


	#第二步：随机选择初始传播节点
	s_start=int(s*seed_num)  # s传播者初始比例
	e_start=int(e*seed_num) # e免疫者初始比例


	s_start_list = random.sample(range(len(seed_list)),s_start)  #从列表seed_list中随机选择s_start个元素的索引，注意是索引！
	#range(len(seed_list))表示范围是（0，len(seed_lisst))中随机选择s_start个元素
	# 遍历这些索引，并将对应位置的元素赋值  
	for s in s_start_list:  
		seed_list[s] = -random.randint(1,4)  #随机赋值（传播节点的病毒含量），注意前面的负号。


	#第三步：随机设置初始免疫节点
	# 首先，找到所有大于零的元素的索引（即排除掉所有的传播节点）
	postive_indices = [i for i, val in enumerate(seed_list) if val >=0 ] #默认前面是索引后面是值  
	# print(seed_list)
	# print(postive_indices)
	# 如果正值元素的数量少于初始值，则无法继续  
	if len(postive_indices) < e_start:  
	    print("没有足够的非零元素来继续操作。")  

	else:  
	    # 随机选择一定的正值元素的索引  
	    selected_postive_indices = random.sample(postive_indices,e_start)  #表示选择范围是postive_indices列表，从中选择e_start个元素的索引。
	    #print(len(selected_postive_indices))
	    # 将这些索引对应的元素值设置为免疫值  
	    for index in selected_postive_indices:  
	        seed_list[index] = random.randint(4,8)
	return seed_list


#同时获取元素索引和元素值
# for index, value in enumerate(seed_list):
# 	print(f"Index: {index}, Value: {value}")


#随机相遇函数（随机选择哪些个体参与接触）
def encounter(seed_list,num_prop):
	encounter_num=int(len(seed_list)*num_prop)
	encounter_list_indeces=random.sample(range(len(seed_list)),encounter_num)  #这取出的是索引，不是元素
	encounter_list=[seed_list[i] for i in encounter_list_indeces]
	# unencounter_list=[n for n in seed_list if n not in encounter_list]  这里因为值可能是重复的，所以不能这么写，必须用索引
	unencounter_list_indeces=[i for i in range(len(seed_list)) if i not in encounter_list_indeces]
	unencounter_list=[seed_list[i] for i in unencounter_list_indeces] 



	return encounter_list,unencounter_list

	
#常规转换通道
def norn_convert(seed_list,value,meet_other):
	if value<0 and seed_list[meet_other]<0:#（传播者--传播者）
		value+=-0.06
		seed_list[meet_other]+=-0.06
	elif value<0 and (seed_list[meet_other]>=0 and seed_list[meet_other]<4):#（传播者--无知者））
		value+=0
		seed_list[meet_other]+=-0.06
	elif value<0 and seed_list[meet_other]>=4:#（传播者--免疫者）
		value+=0.03
		seed_list[meet_other]+=-0.06
	#无知者
	elif (value>=0 and value<4) and seed_list[meet_other]<0:#（无知者--传播者）
		value+=-0.06
		seed_list[meet_other]+=0

	elif (value>=0 and value<4) and (seed_list[meet_other]>=0 and seed_list[meet_other]<4):#（无知者--无知者）
		value+=0
		seed_list[meet_other]+=0
	elif (value>=0 and value<4) and seed_list[meet_other]>=4:#（无知者--免疫者）
		value+=0.03
		seed_list[meet_other]+=0
	#免疫者
	elif value>=4 and seed_list[meet_other]<0:#（免疫者--传播者）
		value+=-0.06
		seed_list[meet_other]+=0.03

	elif value>=4 and (seed_list[meet_other]>=0 and seed_list[meet_other]<4):#（免疫者--无知者）
		value+=0
		seed_list[meet_other]+=0.03
	elif value>=4 and seed_list[meet_other]>=4:#（免疫者--免疫者）
		value+=0.03
		seed_list[meet_other]+=0.03
	return seed_list


#大跨度转换通道
def widerange_convert(seed_list,value,meet_other):

	if value<0 and seed_list[meet_other]<0:#（传播者--传播者）
		value+=-0.06
		seed_list[meet_other]+=-0.06
	elif value<0 and (seed_list[meet_other]>=0 and seed_list[meet_other]<4):#（传播者--无知者））
		value+=0
		seed_list[meet_other]+=-random.randint(1,10)
	elif value<0 and seed_list[meet_other]>=4:#（传播者--免疫者）
		value+=random.randint(1,50)
		seed_list[meet_other]+=-random.randint(1,50)
	#无知者
	elif (value>=0 and value<4) and seed_list[meet_other]<0:#（无知者--传播者）
		value+=-random.randint(1,10)
		seed_list[meet_other]+=0

	elif (value>=0 and value<4) and (seed_list[meet_other]>=0 and seed_list[meet_other]<4):#（无知者--无知者）
		value+=0
		seed_list[meet_other]+=0
	elif (value>=0 and value<4) and seed_list[meet_other]>=4:#（无知者--免疫者）
		value+=random.randint(1,10)
		seed_list[meet_other]+=0
	#免疫者
	elif value>=4 and seed_list[meet_other]<0:#（免疫者--传播者）
		value+=-random.randint(1,50)
		seed_list[meet_other]+=random.randint(1,50)

	elif value>=4 and (seed_list[meet_other]>=0 and seed_list[meet_other]<4):#（免疫者--无知者）
		value+=0
		seed_list[meet_other]+=random.randint(1,10)
	elif value>=4 and seed_list[meet_other]>=4:#（免疫者--免疫者）
		value+=0.03
		seed_list[meet_other]+=0.03

	return seed_list
	
#挑选函数（常规通道or大跨度通道）,生成一个随机选取概率为10%的列表
def select_fc(fc_prop):
	list_fc=[random.randint(0,3) for _ in range(10)]
	if fc_prop !=0:
		for i in range(fc_prop):
			list_fc[i]=-random.randint(1,3)

		indece=random.sample(range(len(list_fc)),1) #此处为一个列表，因此，还需要int(len(indece))转换成整数
		rand_num=list_fc[int(len(indece))]
	else:
		rand_num=6

	return rand_num




#状态转化函数
def state_convert(seed_list,fc_prop,echo):
	# print(seed_list)
	#取出所有元素索引和值，让每个人都随机接触一些人
	for index, value in enumerate(seed_list):  #
		#从这些元素中随机取出一定数量的元素的索引，注意是索引！作为每个个体即将相遇的陌生人
		negitive_indices = [i for i, val in enumerate(seed_list) if val < 0 ] #传播者索引集合
		ingnore_indices = [i for i, val in enumerate(seed_list) if val>=0 and val < 4 ] #易感者索引集合
		postive_indices = [i for i, val in enumerate(seed_list) if val >= 4 ] #免疫者索引集合

		if value <0: #需要构造一个95%个体为传播者的集合
			#构造固定数量目标集合
			other_indices=ingnore_indices+postive_indices #列表拼接，其他节点索引集合
			neg_len=int(round(50*echo)) #同类节点数量  从50个个体中相遇
			other_len=50-neg_len  #其余节点数量
			#如果出现样本大于总体（两个部分：1、同类集合；2、异类集合，用or连接）
			if len(negitive_indices)<=neg_len or len(other_indices)<=other_len:
				#print('"没有足够的传播者个体来继续操作。"')
				#那么这时候从总体集合中随机取数
				meet_other_indices = random.sample(range(len(seed_list)),random.randint(0,6)) 
			else:
				#构造回音室集合（大概率遇到同类）
				neg_indices=random.sample(negitive_indices,neg_len)+random.sample(other_indices,other_len)
				#相遇集合
				meet_other_indices = random.sample(neg_indices,random.randint(0,6))
		#遍历这些陌生人的索引
			for  meet_other in meet_other_indices:
				#判断这个陌生人是否是自己（利用索引进行判别）
				if index != meet_other: #如果不是自己则继续
					#print("第",index,'号节点开始接触陌生人！')
					#传播者（接触个体是传播者）
					rand_num=select_fc(fc_prop)
					if rand_num<0:
						seed_list=widerange_convert(seed_list,value,meet_other)
					else:
						seed_list=norn_convert(seed_list,value,meet_other)

				else: # 
					continue

		elif value>=0 and value<4:
			#没有回音室效应
			#meet_other_indices = random.sample(range(len(seed_list)),random.randint(0,6))




			other_indices=negitive_indices+postive_indices #列表拼接，其他节点索引集合
			ign_len=int(round(50*echo)) #同类节点数量
			other_len=50-ign_len  #其余节点数量


			#如果出现样本大于总体（两个部分：1、同类集合；2、异类集合，用or连接）
			if len(ingnore_indices)<=ign_len or len(other_indices)<=other_len:
				#print('"没有足够的传播者个体来继续操作。"')
				#那么这时候从总体集合中随机取数
				meet_other_indices = random.sample(range(len(seed_list)),random.randint(0,6)) 
			else:
				#构造回音室集合（大概率遇到同类）
				ign_indices=random.sample(ingnore_indices,ign_len)+random.sample(other_indices,other_len)
				#相遇集合
				meet_other_indices = random.sample(ign_indices,random.randint(0,6))
			for  meet_other in meet_other_indices:
				if index != meet_other: #如果不是自己则继续
					#print("第",index,'号节点开始接触陌生人！')
					#传播者（接触个体是传播者）
					rand_num=select_fc(fc_prop)
					if rand_num<0:
						seed_list=widerange_convert(seed_list,value,meet_other)
					else:
						seed_list=norn_convert(seed_list,value,meet_other)

				else: # 
					continue
		else:
			other_indices=ingnore_indices+negitive_indices
			post_len=int(round(50*echo))
			other_len=50-post_len

			if len(postive_indices)<=post_len or len(other_indices) <= other_len:
				#print('"没有足够的免疫者个体来继续操作。"')
				meet_other_indices = random.sample(range(len(seed_list)),random.randint(0,6))
			else:
				post_indices=random.sample(postive_indices,post_len)+random.sample(other_indices,other_len)
				meet_other_indices = random.sample(post_indices,random.randint(0,6))
			for  meet_other in meet_other_indices:
				if index != meet_other:
					#免疫者
					rand_num=select_fc(fc_prop)
					if rand_num<0:
						seed_list=widerange_convert(seed_list,value,meet_other)
					else:
						seed_list=norn_convert(seed_list,value,meet_other)
				else: # 
					continue

	return seed_list





def state_attenuation(seed_list_convert,s_start,e_start):
	#print(seed_list_convert)
	s_li=[i for i in seed_list_convert if i <0]
	i_li=[i for i in seed_list_convert if i >=0 and i <4]
	e_li=[i for i in seed_list_convert if i >=4]
	ps=round(int(len(s_li))/int(len(seed_list_convert)),2)
	pe=round(int(len(e_li))/int(len(seed_list_convert)),2)

	s_num=int(int(len(s_li))*((0.3)/(s_start+math.exp(1-ps))))  #表示最大的时候衰减率为10%,0.1的大小表示了波动大小，可以作为一个分析点
	#s_num=int(int(len(s_li))*((e_start)/(1+math.exp(1-ps))))
	# s_num=int(int(len(s_li))/(1+math.exp(1-ps*300)))
	s_indices = random.sample(range(len(s_li)),s_num)
	for i in s_indices:
		s_li[i]=random.randint(0,8) 



	e_num=int(int(len(e_li))*((0.3)/(e_start+math.exp(1-pe))))  #表示最大的时候衰减率为30%

	e_indices = random.sample(range(len(e_li)),e_num)
	for i in e_indices:
		e_li[i]=random.randint(-4,3) 

	seed_list_attenuation=s_li+i_li+e_li


	return seed_list_attenuation






#统计每种状态数量
def state_sum(seed_list_convert,seed_num):
	s_list=[] #每个时步统计一次（更新一次），所以每次s_list都会被重置（即重新变为空集）
	i_list=[]
	e_list=[]
	#对seed_list中的节点进行归类（传播者、无知者、免疫者）
	for  value in seed_list_convert:
		if value<0:
			s_list.append(value)
		elif value>=0 and value<4:
			i_list.append(value)
		else:
			e_list.append(value)

	s_num=int(len(s_list))
	i_num=int(len(i_list))
	e_num=int(len(e_list))
	# print(e_num)
	# print(s_num)
	s_port=round((s_num/seed_num),2) #转换为百分比，100为总人数
	i_port=round((i_num/seed_num),2)
	e_port=round((e_num/seed_num),2)

	return s_port,i_port,e_port






#1、绘图函数(时间--各群体状态变化曲线）)
def time_state(t_control,seed_list,seed_num,num_prop,fc_prop,s_start,e_start,echo):
	s=[]  #用来存储传播者的人数占比变化
	w=[]  #用来存储无知者的人数占比变化
	e=[]
	#控制时间（时步）
	for i in range(0,t_control):
		#如果是第一次，则直接统计占比，
		if i ==0:  #第一次（初始值）不参与状态转换
			s_port,i_port,e_port=state_sum(seed_list,seed_num)  #1.每种状态人数变化
			# anti=antibody_sum()
			s.append(s_port)
			w.append(i_port)
			e.append(e_port)
		else:  #之后则需要统计经过状态转换之后的人数占比
			encounter_list,unencounter_list=encounter(seed_list,num_prop)
			#print(len(unencounter_list))
			seed_list_convert=state_convert(encounter_list,fc_prop,echo)
			seed_list=seed_list_convert+unencounter_list

			seed_list_attenuation=state_attenuation(seed_list,s_start,e_start)  #衰减函数处理
			s_port,i_port,e_port=state_sum(seed_list_attenuation,seed_num)
			s.append(s_port)
			w.append(i_port)
			e.append(e_port)
	# print('信谣者稳态值为'+str(s[-1]))
	# print('中立者稳态值为'+str(w[-1]))
	# print('免疫者稳态值为'+str(e[-1]))
	# print(len(seed_list))
	dt=1 #时间间隔
	t= np.arange(0, t_control, dt)  # 生成时间数组  

	mpl.rcParams['font.family'] = 'Arial'
	mpl.rcParams['font.size'] = 8
	mpl.rcParams['axes.linewidth'] = 1
	mpl.rcParams['lines.linewidth'] = 1.2

	plt.figure(figsize=(3.35,2.4))


	plt.plot(t,s,color="#D55E00",linestyle="--", linewidth=2, label="Believer")# t和s必须是相同维度的数组（列表）
	plt.plot(t,w,color="#009E73", linestyle="-.", linewidth=2, label="Neutral")
	plt.plot(t,e,color="#0072B2",  linestyle="-", linewidth=2, label="Immune")

	plt.xlabel("Time")
	plt.ylabel("Proportion of individuals(%)")
	plt.legend()
	plt.tight_layout()
	plt.savefig(r'E:\AAA\论文写作\A群体免疫\A优化模型\写作内容\投稿\英文投稿\英文\CHB\退修\imag\FIG12a.tif',
			 format="tif" ,
			 dpi=1000,
			 bbox_inches="tight",
			 pil_kwargs={"compression": "tif_lzw"})
	plt.show()  #显示图形




#1、各群体状态变化控制台

seed_list=seed_create(10000,0.05,0.26)
time_state(600,seed_list,10000,0.3,1,0.05,0.26,0.8)






