# -*-coding:utf-8 -*-

import tushare as ts 
import pandas as pd 
import matplotlib.pyplot as plt 

start_date = "2018-01-01"
end_date = "2020-02-35"
obs_percent = 0.3
cmp_percent = 0.1
cnt = 0

stock_list = ts.get_stock_basics()['name']
pf_list = []
for code,name in stock_list.iteritems():
	if name.find('ST') != -1:
		continue
	df = ts.get_k_data(code,start=start_date,end=end_date,ktype="D",autype="qfq")
	if len(df)<400:
		continue
	print(cnt,code,name)
	df.index = df.pop('date')
	win_size = int(len(df)*obs_percent)

	profit_1 = int((df['close'][win_size-1]-df['close'][0])/df['close'][0]*100)
	profit_2 = int((df['close'][-1]/df['close'][-win_size]-1.0)*100)

	if profit_1>150 or profit_2>150:
		continue

	pf_list.append(dict(code=code,pf1=profit_1,pf2=profit_2))

	cnt+=1	
	if cnt>=100:
	    break

pf_list.sort(key=lambda x:x['pf1'],reverse=True)

for idx,doc in enumerate(pf_list):
	doc['rank_1'] = idx

num_cands = int(len(pf_list)*cmp_percent)
top_cands = pf_list[:num_cands]     #组合1
btm_cands = pf_list[-num_cands:]    #组合2
top_group_code = set([doc['code'] for doc in top_cands])
btm_group_code = set([doc['code'] for doc in btm_cands])

avg_top_idx = round(sum([doc["rank_1"] for doc in top_cands])/num_cands/len(pf_list),2)
avg_btm_idx = round(sum([doc["rank_1"] for doc in btm_cands])/num_cands/len(pf_list),2)
avg_mid_idx = (0+len(pf_list)-1)/2/len(pf_list)   #  ==0.5

#第二段时间step2

pf_list.sort(key=lambda x:x['pf2'],reverse=True)
for idx,doc in enumerate(pf_list):
	doc['rank_2'] = idx


cmp_avg_top_idx = round(sum([doc["rank_2"] for doc in pf_list if doc['code'] in top_group_code])/num_cands/len(pf_list),2)
cmp_avg_btm_idx = round(sum([doc["rank_2"] for doc in pf_list if doc['code'] in btm_group_code] )/num_cands/len(pf_list),2)

print('top_group:',avg_top_idx,"->",cmp_avg_top_idx,"(avg:%.2f)"%avg_mid_idx)
print('btm_group:',avg_btm_idx,"->",cmp_avg_btm_idx,"(avg:%.2f)"%avg_mid_idx)

						
profits = pd.DataFrame({'pf1':[doc['pf1'] for doc in pf_list],
	                    'pf2':[doc['pf2'] for doc in pf_list]
						})
profits.plot.hist(bins=200,alpha=0.5)
plt.show()
