from bokeh.plotting import figure, curdoc
import pandas as pd
from bokeh.layouts import column
import numpy as np
import 

# load data
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep']
df = pd.read_csv('pivot_table.csv')
k = [df['01'].sum(), df['02'].sum(), df['03'].sum(), df['04'].sum(), df['05'].sum(), df['06'].sum(), df['07'].sum(), df['08'].sum(), df['09'].sum()]
norm = []
for i in k:
        norm.append(i/233)


name1 = str(df.post.iloc[0])
name2 = str(df.post.iloc[1])
avrg_time = df.iloc[0]
avrg_time1 = df.iloc[1]
avrg = avrg_time.to_numpy()
avrg1 = avrg_time1.to_numpy()

avrg = np.delete(avrg, 0)
avrg1 = np.delete(avrg1, 0)

p = figure(x_range=months, title='Response time in NYC depending on zipcode')
r1 = p.line(months, avrg, legend_label='line1', color='pink', line_width=2)
r2 = p.line(months, avrg1, legend_label='line2', color='green', line_width=2)
r3 = p.line(months, norm, color='orange', legend_label='average', line_width=2)

ds1 = r1.data_source
ds2 = r2.data_source

def change_line1(i):
    new_data = {}
    #namen = str(df.post.iloc[i])
    #ds1.legend_label = namen
    avrg_timen = df.iloc[i]
    avrgn = avrg_timen.to_numpy()
    avrgn = np.delete(avrgn, 0)
    new_data['x'] = months
    new_data['y'] = avrgn
    ds1.data = new_data


def change_line2(i):
    new_data = {}
    #namen = str(df.post.iloc[i])
    #ds2.legend_label = namen
    avrg_timen = df.iloc[i]
    avrgn = avrg_timen.to_numpy()
    avrgn = np.delete(avrgn, 0)
    new_data['x'] = months
    new_data['y'] = avrgn
    ds2.data = new_data



# change_line1(2)
# generate plots
#p = figure(x_range=(0,10), y_range=(0,10))
#r = p.circle(avrg, [1,2,3,4,5,6,7], size = 5)

# handle callbacks
#ds1 = r1.data_source
#ds2 = r2.data_source

#def replace_linei():
 #   new_data={}
  #  new_data['months'] = months
  #  new_data[''] = ds.data['y'] + [random()*10]
   # ds.data = new_data

# create interactive widgets
#b = Button(label="Add Circle")
#b.on_click(add_circle)

# format/create the document
curdoc().add_root(column(p))
