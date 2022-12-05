import bzip
import sys

opener = bzip.open

if __name__ == '__main__':
    f = bzip.open(sys.argv[1], mode='wt')
    f.write(' '.join(sys.argv[2:]))
    f.close()
