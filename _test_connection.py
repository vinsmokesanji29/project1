import oracledb, os
from dotenv import load_dotenv
load_dotenv()

dsn = "(description=(retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=jxcpe1ln.adb.us-ashburn-1.oraclecloud.com))(connect_data=(service_name=g9d7e65d57136ab_saleslake_low.adb.oraclecloud.com))(security=(ssl_server_dn_match=no)))"

conn = oracledb.connect(user="ADMIN", password="DODO##202507do", dsn=dsn)
cur = conn.cursor()
cur.execute("SELECT SYS_CONTEXT('USERENV','SERVICE_NAME') FROM dual")
print("Service:", cur.fetchone()[0])
cur.execute("SELECT COUNT(*) FROM PROD_DATASETS.WSI")
print("WSI rows:", cur.fetchone()[0])
cur.execute("SELECT COUNT(*) FROM PROD_DATASETS.NBP")
print("NBP rows:", cur.fetchone()[0])
conn.close()
print("Connection OK - Lakehouse LOW service confirmed")
