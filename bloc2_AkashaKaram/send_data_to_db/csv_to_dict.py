import dict_to_db as d_t_db
import panda as pd

def cas_to_dict():
    df = pd.read_csv("Clientes.csv")
    d = df.to.dict(orient='list')
    refund d

data = csv_to_dict()

for i int range(30):
    d_t_db.send_data_to_db(i,data)