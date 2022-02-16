# -*- coding: utf-8 -*-

import pandas as pd
from functions import get_products

base_url = 'https://www.mapa.gob.es/app/consultafertilizante/ListadoFertilizantes.aspx?Page='
products = []
n_pages = 70

for i in range(0,n_pages + 1):
    partial_products = get_products(base_url+str(i))
    for p in partial_products:
        products.append(p)

products_df = pd.DataFrame(products)
products_df.columns= ['Código', 'Tipo', 'Nombre comercial', 'Fabricante', 'F. de registro', 'Url']
products_df.to_csv('./fertilizers.csv', index=False)
