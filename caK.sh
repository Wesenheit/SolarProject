data=$(date +%y%m)
day=$(date +%d)
konk=$(date +%Y%m%d)
echo $data

python3 entry.py
pliki=(spec*txt)

if [ -s ${pliki[0]} ];
then
	wget ftp://ftpbass2000.obspm.fr/pub/meudon/spc/K/$data/spectro_obspm_fullprofile_Cak_3D_$konk*.fits.gz
	gunzip *.gz
	python3 specK.py
	echo "active region found" >> log.dat
	mkdir plots/$konk
	mv *png plots/$konk
	mkdir binning/$konk
	mv spec*txt binning/$konk
else
	echo "no active region found" >> log.dat
fi

