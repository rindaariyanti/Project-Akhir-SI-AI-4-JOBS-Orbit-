import numpy as np
import pickle
import streamlit as st
from PIL import Image

# Load the saved model
loaded_model = pickle.load(open(r'model.pkl', 'rb'))

# Create a function for Prediction
def prediction(input_data):

    # Change the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return "Calon Nasabah BERMINAT Membuka Tabungan Berjangka"
    elif (prediction[0] == 1):
      return "Calon Nasabah TIDAK BERMINAT Membuka Tabungan Berjangka"
    else:
      return "Hasil tidak dapat ditemukan"

image = Image.open('header.jpg')

def main():
    
    # Judul
    st.markdown("<h1 style='text-align: center;color: rgb(106, 90, 205);'>Website Prediksi Calon Nasabah yang Akan Membuka Tabungan Deposito Berjangka Menggunakan Support Vector Machine (SVM)</h1>", unsafe_allow_html=True)
    st.markdown("""---""")
    
    st.image(image)
    
    # Proses Input
    st.markdown("""---""")
    st.markdown("<h1 style='text-align: center;'>Selamat Datang !</h1>", unsafe_allow_html=True)
    st.markdown("""---""")
    st.markdown(
      """
      Website ini dapat digunakan untuk memprediksi kemungkinan nasabah membuka rekening 
      deposito berdasarkan variabel-variabel yang dimasukkan. Website ini dibangun menggunakan 
      algoritma Support Vector Machine (SVM) untuk mengidentifikasi kategori calon nasabah 
      potensial yang diprediksi berminat membuka rekening deposito dengan menggunakan metode kasifikasi 
      yang telah dibangun

      Oleh Kelompok 6 Kelas Engine : 

      1.  Hawa Nur Rahma
      2.  Rinda Ariyanti
      3.  The Syifaul Maula
      4.  Misi Tri Cahyanti
      5.  Aldi Mahendra 
      6.  Didin Mahfudin
      """
    )
    st.markdown("""---""")
    st.markdown("<h1 style='text-align: center;'>Masukkan Data Calon Nasabah</h1>", unsafe_allow_html=True)
    st.markdown("""---""")
    age = st.number_input('Age', min_value=1)
    job = st.slider('Type of Job (0=admin; 1=technician; 2=services; 3=management; 4=retired; 5=blue-collar; 6=unemployed; 7=entrepreneur; 8=housemaid; 9=unknown; 10=self-employed; 11=student)', 0, 11, 0)
    marital = st.slider('Marital status (0=married; 1=single; 2=divorced)', 0,2,0)
    education = st.slider('Education (0=secondary; 1=tertiary; 2=primary; 3=unknown)', 0,3,0)
    default = st.slider('Has credit in default? (0=no; 1=yes)', 0, 1, 0)
    balance = st.number_input('Average yearly balance, in euros', min_value=0)
    housing = st.slider('Has housing loan? (0=yes; 1=no)', 0, 1, 0)
    loan = st.slider('Has personal loan? (0=no; 1=yes)', 0, 1, 0)
    contact = st.slider('Contact communication type (0=unknown; 1=cellular; 2=telephone)', 0,2,0)
    day = st.number_input('Last contact day of the month', min_value=1)
    month = st.slider('Last contact month of year (0=may; 1=jun; 2=jul; 3=aug; 4=oct; 5=nov; 6=dec; 7=jan; 8=feb; 9=mar; 10=apr; 11=sep)', 0,11,0)
    duration = st.number_input('Last contact duration, in seconds', min_value=0)
    campaign = st.slider('Number of contacts performed during this campaign and for this client', 0, 100, 0)
    pdays = st.number_input('Number of days that passed by after the client was last contacted from a previous campaign', min_value=-1)
    previous = st.number_input('Number of contacts performed before this campaign and for this client', min_value=0)
    poutcome = st.slider('Outcome of the previous marketing campaign (0=unknown; 1=other; 2=failure; 3=success)', 0,3,0)
    
    # Code for Prediction
    diagnosis = ''
    
    # Tombol Cetak Hasil
    st.header('Hasil Prediksi')
    if st.button('Cetak Hasil Prediksi'):
        diagnosis = prediction([age, job, marital, education, default, balance, housing, loan, contact, day, month, duration, campaign, pdays, previous, poutcome])
        
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()


