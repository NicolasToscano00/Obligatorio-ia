import streamlit as st
import requests

# Configuración de la página
st.set_page_config(page_title="Retail 360 Chatbot", page_icon="🤖")

st.title("🤖 Retail 360 - Asistente de Decisiones")
st.markdown("Pregunta sobre ventas, productos, locales y clientes.")

# URL del Backend (Asumiendo que corre en el puerto 8000 por defecto de FastAPI)
BACKEND_URL = "http://127.0.0.1:8000/chat"

# Inicializar historial de chat en la sesión si no existe
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes previos del historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        # Si hay fuentes guardadas en el historial, las mostramos
        if "sources" in message and message["sources"]:
            with st.expander("Ver fuentes consultadas"):
                for source in message["sources"]:
                    st.caption(f"- {source}...")

# Capturar entrada del usuario
if prompt := st.chat_input("Escribe tu consulta aquí..."):
    # 1. Mostrar mensaje del usuario y guardarlo
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Llamar al Backend
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("⏳ *Consultando datos...*")
        
        try:
            # Hacemos la petición POST al endpoint /chat definido en src/app.py
            payload = {"question": prompt}
            response = requests.post(BACKEND_URL, json=payload)
            
            if response.status_code == 200:
                data = response.json()
                answer = data.get("answer", "No se obtuvo respuesta.")
                sources = data.get("sources", [])
                
                # Mostrar respuesta final
                message_placeholder.markdown(answer)
                
                # Mostrar fuentes (Requisito del PDF para validar veracidad)
                if sources:
                    with st.expander("📚 Fuentes de datos utilizadas"):
                        for idx, source in enumerate(sources):
                            st.caption(f"**Fuente {idx+1}:** {source}...")
                
                # Guardar respuesta en el historial
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": answer,
                    "sources": sources
                })
                
            else:
                error_msg = f"Error en el servidor: {response.status_code}"
                message_placeholder.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

        except requests.exceptions.ConnectionError:
            error_msg = "❌ No se pudo conectar con el Backend. Asegúrate de que `src/app.py` esté corriendo."
            message_placeholder.error(error_msg)