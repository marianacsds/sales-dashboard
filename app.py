import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("Sales Dashboard")
st.markdown("Análise de dados de vendas — estilo Salesforce")

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

col1, col2, col3 = st.columns(3)
col1.metric("Total de pedidos", len(df))
col2.metric("Receita total", f"$ {df['SALES'].sum():,.0f}")
col3.metric("Ticket médio", f"$ {df['SALES'].mean():,.0f}")

st.subheader("Receita por país")
pais = df.groupby("COUNTRY")["SALES"].sum().reset_index().sort_values("SALES", ascending=False)
fig1 = px.bar(pais, x="COUNTRY", y="SALES", color="SALES", color_continuous_scale="teal")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Receita por linha de produto")
produto = df.groupby("PRODUCTLINE")["SALES"].sum().reset_index()
fig2 = px.pie(produto, names="PRODUCTLINE", values="SALES")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Evolução de vendas ao longo do tempo")
df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])
tempo = df.groupby("ORDERDATE")["SALES"].sum().reset_index()
fig3 = px.line(tempo, x="ORDERDATE", y="SALES")
st.plotly_chart(fig3, use_container_width=True)

st.subheader("Dados brutos")
st.dataframe(df)