# Docking tutorial
## Protein-ligand docking and virtual screening tutorial

Necessary hardware:
* any computer with Internet connection

Necessary software (all free except PyMol):
* [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
* [VMD](http://www.ks.uiuc.edu/Research/vmd/) or [UCSF Chimera](https://www.cgl.ucsf.edu/chimera/) or [PyMol](https://www.pymol.org/)

## Small Linux tutorial

### Linux - usual directory structure

root directiory `/`

* `/bin` = system commands

* `/boot` = startup programs

* `/dev` = devices (disks and otehrs)

* `/etc` = settings

* `/home` = users' home directories

* `/home/vojtech` = home directory of the user vojtech

* `/lib` = libraries

* `/lost+found` = ?

* `/media` or `/mnt` = access to CD/DVD or USB drives

* `/opt` = other programs

* `/proc` = processes

* `/root` = superuser's home directory

* `/sbin` = additional programs

* `/sys` = system

* `/temp` or `/tmp` = temporary data

* `/usr` = main user programs

* `/var` = others

names of files: case-sensitive, avoid space, or @$%^&*()+=/

### Linux help

`man man` - command man with parameter man - the manual for the manual program

`man -h` - command man with modifier -h - the manual's help

### Main Linux commands for file manipulation

* `ls` - prints files/dirs in the current dir

* `ls *.txt` - prints files with name ending .txt in the current dir

* `ls -l` - same as ls but in a long format

* `ls -a` - same as ls but including hidden files

* `ls -t` - same as ls but in the order of file creation

* `ls -rt` - same as ls -t but reverse

* `cd dirname` - go to the subdir called dirname

* `cd ..` - go to the upper directory

* `mkdir dirname` - make directory called dirname

* `pwd` - print current dir

* `ls ~` - prints files/dirs in the home dir

* `cp file1.txt file2.txt` - copy file1.txt to file2.txt

* `mv file1.txt file2.txt` - move file1.txt to file2.txt

* `cp ../file1.txt .` - copy file1.txt from upper directory here

* `rm file1.txt` - delete file1.txt

* `mc` - Midnight Commander 

### Main Linux commands for text manipulation

* `cat file1.txt` - prints the text content

* `head file1.txt` - prints the first 10 lines of the text content

* `head -100 file1.txt` - prints the first 1000 lines of the text content

* `tail file1.txt` - prints the last 10 line of the text content

* `more file1.txt` - prints the text content page by page (can be contorled by Enter, Space or q, similar to less)

* `grep 00033 file1.txt` - prints lines containing 00033

* `grep -v 00033 file1.txt` - prints lines not containing 00033

* `grep -i BB file1.txt` - prints lines containing BB, bb, Bb or bB

* `grep "00 33" file1.txt` - prints lines containing "00 33"

* `wc file1.txt` - counts words and lines

* `diff file1.txt file2.txt` - prints differences in files

### Redirections and pipes

* `cat file1.txt file2.txt > file12.txt` - joints two files into file12.txt

* `grep 000 file1.txt > file2.txt` - prints lines from file1.txt containing 000 to file2.txt

* `cat > file3.txt`
`Write something`
`here`
`Ctrl+D` - creation of a file by cat

* `echo "Write something here" > file1.txt` - creation of a file by echo

* `cat file1.txt >> file2.txt` - appends file1.txt at the end of file2.txt

* `egrep 000 file1.txt | wc` = counts lines containing 000 in file1.txt


