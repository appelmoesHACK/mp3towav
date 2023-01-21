# copyright appelmoesGG

import os
os.chdir('/mnt/chromeos/MyFiles/klanken/Instrumenten')

for dir in os.listdir():
    os.chdir('/home/appelmoes/Documents/klanken/Instrumenten/' + dir)
    for filename in os.listdir():
        f = filename
        if os.path.isfile(f):
           f = str(f)
           nomp3 = f.replace('.mp3', '')
           os.system('mpg321 -q -w ' +  nomp3 + ".wav " + f)
           print('Converted ' + f)
    os.system('rm *.mp3')
    os.chdir('/home/appelmoes/Documents/klanken/Instrumenten/')
    print('Finsished with ' + dir)
