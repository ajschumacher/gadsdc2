
#Time Series Graphs
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file = 'P:/Projects/Metro Exports/Profiles/Python Viz/CBSA_Totals.csv'
data = pd.read_csv(file)

item_list = data['cbsa_name'].unique()

for elem in item_list:
	current = data[data['cbsa_name'] == elem]
	#Data
	x1 = list(current['real_exports_pcb'])
	x2 = list(current['real_exports_fpb'])
	y = current['year']
	#Graph
	fig = plt.figure()
	ax = plt.subplot(111)
	ax.plot(y, x1, 'c-', label='Non-FAF Adjusted')
	ax.plot(y, x2, 'b-', label='FAF Adjusted')
	#Y Axis
	ymax_row = max(x1, x2)
	ymax = max(ymax_row)
	ax.set_ylim(0, ymax)
	#X Axis
	ax.set_xlim(left=2003, right=2013)
	ax.set_xticks([2003,2008,2013])
	#Legend
	box = ax.get_position()
	ax.set_position([box.x0, box.y0, box.width, box.height * 0.80])
	ax.legend(loc='upper center', bbox_to_anchor=(.5,1.3))
	#Labels
	fig_title = str(elem)
	ax.set_title(fig_title)
	ax.set_xlabel('Year')
	ax.set_ylabel('Real Exports, (mil. USD 2013)')
	#Save PNG
	loc = 'P:/Projects/Metro Exports/Profiles/Python Viz/Trend Figures/%s.png' % elem.replace(',','').replace(' ','')
	plt.savefig(loc)
plt.close('all')


#Bubble Chart Industry Charts
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file = 'P:/Projects/Metro Exports/Profiles/Python Viz/CBSA_Industry.csv'

data = pd.read_csv(file)

data['rank'] = data.groupby(['cbsa_name'])['growth_03_13_fpb'].rank(ascending=True)
#data.rank_vol = data.groupby(['cbsa_name'])['real_exports_fpb'].rank(ascending=False)
#data.rank_gro = data.groupby(['cbsa_name'])['growth_03_13_fpb'].rank(ascending=False)

geo_list = data['cbsa_name'].unique()

for geo in geo_list:
    geo_i = data[data['cbsa_name'] == geo]
    x = geo_i['rank']
    y = geo_i['growth_03_13_fpb']
    y = y * 100
    labels = list(geo_i['naics_3'])
    colors = np.random.rand(30)
    area = geo_i['real_exports_fpb']/10
    fig = plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    ax = plt.subplot(111)
    ax.set_ylabel('Annualized Export Growth (%), 2003-2013')
    ax.set_xlabel('Bubble area scales with industry export volume')
    fig_title = str(geo) + ':' + '\nExport Volume and Growth by Industry'
    ax.set_title(fig_title)  
    plt.title(fig_title, y=1.10, fontsize=15)
    #plt.text(0.5, 3, fig_title, horizontalalignment='center')
    #ax.legend(loc='upper center', bbox_to_anchor=(.5,1.3))
    ax.set_xticks([],[])
    ax.set_xticklabels([],[])
    plt.grid(True)
    #fig.set_figwidth(24.)
    #ax.set_xscale(np.arange(-1, 41, .5))
    for label, x, y in zip(labels, x, y):
        plt.annotate(
        label, 
        xy = (x, y), xytext = (0, 15),
        textcoords = 'offset points', rotation=270, ha = 'center', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.2', fc = 'MintCream', alpha = 0.3),
        arrowprops = dict(arrowstyle = '-|>', connectionstyle = 'arc3,rad=0'),fontsize=6)
    plt.tight_layout()
    loc = 'P:/Projects/Metro Exports/Profiles/Python Viz/Bubble Figures/%s.png' % geo.replace(',','').replace(' ','')
    plt.savefig(loc, dpi=500)
    plt.close('all')


#Scatter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#file = 'P:/Projects/Metro Exports/Profiles/Python Viz/CBSA_Totals.csv'
file = 'C:/Users/Nick/Desktop/Viz/CBSA_Totals.csv'
data = pd.read_csv(file)
data = data[data.year == 2013]
x = data['real_exports_pcb']
y = data['real_exports_fpb']
fig = plt.scatter(x,y)
ax = plt.subplot(111)
ax.set_title('Metro Export Totals (mil.) 2013')
ax.set_ylabel('FAF adjusted')
ax.set_xlabel('non-FAF adjusted')
#plt.show()
loc = 'C:/Users/Nick/Desktop/Viz/Scatter.png'
plt.savefig(loc, dpi=200)


#Ranked Bar Charts
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file = 'P:/Projects/Metro Exports/Profiles/Python Viz/CBSA_Totals.csv'
data = pd.read_csv(file)


#data2 = data[data.year == 2013]
#data2 = data2.sort(['real_exports_fpb'], ascending=[1, 0])

x = data.real_exports_fpb
y = data.cbsa_names
pyplot.bar(x,y)



#plt.figure(figsize=(3, 8))
for yr in data2['year']:
    current = data2[data2['year'] == yr]
    exports = data2['real_exports_fpb']
    metro = list(data2['cbsa_name'])
    pos = np.arange(len(exports))
    plt.title('Real Exports, (mil. USD 2013)')
    plt.barh(pos, exports)
    #for p, m, x in zip(pos, metro, exports):
    #    plt.annotate(str(x), xy=(x + 1, pos + .5), va='center')

    ticks = plt.yticks(pos + .5, metro)
    xt = plt.xticks()[0]
    plt.xticks(xt, [' '] * len(xt))
#minimize chartjunk
#remove_border(left=False, bottom=False)
    plt.grid(axis = 'x', color ='white', linestyle='-')

#set plot limits
#plt.ylim(pos.max() + 1, pos.min() - 1)
#plt.xlim(0, 30)
    pylab.show()
    #loc = 'P:/Projects/Metro Exports/Profiles/Python Viz/Bar Chart Figures/figure.png'
    #plt.savefig(loc)


