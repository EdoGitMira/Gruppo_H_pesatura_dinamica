import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
import Function
list = Function.open_data()
temp_env=list[0]
temp_cell=list[1]
volt_cell=list[2]
volt_std_mean=list[3]
volt_std=list[4]
time=list[5]
initial_time=list[6]
print(initial_time)
time_sec = [(el - initial_time).total_seconds()/1000 for el in time]
mass_cell = [el * 5191.421 - 4874.38 for el in volt_cell]
volt_std_mean=[el * 1000 for el in volt_std_mean]
# Create a figure and a 3D Axes
fig = plt.figure()
ax = Axes3D(fig)
fig.add_axes(ax)
# Create an init function and the animate functions.
# Both are explained in the tutorial. Since we are changing
# the the elevation and azimuth and no objects are really
# changed on the plot we don't have to return anything from
# the init and animate function. (return value is explained
# in the tutorial.
def init():
    ax.scatter(time_sec,volt_std_mean,mass_cell, marker='o', s=20, c="blue", alpha=0.6)
    ax.set_xlabel("Tempo [ks]", fontsize=15, labelpad=20)
    ax.set_ylabel("Deviazione standard [uV/V]", fontsize=15, labelpad=20)
    ax.set_zlabel("Massa [g]", fontsize=15, labelpad=20)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    for t in ax.zaxis.get_major_ticks(): t.label.set_fontsize(10)
    return fig,

def animate(i):
    ax.view_init(elev=10., azim=i/4+30)
    return fig,

# Animate
anim = animation.FuncAnimation(fig, animate, init_func=init,frames=120*4, interval=100, blit=True)

# Save
anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])