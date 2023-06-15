import os

os.chdir('D:/Sami/Sami/Python/rename')

for f in os.listdir():
    fname, fext = os.path.splitext(f)
    #print(fname)
    ftitle, fcourse, fnum = fname.split('-')
    fnum, ftitle = fnum.strip()[1:].zfill(2), ftitle.strip()
    new_name = '{}-{}{}'.format(fnum, ftitle, fext)
    print(new_name)
    os.rename(f, new_name)