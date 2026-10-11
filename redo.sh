echo "RV_sa-hn-ru-de-en_5.html (py3 port of the rvtest 5/6/7 chain)"
python3 prep_source.py RV_sa-hn-ru-de-en_1.html temp_RV_sa-hn-ru-de-en_5.html
echo "make rvhymns"
mkdir -p rvhymns
cp rvhymns.css rvhymns/
mkdir -p rvhymns/fonts
cp fonts/siddhanta.ttf rvhymns/fonts/
python3 make_hymns_01.py temp_RV_sa-hn-ru-de-en_5.html rvhymns make_hymns_log.txt
echo "keep the 2020 hand-fixed Griffith bodies (rv08.049-103; source never updated)"
python3 keep_griffith_fix.py
echo "social preview cards (pilot: first su.kta of each mandala; full 1028 set after the TG canary)"
python3 make_cards.py temp_RV_sa-hn-ru-de-en_5.html rv01.001 rv02.001 rv03.001 rv04.001 rv05.001 rv06.001 rv07.001 rv08.001 rv09.001 rv10.001
echo "re-run make_hymns so pages pick up og:image + twitter:card where cards exist"
python3 make_hymns_01.py temp_RV_sa-hn-ru-de-en_5.html rvhymns make_hymns_log.txt
python3 keep_griffith_fix.py
echo "removing big intermediate files"
sh clean.sh
