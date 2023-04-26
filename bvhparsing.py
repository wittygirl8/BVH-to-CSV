#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys

boneName = []
frameCount = 0

# if (len(sys.argv)!=2):
#     print ('Usage: python bvhparser.py path/to/filename')
#     sys.exit()

filename = "C:/Users/Dell/Downloads/BVHExtract.bvh"
    # sys.argv[1]

text_file = open(filename, "r")
f = data = text_file.read()
words = f.split()
addNext = False


for word in words:
    if addNext:

        boneName.append(word + 'Xpos')
        boneName.append(word + 'Ypos')
        boneName.append(word + 'Zpos')
        boneName.append(word + 'Yrot')
        boneName.append(word + 'Xrot')
        boneName.append(word + 'Zrot')

        addNext = False

    if word == 'ROOT' or word == 'JOINT':
        addNext = True

    if word == 'Frames:':
        frameCount = int(words[words.index('Frames:')+1])
    if word == 'Time:':
        words = words[words.index('Time:')+2:]
        break

data = [[] for _ in range(len(boneName))]
size = len(boneName)


count = 0
for word in words:
    bin = count % size
    data[bin].append(word)
    count+=1


f = open(filename[:filename.index('.')] + ".csv",'w')
f.write('Frames,')
for i in range(1, frameCount+1):
    f.write(str(i) + ',')
f.write('\n')

count = 0
for name in boneName:
    f.write(name + ',')
    for word in data[count]:
        f.write(word + ',')
    f.write('\n')
    count+=1

f.close()
text_file.close()


# In[3]:


import pandas as pd

df = pd.read_csv('C:/Users/Dell/Downloads/BVHExtract.csv')


# In[4]:


df


# In[128]:



df1 = df.fillna(0)


# In[129]:


print(df1)
# list(df1)


# In[130]:


import plotly.express as px

nparray = df1.to_numpy()
l = len(nparray[0][1:])+1
xrange = [i for i in range(1,l)]
yrange = nparray[0][1:]

fig = px.line( x=xrange, y=yrange, title='Time Series with Rangeslider')
fig.update_xaxes(rangeslider_visible=True)
fig.show()


# In[52]:


import matplotlib.pyplot as plt

ax = plt.axes(projection='3d')
zline = df['1']
xline = df['2']
yline = df['3']
ax.plot3D(xline, yline, zline, 'black')
    
zdata = df['1']
xdata = df['2']
ydata = df['3']
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');


# In[ ]:




