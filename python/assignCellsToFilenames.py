import pandas as pd
import sys
import sys
#sys.path.append("/Volumes/moehlc/idaf_library/lib idaf")
sys.path.append("/mnt/moehlc/home/idaf_library/")
import libidaf.idafIO as io
import os


def getNamesByNr(folder):
	filesTiff = io.getFilelistFromDir(folder,'.tiff')
	fileTiff = filesTiff[0]

	# generate list with tuples of image numbers and filenames
	numbersAndNames = [] 
	for fileTiff in filesTiff:
		fileNr = int(fileTiff[0:3])
		fileName = fileTiff[4:]
		numbersAndNames.append((fileNr,fileName))
	#sort by number
	numbersAndNames = sorted(numbersAndNames, key = lambda x: x[0])

	namesByNr = {} #dict with filenames, keyed by their cellprofiler image number
	for i in range(len(numbersAndNames)):
		namesByNr[i+1] = numbersAndNames[i][1]
	return namesByNr	


def getCellProfilerDataByNr(folder,namesByNr):
	# load cell profiler data 
	celldatname = folder + '/DefaultOUT_SingleCellsInfected.csv'
	dat = pd.read_csv(celldatname)
	dat = dat[['ImageNumber','AreaShape_Center_X','AreaShape_Center_Y']]
	dat.columns = ['imNr','x','y'] # clean data table


	posImNrs = dat['imNr'].unique() # these image numbers are present in the cell profiler data

	datByNr = {}  # dict of dataframes, keyed by image number

	for nr in posImNrs:
		datsel = dat[dat['imNr'] == nr]
		datsel.insert(3,'filename',namesByNr[nr])
		datByNr[nr] = datsel

	return datByNr	


rootfolder = '/mnt/moehlc/idaf/IDAF_Projects/140507_hanna_gags_dataIntegration/data/cellProfiler'
savefolder = '/mnt/moehlc/idaf/IDAF_Projects/140507_hanna_gags_dataIntegration/data/glueImageCellprofiler'

folders = io.getFilelistFromDir(rootfolder,'V')
folder = folders[3]


namesByNr = getNamesByNr(rootfolder + '/' + folder)
datByNr = getCellProfilerDataByNr(rootfolder + '/' + folder,namesByNr)