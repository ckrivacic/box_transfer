'''
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
    transfer_to_box.py <folder_or_file> <destination> [options]

Options:
'''


import os
import glob
import docopt
import getpass

args = docopt.docopt(__doc__)

username = input('UCSF email address: ')
password = getpass.getpass(prompt='Box password: ', stream=None)

if os.path.isfile(args['<folder_or_file>']):
    files = [args['<folder_or_file>']]
    basename = os.path.basename(args['<folder_or_file>'])
else:
    basename = os.path.basename(os.path.abspath(args['<folder_or_file>']))
    options = 'cvf'
    suffix = 'tar'
    tar_cmd = "tar -{} - {} | split --bytes=9G --suffix-length=3 --numeric-suffix - {}.{}.".format(
            options, args['<folder_or_file>'], basename, suffix)
    os.system(tar_cmd)
    files = sorted(glob.glob('{}.{}.*'.format(basename, suffix)))

finished = []
for f in files:
    print('Uploading {}'.format(f))
    if f.split('.')[-1] not in finished:
        cmd = "lftp -c \"open {}:{}@ftp.box.com & put -O kortemmelab/{} {}\"".format(
                username, password, args['<destination>'], f)
        os.system(cmd)
