# -*-coding:utf-8 -*-
import tushare as ts 
import pandas as pd 
import matplotlib.pyplot as plt


start_date='2020-01-01'
end_date = '2020-02-28'
obs_present = 0.3
com_percent = 0.1
profit_list = []
cnt = 0

stock_list = ts.get_stock_basics()['name']
for code,name in stock_list.iteritems():  #返回tuple类型
    if name.find("ST") != -1:
    	continue
    df = ts.get_k_data(code,start=start_date,end=end_date,ktype='D',autype='qfq')
    if len(df) <10:
    	continue
    print(cnt,code,name)

    df.index = df.pop('date')
    winsize = int(len(df)*obs_present)

    winsize = 2
    profit_1 = int((df['close'][winsize-1]-df['close'][0])/df['close'][0]*100)
    profit_2 = int((df['close'][-1]-df['close'][-winsize])/df['close'][-winsize]*100) #取该值

    profit_list.append(dict(code=code,pf1=profit_1,pf2=profit_2))


    cnt+=1
    # if cnt>100:
    # 	break
profit_list.sort(key= lambda x:x['pf1'],reverse=True) #从小到大为正序
#列表中增加排名信息
for idx,doc in enumerate(profit_list):
	doc['rank_1'] = idx 
num_cands = int(len(profit_list)*com_percent)
top_cands = profit_list[:num_cands-1]
btm_cands = profit_list[-num_cands:]
top_group_code = set([doc['code'] for doc in top_cands])  #股票代码做集合方便快速查找（不使用线性查找）
btm_group_code = set([doc['code'] for doc in btm_cands])

avg_top_idx = round(sum([doc['rank_1'] for doc in top_cands])/num_cands/len(profit_list),2)
avg_btm_idx = round(sum([doc['rank_1'] for doc in btm_cands])/num_cands/len(profit_list),2)
avg_mid_idx = (0+len(profit_list))/2/len(profit_list)

#时间段2 全市股票收益统计
profit_list.sort(key= lambda x:x['pf2'],reverse=True)
#列表中增加第二段时间排名信息
for idx,doc in enumerate(profit_list):
	doc['rank_2'] = idx 
cmp_avg_top_idx = round(sum([doc['rank_2'] for doc in profit_list if doc['code'] in top_group_code ])/num_cands/len(profit_list),2)
cmp_avg_btm_idx = round(sum([doc['rank_2'] for doc in profit_list if doc['code'] in btm_group_code])/num_cands/len(profit_list),2)



print('top_group:',avg_top_idx,'->',cmp_avg_top_idx,"(avg:%.2f)"%avg_mid_idx)
print('btm_group:',avg_btm_idx,'->',cmp_avg_btm_idx,"(avg:%.2f)"%avg_mid_idx)


profits =pd.DataFrame({'pf1':[doc['pf1'] for doc in profit_list],
					   'pf2':[doc['pf2'] for doc in profit_list]})
profits.plot.hist(bins=200,alpha=0.5)
plt.show()