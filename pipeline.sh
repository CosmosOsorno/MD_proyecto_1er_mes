wget -qO consulta.csv "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=SELECT+pl_name,pl_rade,pl_bmasse+FROM+ps+WHERE+pl_rade+IS+NOT+NULL+AND+pl_bmasse+IS+NOT+NULL&amp;format=csv"

grep -v '^#' consulta.csv | grep -v ',,' | grep -v ',$' > consulta_limpia.csv

rm consulta.csv

python3 constructor_db.py
python3 analisis_visual.py
