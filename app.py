import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
from sklearn import svm
import streamlit as st



# Path del modelo preentrenado
MODEL_PATH = 'pickle_model.pkl'


# Se recibe la imagen y el modelo, devuelve la predicción
def model_prediction(x_in, model):

    x = np.asarray(x_in).reshape(1,-1)
    preds=model.predict(x)

    return preds


def main():
    
    model=''

    # Se carga el modelo
    if model=='':
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)
    
    # Título
    html_temp = """
    <h1 style="color:#181082;text-align:center;">SISTEMA INTELIGENTE DE RECOMENDACIÓN DE CULTIVOS EN TOLIMA</h1>
    </div>
    """
   
    st.markdown(html_temp,unsafe_allow_html=True)

    # Lecctura de datos
    #Datos = st.text_input("Ingrese los valores : N P K Temp Hum pH lluvia:")
    N = st.text_input("Nitrógeno(N)(%)):")
    P = st.text_input("Fósforo(P)(mg/L)):")
    K = st.text_input("Potasio(K en %):")
    Temp = st.text_input("Temperatura(C):")
    Hum = st.text_input("Humedad %:")
    pH = st.text_input("pH(0-14):")
    rain = st.text_input("Lluvia(mm):")
    
    # El botón predicción se usa para iniciar el procesamiento
    if st.button("Predicción del cultivo:"): 
        #x_in = list(np.float_((Datos.title().split('\t'))))
        x_in =[np.float_(N.title()),
                    np.float_(P.title()),
                    np.float_(K.title()),
                    np.float_(Temp.title()),
                    np.float_(Hum.title()),
                    np.float_(pH.title()),
                    np.float_(rain.title())]
        predictS = model_prediction(x_in, model)
        st.success('EL CULTIVO RECOMENDADO ES: {}'.format(predictS[0]).upper())

    st.image("clustering.jpg", caption="clustering")

    # Botón para cerrar la aplicación
    if st.button("Cerrar aplicación"):
    # Mensaje para notificar al usuario que la ventana se cerrará
        st.write("Intentando cerrar la ventana del navegador...")
    
    # Ejecutar JavaScript para cerrar la pestaña del navegador
    close_script = """
    <script>
    function closeWindow() {
        if (confirm("¿Estás seguro de que deseas cerrar la aplicación?")) {
            window.open('', '_self', ''); 
            window.close();
        } else {
            alert("La ventana no se cerró.");
        }
    }
    closeWindow();
    </script>
    """
    st.markdown(close_script, unsafe_allow_html=True)

    # Contenido adicional que solo se muestra si la ventana no se cierra
    st.write("Gracias por utilizar la aplicación.")

if __name__ == '__main__':
    main()
