# -*- coding: utf-8 -*-

import pandas as pd
from functions import get_products, get_composition

base_url = 'https://www.mapa.gob.es/app/consultafertilizante/ListadoFertilizantes.aspx?Page='
products = []
n_pages = 70
components = ['Nitrógeno(N) Total', 'Anhidrido fosfórico (P2O5)', 'Óxido de potasio (K2O)', 'Boro (B)', 'Cobalto (Co)', 'Cobre (Cu)', 'Hierro (Fe)','Manganeso (Mn)', 'Molibdeno (Mb)','Cinc (Zn)']
equivalencies = {
    'Nitrógeno(N) Total': 'Nitrógeno (N)', 
    'Anhidrido fosfórico (P2O5)' : 'Fósforo (P)', 
    'Óxido de potasio (K2O)': 'Potasio (K)'
    }

for i in range(0,n_pages + 1):
    partial_products = get_products(base_url+str(i))
    for p in partial_products:
        products.append(p)

products_df = pd.DataFrame(products)
products_df['Composicion'] = products_df.apply(lambda row: get_composition(components, equivalencies, row[5]), axis=1)

products_df.columns= ['Código', 'Tipo', 'Nombre comercial', 'Fabricante', 'F. de registro', 'Url', 'Composition']
products_df.to_csv('./fertilizers_composition.csv', index=False)
