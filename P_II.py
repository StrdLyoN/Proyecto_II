import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

instacart_orders = pd.read_csv('./instacart_orders.csv',sep=';')
products = pd.read_csv('./products.csv',sep=';')
aisles = pd.read_csv('./aisles.csv',sep=';')
departments = pd.read_csv('./departments.csv',sep=';')
order_products = pd.read_csv('./order_products.csv', sep=';')

print()
print("Descripción de los datos")
print()
print(instacart_orders.info())
print()
print(products.info())
print()
print(aisles.info())
print()
print(departments.info())
print()
print(order_products.info())
print()
print('Preprocesamiento de los datos')
print()
print(instacart_orders.duplicated().sum())
print()
wednesday_orders = instacart_orders[(instacart_orders['order_dow'] == 3) & (instacart_orders['order_hour_of_day'] == 2)] 
print(wednesday_orders)
instacart_orders = instacart_orders.drop_duplicates(subset='order_id')
print('Verificar si hay filas duplicadas')

print('Verificar únicamente si hay IDs duplicados de pedidos')
print(instacart_orders['order_id'].duplicated().sum())
print()
print('Verifica si hay filas totalmente duplicadas')
print(products.duplicated().sum())
print()
print('Revisa únicamente si hay ID de departamentos duplicados')
print(products['product_id'].duplicated().sum())
print()
print('Revisa únicamente si hay nombres duplicados de productos (convierte los nombres a letras mayúsculas para compararlos mejor)')
products['product_name'] = products['product_name'].str.upper()
print(products['product_name'].duplicated().sum())
print()
print(products[(~products['product_name'].isna()) & products['product_name'].duplicated()])
print()
print('Revisa si hay filas totalmente duplicadas')
print(departments.duplicated().sum())
print()
print('Revisa únicamente si hay IDs duplicadas de productos')
print(departments['department_id'].duplicated().sum())
print()
print('Revisa si hay filas totalmente duplicadas')
print(aisles['aisle_id'].duplicated().sum())
print()
print('Revisa si hay filas totalmente duplicadas')
print(order_products.duplicated().sum())
print()
print('Vuelve a verificar si hay cualquier otro duplicado engañoso')
print(order_products.duplicated().sum())
print()
print('Encuentra los valores ausentes en la columna product_name')
print()
products['product_name'].isnull().sum()
print(products.isna().sum())
print()
print('¿Todos los nombres de productos ausentes están relacionados con el pasillo con ID 100?')
print(products.head())
print()
print('¿Todos los nombres de productos ausentes están relacionados con el departamento con ID 21?')
print()
products_NA = products[(products['department_id'] == 21)] 
print(products_NA)
print()
print(products.isna().sum())
print()
print('Usa las tablas department y aisle para revisar los datos del pasillo con ID 100 y el departamento con ID 21.')
products_NA_2 = products[(products['department_id'] == 21) & (products['aisle_id'] == 100)]
print()
print(products_NA_2)
print()
print('Completa los nombres de productos ausentes con Unknown')
products['product_name'] = products['product_name'].fillna('Unknow')
print()
print('Encuentra los valores ausentes')
print(order_products.isna().sum())
print()
print('¿Cuáles son los valores mínimos y máximos en esta columna?')
min_add_to_cart_order = order_products['add_to_cart_order'].min()
max_add_to_cart_order = order_products['add_to_cart_order'].max()
print()
print(min_add_to_cart_order) 
print(max_add_to_cart_order)
print('Guarda todas las IDs de pedidos que tengan un valor ausente en add_to_cart_order')
missing_values_ids = order_products[order_products['add_to_cart_order'].isnull()]['order_id'].unique()
print()
print('¿Todos los pedidos con valores ausentes tienen más de 64 productos?')
max_add_to_cart_order = order_products['add_to_cart_order'].max()
print(max_add_to_cart_order)
print()
print('Agrupa todos los pedidos con datos ausentes por su ID de pedido.')
missing_data = order_products.groupby('order_id')['product_id'].count().min()
print()
print('Cuenta el número de product_id en cada pedido y revisa el valor mínimo del conteo.')
print(missing_data)
print()
print('Remplaza los valores ausentes en la columna add_to_cart? con 999 y convierte la columna al tipo entero.')
order_products['add_to_cart_order'] = order_products['add_to_cart_order'].fillna(999).astype(int)
print(order_products[order_products['add_to_cart_order'] == 999])
print()
print('Verifica que los valores sean sensibles')
print()
valid_order_hour_of_day = instacart_orders[(instacart_orders['order_hour_of_day'] >= 0) & (instacart_orders['order_hour_of_day'] <= 23)].shape[0]
valid_order_dow = instacart_orders[(instacart_orders['order_dow'] >= 0) & (instacart_orders['order_dow'] <= 6)].shape[0]
print()
print('Para cada hora del día, ¿cuántas personas hacen órdenes?')
print(instacart_orders.head())
order_count_by_hour = instacart_orders['order_hour_of_day'].value_counts().sort_index()
order_count_by_hour.plot(kind= 'bar', x='order_hour_of_day', y= 'order_number')
print(plt.show())
print()
print('¿Qué día de la semana compran víveres las personas?')
order_count_by_hour = instacart_orders['order_dow'].value_counts().sort_index()
order_count_by_hour.plot(kind= 'bar', x='order_dow', y= 'order_number')
print(plt.show())
print()
print('¿Cuánto tiempo esperan las personas hasta hacer otro pedido? Comenta sobre los valores mínimos y máximos.')
order_count_by_hour = instacart_orders['days_since_prior_order'].value_counts().sort_index()
order_count_by_hour.plot(kind= 'bar', x='days_since_prior_order', y= 'order_number')
print(plt.show())
print()
print('Diferencia entre miércoles y sábados para order_hour_of_day. Traza gráficos de barra para los dos días y describe las diferencias que veas.')
wednesday_orders = instacart_orders[instacart_orders['order_dow'] == 3]
saturday_orders = instacart_orders[instacart_orders['order_dow'] == 6]
wednesday_hours = wednesday_orders['order_hour_of_day'].value_counts().sort_index()
saturday_hours = saturday_orders['order_hour_of_day'].value_counts().sort_index()

