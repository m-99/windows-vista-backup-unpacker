# windows-vista-backup-unpacker
Get your files out of a Windows Vista backup!

## Description
What this does is take the output from a Windows Vista backup that was made with the Backup and Restore Center, which looks kind of like this:

(image coming soon)

and unzips all of the folders, then moves all of the contents of the folders into their original file structure. The location of these consolidated files will be the root directory where the zipped folders were located.

Something that can do this probably already exists (it might even be built in to Windows!), but I couldn't find something helpful after a  few internet searches, so I made this real quick.

## To use:
1. Download `VistaUnpacker.py`
2. Move `VistaUnpacker.py` into the same folder where the zipped backup files are located
3. Run `py VistaUnpacker.py`

### Notes
This might take a long time! I didn't really optimize for performance, and doing this could potentially take up a TON of disk space, since you're unzipping every folder from your backup.

This script does not delete any files, but I do not take any responsibility for what happens when you run this. It might be a good idea to make a copy of the backup, then run this script on the copy.
