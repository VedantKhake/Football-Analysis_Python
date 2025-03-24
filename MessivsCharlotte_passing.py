
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer.pitch import Pitch
import seaborn as sns
df=pd.read_csv("C:/Users/vedan/OneDrive/Desktop/Python viz/messibetis.csv")
df['x']=df['x']*1.2
df['y']=df['y']*0.8
df['endX']=df['endX']*1.2
df['endY']=df['endY']*0.8
fig,ax=plt.subplots(figsize=(13.5,6))
fig.set_facecolor('#22312b')
ax.patch.set_facecolor('#22312b')

pitch = Pitch(pitch_color='black', line_color='white', stripe=False)
pitch.draw(ax=ax)
plt.gca().invert_yaxis()
for x in range(len(df['x'])):
               if df['outcome'][x]=='Successful':
                plt.plot((df['x'][x], df['endX'][x]), (df['y'][x], df['endY'][x]), color='green')
                plt.scatter(df['x'][x],df['y'][x],color='green')
               if df['outcome'][x]=='Unsuccessful':
                plt.plot((df['x'][x], df['endX'][x]), (df['y'][x], df['endY'][x]), color='red')
                plt.scatter(df['x'][x],df['y'][x],color='red')
plt.title('Messi Pass Map vs Charlotte',color='White',size=22)
plt.show()