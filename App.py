import streamlit as st
import urllib.parse
from datetime import datetime

st.set_page_config(page_title="Agenda Vet", page_icon="🐾")
st.title("🐾 Clínica Veterinária - Agendamento")

with st.form("form_vet", clear_on_submit=True):
    dono = st.text_input("Nome do Tutor*")
    pet = st.text_input("Nome do Pet*")
    telefone = st.text_input("WhatsApp do Tutor* (apenas números, ex: 5511999999999)")
    data = st.date_input("Data da Consulta")
    horario = st.time_input("Horário")
    
    submetido = st.form_submit_button("Confirmar Agendamento")
    
    if submetido:
        if not dono or not pet or not telefone:
            st.error("Preencha todos os campos obrigatórios (*).")
        else:
            # Gerar Link WhatsApp
            msg = f"Olá {dono}! A consulta do(a) {pet} está confirmada para {data.strftime('%d/%m/%Y')} às {horario.strftime('%H:%M')}."
            msg_codificada = urllib.parse.quote(msg)
            link_wpp = f"https://wa.me/{telefone}?text={msg_codificada}"
            
            # Gerar Link Google Calendário
            data_hora = datetime.combine(data, horario)
            formato_gcal = data_hora.strftime("%Y%m%dT%H%M%S")
            link_gcal = f"https://calendar.google.com/calendar/render?action=TEMPLATE&text=Consulta+Vet+-+{pet}&dates={formato_gcal}/{formato_gcal}&details=Tutor:+{dono}%0ATelefone:+{telefone}"
            
            st.success("Consulta registada com sucesso!")
            st.markdown(f"📱 **[Clique aqui para enviar a confirmação no WhatsApp]({link_wpp})**")
            st.markdown(f"📅 **[Clique aqui para salvar no Google Calendário]({link_gcal})**")