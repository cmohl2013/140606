import pandas as pd
import sys
import sys
#sys.path.append("/Volumes/moehlc/idaf_library/lib idaf")
sys.path.append("/mnt/moehlc/home/idaf_library/")
import libidaf.idafIO as io



rootfolder = '/mnt/moehlc/idaf/IDAF_Projects/140507_hanna_gags_dataIntegration/data/cellProfiler'


folders = io.getFilelistFromDir(rootfolder,'V')

folder = folders[1]

filesTiff = io.getFilelistFromDir(rootfolder + '/' + folder,'.tiff')

fileTiff = filesTiff[0]

for fileTiff in filesTiff:
	fileNr = int(fileTiff[0:3])
	fileName = fileTiff[4:]

	#print fileNr
	#print fileName

