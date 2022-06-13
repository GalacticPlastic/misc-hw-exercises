# moving around
pwd = current working directory
cd = change directory 

. current directory
.. parent directory
- previous working directory

tree #will allow you to see directory structure may require installation 

Absolute paths /etc #Actual path
Relative paths if pwd is / then etc is relative to / #path relative to where you are
	../../somefolder  exemple

ls = list directory 
	ls 	-a or --all = shows all directories including hidden stuff
		-d ––directory Show a directory’s own metadata instead of its contents.
		-F ––classify Classify each file’s type using an indicator code (*,/,=,>,@, or |).
		-i ––inode Display all file and subdirectory names along with their associated
		index number.
		-l  Display file and subdirectory metadata, which includes file type, file
			access permissions, hard link count, file owner, file’s group, modification date and time, and file name.
		-R  Show a directory’s contents, and for any subdirectory within the original
			directory tree, consecutively show their contents as well (recursively).
touch filename # will create an empty file 
mkdir # create a bnew directory 
	with a -p can make nested directories -v you can see it verbose
	
file command will give you info about a file 

cp copy 
	cp filetocopy newcopy
		-a ––archive Perform a recursive copy and keep all the files’ original
			attributes, such as permissions, ownership, and timestamps.
		-f ––force Overwrite any preexisting destination files with same name as DEST.
		-i ––interactive Ask before overwriting any preexisting destination files with
			same name as DEST.
		-n ––no-clobber Do not overwrite any preexisting destination files with same
			name as DEST.
		-R, -r ––recursive Copy a directory’s contents, and for any subdirectory within the
			original directory tree, consecutively copy its contents as well
			(recursive).
		-u ––update Only overwrite preexisting destination files with the same name
			as DEST, if the source file is newer.
		-v ––verbose Provide detailed command action information as command
			executes.
mv can be used to move or rename a file 
	mv filename newfilename
			-f ––force Overwrite any preexisting destination files with same name
				as DEST.
			-i ––interactive Ask before overwriting any preexisting destination files with the
				same name as DEST.
			-n ––no-clobber Do not overwrite any preexisting destination files with the same
				name as DEST.
			-u ––update Only overwrite preexisting destination files with the same name
				as DEST if the source file is newer.
			-v ––verbose Provide detailed command action information as command
				executes.
				
rsync # like scp it can be tunneled over ssh like if you are backing up to a share
	a ––archive Use archive mode. # same as rlptgoD used for back ups 
	-D N/A Retain device and special files.
	-g ––group Retain file’s group.
	-h ––human-readable Display any numeric output in a human-readable format.
	-l ––links Copy symbolic links as symbolic links.
	-o ––owner Retain file’s owner.
	-p ––perms Retain file’s permissions.
	N/A ––progress Display progression of file copy process.
	-r ––recursive Copy a directory’s contents, and for any subdirectory within
		the original directory tree, consecutively copy its contents
		as well (recursive).
		N/A ––stats Display detailed file transfer statistics.
	-t ––times Retain file’s modification time.
	-v ––verbose Provide detailed command action information as command
		executes
		
		# When backing up it only copies what is needed 
		The remote sync utility will often display a speedup rating in its output.
This rating is related to conducting synchronized backups. If you are using
the rsync command to conduct periodic backups of a particular directory
to another directory location, the speedup rating lets you know how many
files did not need to be copied because they had not been modified and
were already backed up. For example, if 600 of 600 files had to be copied to
the backup directory location, the speedup is 1.00. If only 300 of 600 files
had to be copied, the speedup is 2.00. Thus, whenever you are using the
rsync command to copy a single file to a new location, the speedup will
always be 1.00.


rm [option]file # removes file with a -r directories and files never do an rm -rf /* 

		-d ––dir Delete any empty directories.
		-f ––force Continue on with the deletion process, even if some files
			designated by the command for removal do not exist, and do
			not ask prior to deleting any existing files.
		-i ––interactive Ask before deleting any existing files.
		-I N/A Ask before deleting more than three files, or when using the -r
			option.
		-R, -r ––recursive Delete a directory’s contents, and for any subdirectory within
			the original directory tree, consecutively delete its contents and
			the subdirectory as well (recursive).
		-v ––verbose Provide detailed command action information as command
			executes.
			
			# note that rmdir only removes empty directories
