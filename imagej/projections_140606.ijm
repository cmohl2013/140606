loadfolder = "/Volumes/idaf/IDAF_Projects/140507_hanna_gags_dataIntegration/data/images/lsm/"
savefolder = "/Volumes/idaf/IDAF_Projects/140507_hanna_gags_dataIntegration/data/images/tiff/"
File.makeDirectory(savefolder);
ls = getFileList(loadfolder);

setBatchMode(true);
for (i=0;i<ls.length;i++){
	print(ls[i]);

	run("Bio-Formats Importer", "open="+ loadfolder + ls[i]+" color_mode=Default open_files view=Hyperstack stack_order=XYCZT");
	//open(ls[i]);
	savename = File.nameWithoutExtension;
	raw = getImageID();
	getDimensions(width, height, channels, slices, frames);
	run("Z Project...", "start=1 stop="+ slices + " projection=[Average Intensity]");
	run("Split Channels");
	selectImage(raw);
	close();
	close();
	saveAs("Tiff",savefolder + savename + "_C1.tif");
	run("Log");
	saveAs("Tiff",savefolder + savename + "_C3.tif");
	close();
	saveAs("Tiff",savefolder + savename + "_C2.tif");
	
	close();
}
setBatchMode(false);