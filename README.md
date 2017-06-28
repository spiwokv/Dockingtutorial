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

cat soubor1.txt
 = vypíše obsah textového souboru
head soubor1.txt
 = vypíše prvních deset řádků souboru
head -100 soubor1.txt
 = vypíše prvních sto řádků souboru
tail soubor1.txt
 = vypíše posledních deset řádků souboru
more soubor1.txt
 = vypíše obsah souboru po stránkách
(nový řádek Enter, nová stránka mezerník, konec q).
Podobný je příkaz
 less
grep 00033 soubor1.txt
 = vypíše řádky souboru,
které obsahují řetězec 00033
grep -v 00033 soubor1.txt
 = vypíše řádky souboru,
které NEobsahují řetězec 00033
grep -i BB soubor1.txt
 = vypíše řádky souboru, které obsahují
řetězec BB, bb, Bb nebo bB
grep "00 33" soubor1.txt
 = vypíše řádky souboru,
které obsahují řetězec "00 33"
wc soubor1.txt
 = spočítá slova a řádky v souboru 
diff soubor1.txt soubor2.txt
 = zjistí rozdíly v souborech