# LINKING (Shortcuts or alias) 
inode = index number = metadata about a file >> like:

		Device ID
		User ID of the file
		Group ID of the file
		The file mode that determines the file type and how the owner, group, and others (world) can access the file
		Additional system and user flags to further protect the file (note: this can be used limit the files use and modification)
		Timestamps telling when the inode itself was last change (ctime, changing time), the file content was last modified (mtime or modification time), and when the file was last accessed (atime or access time)
		A link counter that lists how many hard links point to the inode
		Pointers to the disk blocks that store the files contents

Hard link = copy of a file linked to the same inode 
soft link = a shortcut to the real thing it has a different inode 
	if the real file is deleted the link breaks 

ln file linked file #hard link
ln -s file softlinkfile #soft link

######### Reading files
cat file # outputs contents

	-A --show-all Equivalent to using the option -vET combination.
	-E --show-ends Display a $ when a newline linefeed is encountered.
	-n --number Number all text file lines and display that number in
	the output.
	-s --squeeze-blank Do not display repeated blank empty text file lines.
	-T --show-tabs Display a ^I when a Tab character is encountered.
	-v --show-nonprinting Display nonprinting characters when encountered
	using either ^ and/or M- notation.

pr allows you to diplsy two files side by side when combined with -mtl options



head top of a file 
tail bottom of a file (you can also specify number of lines) -n #
tail -f streams a file useful to log analisys on the fly
more or less (less has more functionality and is newer) #pager for large files allows you to page up or down...

diff #checks the differences of 2 files 
	-e ––ed Create an ed script, which can be used to make
		the first file compared the same as the second file
		compared.
	-q ––brief If files are different, issue a simple message
		expressing this.
	-r ––recursive Compare any subdirectories within the original
		directory tree, and consecutively compare
		their contents and the subdirectories as well
		(recursive).
	-s ––report-identical-files If files are the same, issue a simple message
		expressing this.
	-W n ––width n Display a width maximum of n characters for
		output.
	-y ––side-by-side Display output in two columns.
	
#gathering intel

which +command #  find whre the binary is located can also show alias 
#to undo an alias type unalias + command to find true path

whereis +command # you will find the binary and source code

locate #command need updatedb as it runs searches out of an index 
 
	-A ––all Display file names that match all the patterns, instead of displaying files that match only one pattern in the pattern list.
	-b ––basename Display only file names that match the pattern and do not
		include any directory names that match the pattern.
	-c ––count Display only the number of files whose name matches the pattern instead of displaying file names.
	-i ––ignore-case Ignore case in the pattern for matching file names.
	-q ––quiet Do not display any error messages, such as permission
		denied, when processing.
	-r ––regexp R Use the regular expression, R, instead of the pattern list to
		match file names.
	-w ––wholename Display file names that match the pattern and include any
		directory names that match the pattern. This is default
		behavior.
find #allows you to find stuff based on metadata info like files that are older than 30 days for eemple

		-cmin n Display names of files whose status changed n minutes ago.
		-empty N/A Display names of files that are empty and are a regular text
			file or a directory.
		-gid n Display names of files whose group id is equal to n.
		-group name Display names of files whose group is name.
		-inum n Display names of files whose inode number is equal to n.
		-maxdepth n When searching for files, traverse down into the starting
			point directory’s tree only n levels.
		-mmin n Display names of files whose data changed n minutes ago.
		-name pattern Display names of files whose name matches pattern. Many
			regular expression arguments may be used in the pattern
			and need to be enclosed in quotation marks to avoid unpredictable results. Replace -name with -iname to ignore case.
		-nogroup N/A Display names of files where no group name exists for the
			file’s group ID.
		-nouser N/A Display names of files where no username exists for the file’s
			user ID.
		-perm mode Display names of files whose permissions matches mode.
			Either octal or symbolic modes may be used.
		-size n Display names of files whose size matches n. Suffixes can be
			used to make the size more human readable, such as G for
			gigabytes.
		-user name Display names of files whose owner is name
	
		 find . -name "*.txt"
			./Project47.txt
			./Answers/Project42.txt
			./Answers/Everything/numbers.txt
			./Answers/Everything/random.txt
			./Answers/Project43.txt
			./Answers/Project44.txt
			./Answers/Project45.txt
			./Answers/Project46.txt
			./SpaceOpera/OriginalSFile.txt
			./SpaceOpera/SoftLinkFile.txt
			$
		find . -maxdepth 2 -name "*.txt"
			./Project47.txt
			./Answers/Project42.txt
			./Answers/Project43.txt
			./Answers/Project44.txt
			./Answers/Project45.txt
			./Answers/Project46.txt
			./SpaceOpera/OriginalSFile.txt
			./SpaceOpera/SoftLinkFile.txt




	
			

