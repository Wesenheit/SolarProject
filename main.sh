data=$(date +%y%m)
day=$(date +%d)
konk=$(date +%Y%m%d)
echo $data
wget ftp://ftpbass2000.obspm.fr/pub/meudon/spc/K/$data/spectro_obspm_Cak_$konk*.fits.gz
gunzip *.gz
ls *.fits > list.txt
if [ -s list.txt ];
then
	echo $konk "initial data found, processing" >> log.dat
	bash caK.sh
else
	echo $konk "no file found" >> log.dat
fi



rm list.txt
rm -f *.fits

