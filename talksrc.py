# Plot area
figure.figsize: 10, 7.5 #powerpoint dimensions
figure.facecolor: white
figure.edgecolor: white
axes.facecolor : white
axes.grid: False
 
# Axes and ticks
axes.linewidth: 2 #width of label text scales with this
axes.edgecolor: black
xtick.direction: in
ytick.direction: in
xtick.major.size: 12
xtick.major.width: 2
# xtick.minor.size: 10
# xtick.minor.width: 2
ytick.major.size: 12
ytick.major.width: 2
# ytick.minor.size: 10
# ytick.minor.width: 2
 
# Space ticklabels
ytick.major.pad: 5
ytick.minor.pad: 5
xtick.major.pad: 10
xtick.minor.pad: 10

# Fonts and font sizes
text.usetex: False
font.style : normal
font.sans-serif : Arial, Helvetica, Bitstream Vera Sans, Lucida Grande, Verdana, Geneva, Lucid, Avant Garde, Gill Sans MT, sans-serif
font.family : sans-serif
mathtext.default : regular
font.size: 24
# font.weight : black 
# weights = 'light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black'
axes.titlesize: medium
# axes.labelsize: large
# axes.labelweight : normal
# xtick.labelsize: large
# ytick.labelsize: large
# relative font sizes = xx-small, x-small, small, medium, large, x-large, xx-large, larger, or smaller

# Legend
# legend.fancybox : False
legend.shadow : True
legend.fontsize: 24
legend.frameon : True
# legend.linewidth : 2
 
# default colormap
image.cmap: gray
 
# Plot elements
lines.linewidth: 4
lines.markersize: 25
axes.color_cycle    : 5DA5DA, FAA43A, 60BD68, F17CB0, B2912F, B276B2, DECF3F, F15854, 4D4D4D
 
# savefig options (avoid clipping at margins)
savefig.bbox : tight
savefig.pad_inches : 0.2
savefig.format : png
# savefig.dpi : 300