
# esse código fica ao final do arquivo pois ele é um botão invis´vel que é clicado automaticamente por um script externo para manter a sessão ativa
with st.empty():
    st.markdown('<div id="autoclick-div">', unsafe_allow_html=True)
    if st.button("Ping Button", key="autoclick_button"):
        print("Ping button clicked by automation.")
    st.markdown('</div>', unsafe_allow_html=True)