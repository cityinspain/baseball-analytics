import glob

pyfiles = glob.glob("./*_*.py")


for pf in pyfiles:
    file_changed = False
    with open(pf) as f:
        file_lines = f.read().splitlines()
        if (len(file_lines) > 0):

            file_firstline = file_lines[0]
            if (file_firstline == "#!/usr/bin/env python"):
                file_lines[0] = file_firstline+"3"
                file_changed = True



    if (file_changed):

        print('file ', pf, 'was changed')

        with open(pf, 'w') as f:
            f.write("\n".join(file_lines))
