Transfer files and folders to Box. 

Files will be transferred as-is, while folders will be put in a tar
archive. This is necessary to prevent large amounts of files from
transferring extremely slowly. Folders that are larger than 9G will be
split into multiple archives and transferred one by one.

Destination is relative to the 'kortemmelab' folder in Box. 
This means if you want something to go in your home directory, 
for instance, the destination should be 'home/<username>', 
rather than 'kortemmelab/home/<username>'.

If you have a large transfer, it is recommended that you run 'screen'
before starting the upload.

Usage:
    transfer_to_box.py <folder_or_file> <destination>
