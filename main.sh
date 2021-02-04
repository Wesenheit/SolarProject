data=$(date +%y%m)
day=$(date +%d)
konk=$(date +%Y%m%d)
echo $data
wget ftp://ftpbass2000.obspm.fr/pub/meudon/spc/K/$data/spectro_obspm_Cak_$konk*.fits.gz
gunzip *.gz
ls *.fits > list.txt
if [ -s list.txt ];
then
	python3 entry.py list.txt $konk
	echo $konk "data found, processing" >> log.dat
else
	echo $konk "no file found" >> log.dat
fi



rm list.txt
#mv *.txt /binning/
rm -f *.fits

