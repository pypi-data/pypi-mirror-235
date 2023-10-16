import numpy as np
import cbx as cbx
import cbx.objectives as obj
from cbx.utils.scheduler import scheduler, multiply
from cbx.plotting import contour_2D
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D 
from scipy.interpolate import CubicSpline

#%%
kwargs = {'alpha': 1.1,
         'dt': 0.001,
         'sigma': 0.1,
         'lamda': 1.0,
         'd': 2,
         'save_int':1000,
         'track_list': ['x'],
         'max_it': 5000,
         'N': 5,
         'M': 1,}

#%% Set seed and define the objective function
np.random.seed(42)
f = obj.Ackley()

#%% Define the initial positions of the particles
x = np.loadtxt('initial.txt',)[None, :,:]
dyn = cbx.dynamics.CBO(f, x=x, **kwargs)
sched = scheduler(dyn, [multiply(name='alpha', factor=1.01, maximum=1e3)])
x_best = dyn.optimize(sched = sched)

#%% plot particle history
x_hist = dyn.history['x'][1:,...]
#idx = [i for i in range(x_hist.shape[0]) if ((i%5==0) or i<4)]
#x_hist = x_hist[idx, ...]
x_min = -4
x_max = 4

plt.close('all')
fig, ax = plt.subplots(1,1)
contour_2D(f, ax=ax, num_pts=1000, 
           x_min=-4, x_max =4., cmap='coolwarm',
           levels=50)
t = np.linspace(0,1, x_hist.shape[0])
t_eval = np.linspace(0,1, 100 * x_hist.shape[0])
colors = ['xkcd:spruce', 
          'xkcd:seaweed','xkcd:minty green', 
          'xkcd:light seafoam', 'xkcd:grapefruit',
          'xkcd:grapefruit','xkcd:grapefruit', 'xkcd:rose pink']

ax.axis('off')
ax.set_aspect('equal')
ax.set_xlim(x_min,x_max)
ax.set_ylim(x_min,x_max)


for i in range(x_hist.shape[-2]):
    cs_0 = CubicSpline(t, x_hist[:, 0, i, 0])
    cs_1 = CubicSpline(t, x_hist[:, 0, i, 1])
    
    line = Line2D(cs_0(t_eval), cs_1(t_eval), 
                  color='xkcd:spruce',#xkcd:strong blue',
                  alpha=.5,linewidth=3,
                  linestyle='dotted',
                  dash_capstyle='round')
    ax.add_line(line)
    sc_idx = 4
    ax.scatter(x_hist[:sc_idx, 0, i, 0], x_hist[:sc_idx, 0, i, 1], 
               color=colors[:sc_idx], 
               s=52,zorder=3)
#%%   
save = True
if save:
    plt.tight_layout(pad=0.0, h_pad=0, w_pad=0)
    plt.savefig('JOSS.png')
