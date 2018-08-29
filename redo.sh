echo "RV_sa-hn-ru-de-en_3.html"
python rvtest.py 5 RV_sa-hn-ru-de-en_1.html temp_RV_sa-hn-ru-de-en_3.html
echo "RV_sa-hn-ru-de-en_4.html"
python rvtest.py 6 temp_RV_sa-hn-ru-de-en_3.html temp_RV_sa-hn-ru-de-en_4.html
echo "RV_sa-hn-ru-de-en_5.html"
python rvtest.py 7 temp_RV_sa-hn-ru-de-en_4.html temp_RV_sa-hn-ru-de-en_5.html
echo "make rvhymns"
mkdir rvhymns
cp rvhymns.css rvhymns/
mkdir rvhymns/fonts
cp fonts/siddhanta.ttf rvhymns/fonts/
python make_hymns_01.py temp_RV_sa-hn-ru-de-en_5.html rvhymns
echo "removing big intermediate files"
sh clean.sh
