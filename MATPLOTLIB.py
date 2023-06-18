import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from itertools import count
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn')

date_merge = pd.read_excel('Tien.xlsx')

# date_merge['Tiên'] = pd.to_datetime(date_merge['Tiên'])
# date_merge.sort_values('Tiên', inplace=True)
# data['Tiên']= data['Tiên'].astype(str)
# price_date =data['Tiên']
# price_date = data['Tiên'].astype(str)
# price_close = data['Mạnh']
# plt.plot(price_date)
# plt.plot(price_close)

# date_merge['Tiên'] = date_merge['Tiên'].astype(str)
# ax = date_merge.plot(x ="Tiên" , y="Mạnh" ,figsize=[15, 5], linewidth=0.6, alpha=0.6, color="#003399", kind="scatter")
# kind="scatter" ,figsize=[15, 5], linewidth=0.1, alpha=0.6, color="#003399",



# plt.plot_datetime.time(price_date, price_close, linestyle='solid')
def animate(i):
    x = date_merge['Tiên'].astype(str)
    y1 =date_merge['Mạnh'] 
    y2 =date_merge['Đạt']
    plt.cla()

    plt.plot(x,y1,label ='t1')
    plt.plot(x,y2,label ='t2')
    plt.gcf().autofmt_xdate()
    plt.legend()
ani = FuncAnimation(plt.gcf(), animate, interval=1000,frames= 500, repeat= False   )

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

    
plt.legend(loc='upper left')
plt.tight_layout()

plt.show()