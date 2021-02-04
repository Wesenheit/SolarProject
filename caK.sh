data=$(date +%y%m)
day=$(date +%d)
konk=$(date +%Y%m%d)
echo $data
wget ftp://ftpbass2000.obspm.fr/pub/meudon/spc/K/$data/spectro_obspm_fullprofile_Cak_3D_$konk*.fits.gz
gunzip *.gz
ls *3D* > list1.txt
python3 entry.py
if [ -s list1.txt ];
then
	python3 specK.py
	echo "3D cube found" >> log.dat
else
	echo "3D cube not found" >> log.dat
fi

mkdir plots/$konk
mv *png plots/$konk
mv spec*txt plots/$konk

