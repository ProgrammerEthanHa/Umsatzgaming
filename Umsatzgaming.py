import streamlit as st
import pandas as pd
import altair as alt

st.header("Gaming ist eine Milliarden-Industrie")
st.subheader("Umsatz im Gaming-Markt (inkl. Hardware) in Deutschland von 2012 bis 2022 (in Millionen Euro)")

source = pd.DataFrame({
        'Umsatz in Millionen Euro': [2384, 2409, 2692, 2902, 2904, 4002, 5904, 6228, 8325, 9756, 9873],
        'Jahr': ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Umsatz in Millionen Euro:Q',
        x='Jahr:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Deutschland; April 2023
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle:  Statista")