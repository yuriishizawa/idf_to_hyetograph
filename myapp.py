
from idf_to_hyetograph import idf_to_hyetograph
import plotly.express as px
import streamlit as st
import base64

st.sidebar.title('Geração de hietograma')

K = st.sidebar.text_input("K: ",1092.22)
a = st.sidebar.text_input("a: ",0.196)
b = st.sidebar.text_input("b: ",9.32)
c = st.sidebar.text_input("c: ",0.736)
T = st.sidebar.text_input("T (anos): ",30)
td = st.sidebar.text_input("Tempo de duração (minutos): ",120)
dt = st.sidebar.text_input("Passo de tempo (minutos): ",5)


idf = idf_to_hyetograph(K=float(K), a=float(a), b=float(b), c=float(c), T=int(T), td=int(td), dt=int(dt))


df = idf.export_df()
csv = df.to_csv().encode()
b64 = base64.b64encode(csv)
href = f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="extract.xlsx">Download</a>'

st.write("""
## Baixar CSV do hietograma
""")
st.markdown(href, unsafe_allow_html=True)

ax = px.bar(df,x='dt',y='intensity', labels={'dt': 'Tempo', 'intensity': 'Intensidade (mm/h)'}, title='Hietograma')
st.plotly_chart(ax,use_container_width = True)