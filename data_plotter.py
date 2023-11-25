# importing required libraries
import plotly.graph_objects as go

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data.csv")
df = df.dropna()
df.columns = ["id"] + list(df.columns[1:])

df = df[df.columns[:-1]]
print(df)
# creating figure
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

c = df[df.columns[1]] < 60
cmap = "coolwarm"
# creating the plot
plot = ax.scatter(
    df[df.columns[1]], df[df.columns[2]], df[df.columns[3]], c=c, cmap=cmap
)

# setting title and labels
ax.set_title("Correlation plot")
ax.set_xlabel(df.columns[1])
ax.set_ylabel(df.columns[2])
ax.set_zlabel(df.columns[3])

ax.set(xlim=(0, 200), ylim=(0, 120), zlim=(0, 250))

# ax.text(df[df.columns[1]], df[df.columns[2]], df[df.columns[3]], df[df.columns[0]])

# displaying the plot
plt.show()
