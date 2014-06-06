#here i check if I have a result table for each filename and vice versa

import pandas as pd
import sys
sys.path.append("/mnt/moehlc/home/idaf_library/")
import libidaf.idafIO as io
import os



tablefolder = '/mnt/moehlc/idaf/IDAF_Projects/140507_hanna_gags_dataIntegration/data/glueImageCellprofiler'
imfolder = '/mnt/moehlc/idaf/IDAF_Projects/140507_hanna_gags_dataIntegration/data/images/tiff'



csvfiles = io.getFilelistFromDir(tablefolder,'.csv')
imfiles = io.getFilelistFromDir(imfolder,'_C1.tif')


badImfiles = []
for imfile in imfiles:
	csvCnd = io.getFilelistFromDir(tablefolder,['.csv',imfile.replace('_C1.tif','')])
	if len(csvCnd) != 1:
		badImfiles.append(imfile)
		print('achtung: files for '+imfile + ':')
		print(csvCnd)

if len(badImfiles)>0:
	print('found following images without result file:')
	print(badImfiles)
else:
	print('check for images is consistent: each image has exactly one csv file')	



print('..test csvs...\\')
badCsv = []
for csvfile in csvfiles:
	imCnd = io.getFilelistFromDir(imfolder,['.tif',csvfile.replace('.csv','')])
	if len(imCnd) != 3:
		badCsv.append(csvfile)
		print('achtung: files for '+csvfile + ':')
		print(imCnd)

if len(badCsv)>0:
	print('found following csvs without image file:')
	print(badCsv)
else:
	print('check for csvs is consistent: each csv has exactly 3 image files')


pd.Series(badCsv).to_csv('missingImages.csv')
pd.Series(badImfiles).to_csv('missingCellProfilerData.csv')			