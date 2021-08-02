import sqlite3
import pandas as pd

eng_lex = pd.read_excel("lex/eng_lex.xlsx", sheet_name="Feuil1", header=0)
esp_lex = pd.read_excel("lex/esp_lex.xlsx", sheet_name="Feuil1", header=0)
fr_lex = pd.read_excel("lex/fr_lex.xlsx", sheet_name="Feuil1", header=0)
db_conn = sqlite3.connect("db/mydb.db")

eng_lex.to_sql("eng_lex", db_conn, index=False, if_exists="replace")
esp_lex.to_sql("esp_lex", db_conn, index=False, if_exists="replace")
fr_lex.to_sql("fr_lex", db_conn, index=False, if_exists="replace")

db_conn.commit()
db_conn.close()
