import os, sys
from os.path import isfile, join

if len(sys.argv) == 2:
    path = sys.argv[1]
    files_sizes = {
        i: os.stat(i).st_size for i in os.listdir(path) if isfile(join(path, i))
    }
    sorted_files_sizes = {
        k: v for k, v in sorted(files_sizes.items(), key=lambda x: (x[1], x[0]))
    }
    for k, v in sorted_files_sizes.items():
        print(f"{k} - {v} bytes")

else:
    raise Exception("You have to specify file path as a fist argument")
