"""
this is the programming to search a file, and it shows the location of the file.

"""



import os
import sys


def pywhich(root, target):
    subfolders = [f.path for f in os.scandir(root) if f.is_dir() ]

    results=[]
    for sub in subfolders:
        try:
            if(target in os.listdir(sub)):
                #print(sub+"/"+target)
                results.append(sub+"/"+target)
        except:
            pass
    
    if(target in os.listdir(root)):
        #print(root+"/"+target)
        results.append(sub+"/"+target)

    return results


root= os.getcwd()

try:
    target=sys.argv[1]
except:
    print("""which [filename]    show the location of the file
          """)
    exit()


pywhich(root, target)
