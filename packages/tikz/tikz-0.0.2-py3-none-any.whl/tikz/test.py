import numpy as np
import tikz

K = 1000
x = np.linspace(0, 1.001, K)
y = 3*np.sin(2*np.pi*x) + 0.5*np.random.randn(K)
z = 3*np.cos(2*np.pi*x) + 0.5*np.random.randn(K)
u = np.zeros((2, K))
u[0, :] = np.row_stack((y, z)).min(axis=0) - 2
u[1, :] = np.row_stack((y, z)).max(axis=0) + 2

fig = tikz.Fig('test')
fig.xlabel = 'x axis'
fig.ylabel = 'y axis'
fig.path(x, u, thickness=0, opacity=0.2)
fig.path(x, y, label='first')
fig.path(x, z, label='second')
fig.render()
