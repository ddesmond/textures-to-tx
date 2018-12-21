# written by aleks katunar

import os, subprocess

### simple converter script from any supported format to TX
### Convert to TX a list of filenames from a provided path

# you can RERUN the script and it will update odl TX with new files data

### Change location to your maketx executable and change root path you want to convert. It will go trough all subfolders and do all conversion for you.
### Please, take note that you can change number of threads

#root folder for TXing texturess
directory = r'G:\PATHTOTEXTURES'

# maketx location
maketx_location = r"R:\\Program Files\\Isotropix\\Clarisse iFX 3.5 SP4\\Clarisse\\"

#change number of threads for maketx to use
threads_to_use = '8'


def get_roots(filepath):
	file_name_w_ext = os.path.basename(filepath)
	file_name, file_extension = os.path.splitext(file_name_w_ext)
	dir_name = os.path.dirname(filepath)
	return file_name, dir_name, file_name_w_ext



def convert_to_tx(folder_for_tx,full_path_tofile):
	full_path_tofile = full_path_tofile.replace("\\","/")
	maketx_arguments = "--checknan"
	maketx_input_file = get_roots(full_path_tofile)
	maketx_input_file = maketx_input_file[0]
	location = get_roots(full_path_tofile)
	maketx_save_file = location[1]+"/"+maketx_input_file+".tx"
	print "save ",maketx_save_file
	all_args = maketx_location+"maketx.exe -v -u --oiio --threads "+threads_to_use+" "+'"'+full_path_tofile+'"'+' -o '+'"'+maketx_save_file+'"'
	print "Converting with args: ",all_args
	converting = subprocess.Popen(all_args, stdout=subprocess.PIPE)
	out, err = converting.communicate()
	print(out)
	return maketx_save_file


#list all files
def listfiles(input):
	for root,dirs,files in os.walk(input, topdown=True):
		for name in files:
			#print(os.path.join(root, name))
			if name.endswith((".png", ".exr",".jpg",".tif",".hdr",".jpeg",".tga",".tiff")):
				print "Converting to TX: "   
				print "original filename: "+name
				path_name = os.path.join(root, name)
				root_for_tx = get_roots(path_name)
				#print root_for_tx
				dirname_tx = root_for_tx[1]
				file_for_tx = root_for_tx[2]
				new_name_tx = convert_to_tx(dirname_tx,path_name)
	print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"      
	print "Work done. Changed so many files, ALWAYS CHECK YOUR FILES!"


listfiles(directory)
