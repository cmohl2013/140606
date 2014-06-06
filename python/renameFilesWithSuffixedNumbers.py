

import re
import pandas as pd
import sys
#sys.path.append("/Volumes/moehlc/idaf_library/lib idaf")
sys.path.append("/mnt/moehlc/home/idaf_library/")
import libidaf.idafIO as io
import os


folder = '/mnt/moehlc/idaf/IDAF_Projects/140507_hanna_gags_dataIntegration/data/images/lsm_new/'

fnames = io.getFilelistFromDir(folder,['.lsm'])
fnamesout = []
for fname in fnames:

	newname = re.sub('^([0-9]){3}_','',fname)
	os.rename(folder + fname,folder + newname)
