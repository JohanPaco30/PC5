#LEYENDO DATOS
import pandas as pd
df_vinos = pd.read_csv("winemag-data-130k-v2.csv")

df_vinos.head()

#RENOMBRANDO EL TITULO DE LOS ENCABEZADOS
df_rename = df_vinos.rename(columns= {'country':'país', 'points':'puntos', 'price':'precio','province':'provincia', 'winery':'bodega', 'variety':'tipo_vino', 'taster_name':'nombre_catador'})
df_drop = df_rename.drop(['Unnamed: 0'], axis = 1)
df_drop.head(10)

#AGREGANDO COLUMNAS
def nota_precio(precio:float):

    if precio > 0 and precio <=500:
        return 'Barato'
    elif precio > 500 and precio <=1000:
        return 'Normal'
    elif precio > 1000 and precio <=1500:
        return 'Caro'
    elif precio > 1500 and precio <=2500:
        return 'Muy Caro'
    else:
        return 'Sin apreciación'

df_drop['Apreciación_Precio'] = df_drop.precio.apply(nota_precio)
df_drop.head(5)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def nota_precio(puntos:int):

    if puntos >= 80 and puntos <=90:
        return 'Muy Bueno'
    elif puntos > 90 and puntos <=95:
        return 'Atractivo'
    elif puntos > 95 and puntos <=100:
        return 'Excepcional'
    else:
        return 'Sin apreciación'

df_drop['Apreciación_Calidad'] = df_drop.puntos.apply(nota_precio)
df_drop.head(5)

df_fil = df_drop.sort_values(by = ['precio'], ascending= False)
df_fil.head(5)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# COLUMNA FILTRADA PARA AQUELLOS QUE DESEAN UN SOLO VINO EXCEPCIONAL Y LES IMPORTA EL PRECIO
df_fil['CRITICA'] = 'NO RECOMENDABLE'

df_fil.loc[(df_fil['Apreciación_Precio'] == 'Barato') & (df_fil['Apreciación_Calidad'] == 'Excepcional'), 'CRITICA'] = 'Calidad/Precio'
df_fil.loc[(df_fil['Apreciación_Precio'] == 'Normal') & (df_fil['Apreciación_Calidad'] == 'Excepcional'), 'CRITICA'] = 'Moderado'
df_fil.loc[(df_fil['Apreciación_Precio'] == 'Caro') & (df_fil['Apreciación_Calidad'] == 'Excepcional'), 'CRITICA'] = 'Hay mejores'
df_fil.loc[(df_fil['Apreciación_Precio'] == 'Muy Caro') & (df_fil['Apreciación_Calidad'] == 'Excepcional'), 'CRITICA'] = 'No lo Vale'
df_fil.loc[(df_fil['Apreciación_Precio'] == 'Sin apreciación') & (df_fil['Apreciación_Calidad'] == 'Excepcional'), 'CRITICA'] = 'Sin Apreciación'



df_fil.head(5)


#GENERANDO REPORTES: 

#EL CATADOR DE LOS VINOS, MOSTRANDO DETALLES EXTRAS
df_catador = df_fil[['nombre_catador','title','description','puntos']].sort_values('nombre_catador', ascending= True)
df_catador.head(5)

#EL PRECIO DE LOS VINOS CATADOS, MOSTRANDO SU VALOR Y SU APRECIACIÓN
df_tipo2 = df_fil[['tipo_vino','description','precio','Apreciación_Precio']].sort_values('tipo_vino', ascending= True)
df_tipo2.head(5)

#REPORTE FINAL
df_filtro = df_fil[['tipo_vino','description','puntos','precio','Apreciación_Precio','Apreciación_Calidad','CRITICA']].sort_values('tipo_vino', ascending= True)
df_excepcional = df_filtro['Apreciación_Calidad'] == 'Excepcional'
df_final = df_filtro[df_excepcional]
df_final

#EXPORTANDO EL REPORTE FINAL
df_final.to_excel('CRITICA_VINOS.xlsx', sheet_name= 'VINO_EXCEPCIONAL',index= False ,engine= 'openpyxl')