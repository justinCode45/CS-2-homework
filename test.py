import matplotlib.animation as animation 
import matplotlib.pyplot as plt   
def animate(n):     
    scatter = ax.scatter(n, n)     
    if n == 0:         
        return ax.get_children()[0],     
    else:         
        return ax.get_children()[:n]   
fig, ax = plt.subplots() 
ax.set_xlim(0, 20) 
ax.set_ylim(0, 20)  
ani = animation.FuncAnimation(fig, animate, interval=100, blit=True) 
plt.show()