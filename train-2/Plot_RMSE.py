# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 18:42:07 2023

@author: Administrator
"""
from pylab import *
import matplotlib.pyplot as plt
import numpy as np
##set figure properties
aw = 2
sizea = 17
fs = sizea
lw = 3.0
font = {'size'   : fs}
matplotlib.rc('font', **font)
matplotlib.rc('axes' , linewidth=aw)
def set_fig_properties(ax_list):
    tl = 10
    tw = 2
    tlm = 3
    
    for ax in ax_list:
        ax.tick_params(which='major', length=tl, width=tw)
        ax.tick_params(which='minor', length=tlm, width=tw)
        ax.tick_params(which='both', axis='both', direction='out', right=False, top=False)


loss_5 = loadtxt('loss.out')
loss_5[:,0] = np.arange(1, len(loss_5) + 1)*100
energy_test_5 = loadtxt('energy_test.out')
force_test_5 = loadtxt('force_test.out')
virial_test_5 = loadtxt('virial_test.out')

energy_test_plt = loss_5[:,5] 
print(loss_5[-1,7],loss_5[-1,8],loss_5[-1,9])
NEP_force = loss_5[-1,8]*1000
NEP_energy = loss_5[-1,7]*1000
NEP_virial = loss_5[-1,9]*1000

mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['font.size'] = sizea
mpl.rcParams['font.family'] = 'Arial'
plt.rc('xtick', labelsize=17)
labelpad_all =2 
labelpad_2 = 10
markersize_all =12
fontsizess = 28
sizea = 19
linewidth_all = 2.5
fs = sizea
figure(figsize=(14, 12))
ax1 = subplot(2, 2, 1)
set_fig_properties([gca()])
loglog(loss_5[:, 0], loss_5[:, 4],  linestyle="-", linewidth=lw, label="Energy_train",color="C1")
loglog(loss_5[:, 0], loss_5[:, 5],  linestyle="-", linewidth=lw, label="Force_train",color="C4")
loglog(loss_5[:, 0], loss_5[:, 6],  linestyle="-", linewidth=lw, label="Virial_train",color="#8c564b")
loglog(loss_5[:, 0], loss_5[:, 7],  linestyle="-", linewidth=lw, label="Energy_test",color="C0")
loglog(loss_5[:, 0], loss_5[:, 8],  linestyle="-", linewidth=lw, label="Force_test",color="C2")
loglog(loss_5[:, 0], loss_5[:, 9],  linestyle="-", linewidth=lw, label="Virial_test",color="C3")
xlim([5e1, 2e6])
ylim([1e-3, 6e1])
plt.xlabel('Generation',fontsize=fontsizess,labelpad =labelpad_all)
plt.ylabel('Loss',fontsize=fontsizess)
legend(loc="upper center",  
        ncol = 2, 
        fontsize = sizea, 
        frameon = False,
        columnspacing = 0.2)
# title("cut off 8 4 n_max 6 4 neuron 100")
subplot(2, 2, 2)
ax2 = subplot(2, 2, 2)
set_fig_properties([gca()])
x2 = [np.min(energy_test_5[:, 0])-0.5 ,np.max(energy_test_5[:, 0])+0.5]
y2 = [np.min(energy_test_5[:, 0])-0.5 ,np.max(energy_test_5[:, 0])+0.5]
plot(energy_test_5[:, 1], energy_test_5[:, 0], '.', color="C0", markersize = 12)
plot(x2,y2,'-', color="C0",linewidth=2.5)
plt.xlabel('DFT energy (eV/atom)',fontsize=fontsizess,labelpad =labelpad_2)
plt.ylabel('NEP energy (eV/atom)',fontsize=fontsizess)
plt.text(0.05, 0.9, s=f'RMSE: {NEP_energy:.1f} meV/atom', fontsize=22,
         bbox=dict(facecolor="C0", alpha=0.5),transform=ax2.transAxes)
xlim([-7.45, -6.5])
ylim([-7.45, -6.5])

subplot(2, 2, 3)
ax3 = subplot(2, 2, 3)
set_fig_properties([gca()])
plot(force_test_5[:, 3:6], force_test_5[:, 0:3], '.', color="C2", markersize = 12)
x3 = [np.min(force_test_5[:, 3:6])-10 ,np.max(force_test_5[:, 3:6])+10]
y3 = [np.min(force_test_5[:, 3:6])-10,np.max(force_test_5[:, 3:6])+10]
plot(x3,y3,'-', color="C2",linewidth=2.5)
plt.xlabel(r'DFT force (eV/$\rm{\AA}$)',fontsize=fontsizess)
plt.ylabel(r'NEP force (eV/$\rm{\AA}$)',fontsize=fontsizess)
plt.text(0.05, 0.9, s=f'RMSE: {NEP_force:.1f} meV/$\mathregular{{\AA}}$', fontsize=22, 
         bbox=dict(facecolor="C2", alpha=0.5),transform=ax3.transAxes)
xlim([-53, 53])
ylim([-53, 53])


subplot(2, 2, 4)
ax4 = subplot(2, 2, 4)
set_fig_properties([gca()])
plot(virial_test_5[:, 0:2], virial_test_5[:, 6:8], '.', color="C3", markersize = 10)

x4 = [np.min(virial_test_5[:, 1])-5 ,np.max(virial_test_5[:, 1])+5]
y4 = [np.min(virial_test_5[:, 1])-5 ,np.max(virial_test_5[:, 1])+5]
plot(x4,y4,'-', color="C3",linewidth=2.5)
plt.xlabel('DFT virial (eV/atom)',fontsize=fontsizess,labelpad =labelpad_2)
plt.ylabel('NEP virial (eV/atom)',fontsize=fontsizess)
plt.text(0.05, 0.9,s=f'RMSE: {NEP_virial:.1f} meV/atom', fontsize=22, 
         bbox=dict(facecolor="C3", alpha=0.5),transform=ax4.transAxes)
xlim([-2, 3.5])
ylim([-2, 3.5])

subplots_adjust(wspace=0.35, hspace=0.28)
savefig("RMSE_all_5.png", bbox_inches='tight',dpi=600)