\\
Text manipulation is a big part of Linux. This goes back to the concept that 
everything in Linux is a file. In turn this will generally present us with the ability
to open anything to look at settings, code and among other things. 
\\

cut command allows you to sip through a large file minus the info that you do not want

$ head -2 /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
$

-------

$ cut -d ":" -f 1,7 /etc/passwd
root:/bin/bash
bin:/sbin/nologin
[...]
$

-----

$ cut -c 1-5 /etc/passwd
root:
bin:x
[...]

Options for CUT
-c nlist --characters nlist Display only the record characters in the nlist (e.g., 1-5).
-b blist --bytes blist Display only the record bytes in the blist (e.g., 1-2).
-d d --delimiter d Designate the record’s field delimiter as d. This overrides
the Tab default delimiter. Put d within quotation marks to
avoid unexpected results.
-f flist --fields flist Display only the record’s fields denoted by flist (e.g., 1,3).
-s --only-delimited Display only records that contain the designated delimiter.
-z --zero-terminated Designate the record end-of-line character as the ASCII
character NUL.

grep command is another tool that can be used for filtering out information and allow use of regular expressions

$ grep root /etc/passwd
root:x:0:0:root:/root:/bin/bash
operator:x:11:0:operator:/root:/sbin/nologin



$
$ grep ^root /etc/passwd
root:x:0:0:root:/root:/bin/bash


REGEX
[ ]: Matches any one of a set characters
[ ] with hyphen: Matches any one of a range characters
^: The pattern following it must occur at the beginning of each line
^ with [ ] : The pattern must not contain any character in the set specified
$: The pattern preceding it must occur at the end of each line
. (dot): Matches any one character
\ (backslash): Ignores the special meaning of the character following it
*: zero or more occurrences of the previous character
(dot).*: Nothing or any numbers of characters.

Within a bracket expression, the name of a character class enclosed in “[:” and “:]” stands for the list of all characters belonging to that class. Standard character class names are:

[[:alnum:]] – Alphanumeric characters.
[[:alpha:]] – Alphabetic characters
[[:blank:]] – Blank characters: space and tab.
[[:digit:]] – Digits: ‘0 1 2 3 4 5 6 7 8 9’.
[[:lower:]] – Lower-case letters: ‘a b c d e f g h i j k l m n o p q r s t u v w x y z’.
[[:space:]] – Space characters: tab, newline, vertical tab, form feed, carriage return, and space.
[[:upper:]] – Upper-case letters: ‘A B C D E F G H I J K L M N O P Q R S T U V W X Y Z’.


options 


-c --count Display a count of text file records that contain a
PATTERN match.
-d action --directories=action When a file is a directory, if action is set to read,
read the directory as if it were a regular text file;
	if action is set to skip, ignore the directory; and
	if action is set to recurse, act as if the - R, -r, or

--recursive option was used.
-E --extended-regexp Designate the PATTERN as an extended regular
expression.
-i --ignore-case Ignore the case in the PATTERN as well as in any
text file records.
-R, -r --recursive Search a directory’s contents, and for any
subdirectory within the original directory
tree, consecutively search its contents as well
(recursively).
-v --invert-match Display only text files records that do not contain
a PATTERN match.


sort # does what its name imlies


	-c --check Check if file is already sorted. Produces no output if file is sorted.
	If file is not sorted, it displays the file name, the line number, the
	keyword disorder, and the first unordered line’s text.
	-f --ignore-case Consider lowercase characters as uppercase characters when
	sorting.
	-k n1 [,n2] --key=n1 [,n2] Sort the file using the data in the n1 field. May optionally
	specify a second sort field by following n1 with a comma and
	specifying n2. Field delimiters are spaces by default.
	-M --month-sort Display text in month of the year order. Months must be listed
	as standard three-letter abbreviations, such as JAN, FEB, MAR,
	and so on.
	-n --numeric-sort Display text in numerical order.
	-o file --output=file Create new sorted file named file.
	-r --reverse Display text in reverse sort order

printf #formating text useful for scripts


wc # word count very useful 

-c --bytes Display the file’s byte count.
-L --max-line-length Display the byte count of the file’s longest line.
-l --lines Display the file’s line count.
-m --chars Display the file’s character count.
-w --words Display the file’s word count.