plt.bar(wednesday_hours.index, wednesday_hours.values, color='blue', label='Wednesday')
plt.bar(saturday_hours.index, saturday_hours.values, color='red', label='Saturday')

print(plt.legend())
print(plt.show())

orders_per_customer = instacart_orders['order_number']
orders_distribution = orders_per_customer.value_counts().sort_index()
print()
print(plt.bar(orders_distribution.index, orders_distribution.values))
print(plt.show())
print()
merged_data = pd.merge(order_products, products, on='product_id', how='inner')
top_products = merged_data['product_id'].value_counts().reset_index()
top_products.columns = ['product_id', 'order_frequency']

top_products = pd.merge(top_products, products, on='product_id', how='inner')

top_20_products = top_products[['product_id', 'product_name']].head(20)

print(top_20_products)
print()
print('¿Cuál es la distribución para el número de pedidos por cliente?')
merged_data = pd.merge(instacart_orders, order_products, on='order_id')
orders_per_customer = merged_data.groupby('user_id')['order_id'].nunique()
plt.hist(orders_per_customer, bins=20)
plt.xlabel('Número de pedidos')
plt.ylabel('Frecuencia')
plt.grid(axis='y', alpha=0.75)
print(plt.show())
print()
print('¿Cuáles son los 20 productos más populares (muestra su ID y nombre)?')
product_count = order_products['product_id'].value_counts()
popular_products = pd.merge(products, product_count, left_on='product_id', right_index=True)
top_20_products = popular_products.sort_values(by='product_id', ascending=False)
print(top_20_products[['product_id', 'product_name']])
print()
print('Cuántos artículos compran normalmente las personas en un pedido? ¿Cómo es la distribución?')
products_per_order = order_products.groupby('order_id')['product_id'].count().reset_index()
products_per_order = products_per_order.rename(columns={'product_id': 'num_products'})
plt.hist(products_per_order['num_products'], bins=50)
plt.xlabel('Número de productos por pedido')
plt.ylabel('Frecuencia')
plt.grid(axis='y', alpha=0.75)
print(plt.show())
print(products_per_order)
print()
print('¿Cuáles son los 20 principales artículos que vuelven a pedirse con mayor frecuencia (muestra sus nombres e IDs de los productos)?')
reordered_products = pd.merge(order_products, products, on='product_id', how='left')
reordered_products = reordered_products[reordered_products['reordered'] == 1]
reordered_count = reordered_products.groupby(['product_id', 'product_name']).size().reset_index(name='reorder_frequency')
top_reordered_products = reordered_count.sort_values(by='reorder_frequency', ascending=False).head(20)
print(top_reordered_products[['product_id', 'product_name']])
print()
print('Para cada producto, ¿cuál es la proporción de las veces que se pide y que se vuelve a pedir?')
merged_df = pd.merge(order_products, products, on='product_id', how='inner')
product_order_count = merged_df['product_id'].value_counts()
reordered_products = merged_df[merged_df['reordered'] == 1]['product_id'].value_counts()
product_reorder_ratio = pd.concat([product_order_count, reordered_products], axis=1, join='inner')
product_reorder_ratio.columns = ['total_orders', 'reordered_orders']

product_reorder_ratio['reorder_ratio'] = product_reorder_ratio['reordered_orders'] / product_reorder_ratio['total_orders']


product_reorder_ratio = product_reorder_ratio.sort_values(by='reorder_ratio', ascending=False)
print(product_reorder_ratio)
print()
print('Para cada cliente, ¿qué proporción de sus productos ya los había pedido?')
merged_data = pd.merge(instacart_orders, order_products, on='order_id')
merged_data = pd.merge(merged_data, products, on='product_id')

total_products = merged_data.groupby(['user_id'])['product_id'].nunique().reset_index()
total_products.columns = ['user_id', 'total_products']

unique_products = merged_data.groupby(['user_id', 'product_id'])['order_id'].nunique().reset_index()
unique_products = unique_products.groupby('user_id')['product_id'].count().reset_index()
unique_products.columns = ['user_id', 'unique_products']
reorder_proportion = pd.merge(total_products, unique_products, on='user_id')
reorder_proportion['reorder_proportion'] = reorder_proportion['unique_products'] / reorder_proportion['total_products']

print(reorder_proportion)
print('¿Cuáles son los 20 principales artículos que las personas ponen primero en sus carritos?')
order_products_merged = pd.merge(order_products, products, on='product_id')
first_in_cart = order_products_merged[order_products_merged.add_to_cart_order == 1]
top_products_first_in_cart = first_in_cart.groupby(['product_id', 'product_name']).size().reset_index(name='count')
top_20_first_in_cart = top_products_first_in_cart.nlargest(20, 'count')
print(top_20_first_in_cart[['product_id', 'product_name', 'count']])
