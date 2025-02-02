import re
import numpy as np
import matplotlib.pyplot as plt
import sys

#put all file names you want to plot here or use CLI
namelist = [
'FILENAME.npy',
'FILENAME.npy'
]

#Command Line Interface usage:
#
#
# ~/projectdir/history/ $ python plotting.py *
#
#This command plots all the history files in the
#same directory as the plotting program.

if len(sys.argv) > 1:
  namelist = [sys.argv[i+1] for i in range(len(sys.argv)-1) if sys.argv[i+1].endswith('.npz')]

plotlist = []

for name in namelist:
  plotlist.insert(0, np.load(name)['arr_0'].item()['val_acc'])

for i in range(len(namelist)):
  plt.xlabel('epoch')
  plt.ylabel('validation accuracy')
  filename =re.search('([^/\s]+)([\s]?)+$', namelist[i]).group(1)
  filename = filename[:-11]
  plt.title('val_acc for ' + filename)
  plt.plot(plotlist[len(plotlist)-i -1])
  plt.savefig('history/' + filename + '.pdf')
  plt.show()


