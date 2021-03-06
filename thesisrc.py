# color cycle
axes.prop_cycle: cycler('color', ['4c72b0', '55a868', 'c44e52', '8172b2', 'ccb974', '64b5cd']) 

# Plot area
figure.figsize: 10, 8
figure.facecolor: white
figure.edgecolor: white
axes.facecolor : white
axes.grid: False
 
# Axes and ticks
axes.linewidth: 2
axes.edgecolor: black
xtick.direction: in
ytick.direction: in
xtick.major.size: 10
xtick.major.width: 2
xtick.minor.size: 10
xtick.minor.width: 2
ytick.major.size: 10
ytick.major.width: 2
ytick.minor.size: 10
ytick.minor.width: 2
 
# Space ticklabels
ytick.major.pad: 5
ytick.minor.pad: 5
xtick.major.pad: 10
xtick.minor.pad: 10
 
# Fonts and font sizes
font.family: serif
font.serif: Computer Modern
# font.weight : black # 'light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black'
text.usetex: True  # All text will be in the LaTeX font.
font.size: 20
axes.titlesize: 20
axes.labelsize: 18
xtick.labelsize: 20
ytick.labelsize: 20
legend.fontsize: 18
 
image.cmap: viridis
 
# Plot elements
lines.linewidth: 4
lines.markersize: 18
 
# savefig options (avoid clipping at margins)
savefig.bbox : tight
savefig.pad_inches : 0.2