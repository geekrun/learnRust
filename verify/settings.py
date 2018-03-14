import os
import sys

PROJECTPATH = os.path.dirname(__file__)
STATICPATH = os.path.join(PROJECTPATH, 'static')
sys.path.append(PROJECTPATH)

if __name__ == "__main__":
	print(STATICPATH)
