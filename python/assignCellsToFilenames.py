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
		fileName = fileTiff[4:]\
		.replace('_convOverlay','')\
		.replace('_conv_cy3higherOverlay','')\
		.replace('.tiff','')
		numbersAndNames.append((fileNr,fileName))
	#sort by number
	numbersAndNames = sorted(numbersAndNames, key = lambda x: x[0])

	namesByNr = {} #dict with filenames, keyed by their cellprofiler image number
	for i in range(len(numbersAndNames)):
		namesByNr[i+1] = numbersAndNames[i][1]
	return namesByNr	


def getCellProfilerDataByNr(folder,namesByNr):
	
	#raise Exception("hi")
	# load cell profiler data 
	fname = io.getFilelistFromDir(folder,['DefaultOUT_','_SingleCellsInfected','.csv'])
	if len(fname) != 1:
		print ('no cellprofiler data found for '+ folder)
		return
	celldatname = folder + '/' + fname[0]
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


def exportGlueTables(savefolder,namesByNr,datByNr):
	try:
		os.makedirs(savefolder)
	except:
		print('folder ' + savefolder + ' already exists')	

	for key in datByNr:
		savename = savefolder + '/' + namesByNr[key] + '.csv'
		datByNr[key].to_csv(savename) 



if __name__ == '__main__':


	rootfolder = '/mnt/moehlc/idaf/IDAF_Projects/140507_hanna_gags_dataIntegration/data/cellProfiler'
	savefolder = '/mnt/moehlc/idaf/IDAF_Projects/140507_hanna_gags_dataIntegration/data/glueImageCellprofiler'

	#greate a table for each image file, containing centroid positions of positive cells 
	folders = io.getFilelistFromDir(rootfolder,'V')
	for folder in folders:
	#folder = folders[5]
		namesByNr = getNamesByNr(rootfolder + '/' + folder)
		datByNr = getCellProfilerDataByNr(rootfolder + '/' + folder,namesByNr)
		exportGlueTables(savefolder,namesByNr,datByNr)


