import os, glob
path = os.path.dirname(os.path.realpath(__file__))

exts = ['.png', '.jpeg']

for ext in exts:
	glob_ext = '*' + ext
	len_ext = len(ext)
	for oldName in glob.glob(glob_ext):
		# Remove the png extension
		oldName = oldName[:-len_ext]
		# Result: BTC_20200101

		# Split in two strings
		oldName_list = oldName.split('_')

		# Create new name
		newName = oldName_list[1] + '_' + oldName_list[0] + ext
		# Result: 20200101_BTC.png

		# Add the png extension again...
		oldName = oldName + ext

		# Rename
		os.rename(oldName, newName)

print('Done mate!')