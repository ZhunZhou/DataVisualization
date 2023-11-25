# importing required libraries
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("data.csv")
df = df.dropna()
df.columns = ["id"] + list(df.columns[1:])

df = df[df.columns[:-1]]

df["colorScale"] = df.apply(lambda row: 1 if row[df.columns[1]] < 60 else 0, axis=1)

fig = go.Figure(
    data=[
        go.Scatter3d(
            x=df[df.columns[1]],
            y=df[df.columns[2]],
            z=df[df.columns[3]],
            hovertemplate="<b>%{text}</b><extra></extra>",
            text=[title for title in df[df.columns[0]]],
            mode="markers",
            marker=dict(size=4, color=df["colorScale"], colorscale="Jet", opacity=0.8),
        )
    ]
)

fig.update_layout(
    scene=dict(
        xaxis_title=df.columns[1], yaxis_title=df.columns[2], zaxis_title=df.columns[3]
    ),
    width=700,
    margin=dict(r=20, b=10, l=10, t=10),
)

fig.show()
