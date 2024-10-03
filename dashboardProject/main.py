import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("Bike Sharing Dashboard")
st.sidebar.markdown("### Analisis Penggunaan Sepeda")

date_range = st.sidebar.date_input("Pilih Rentang Waktu", [])

day_data = pd.read_csv('dashboardProject/day.csv')

day_data['dteday'] = pd.to_datetime(day_data['dteday'])

st.title("Dashboard Penggunaan Sepeda")

# --------------------- Visualisasi 1: Pengaruh Cuaca terhadap Penggunaan Sepeda ---------------------
st.subheader("Pengaruh Kondisi Cuaca terhadap Jumlah Pengguna Sepeda")

weather_group = day_data.groupby('weathersit')['cnt'].mean().reset_index()

fig1, ax1 = plt.subplots()
sns.barplot(x='weathersit', y='cnt', data=weather_group, ax=ax1)
ax1.set_title('Pengaruh Kondisi Cuaca terhadap Pengguna Sepeda')
ax1.set_xlabel('Kondisi Cuaca (1: Cerah, 2: Mendung, 3: Hujan)')
ax1.set_ylabel('Rata-rata Jumlah Pengguna Sepeda')
st.pyplot(fig1)

# --------------------- Visualisasi 2: Pola Musiman Penggunaan Sepeda ---------------------
st.subheader("Pola Penggunaan Sepeda Berdasarkan Musim")

season_group = day_data.groupby('season')['cnt'].mean().reset_index()

season_labels = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
season_group['season'] = season_group['season'].map(season_labels)

fig2, ax2 = plt.subplots()
sns.barplot(x='season', y='cnt', data=season_group, ax=ax2)
ax2.set_title('Penggunaan Sepeda Berdasarkan Musim')
ax2.set_xlabel('Musim')
ax2.set_ylabel('Rata-rata Jumlah Pengguna Sepeda')
st.pyplot(fig2)

# --------------------- Visualisasi 3: Penggunaan Sepeda oleh Casual vs Registered ---------------------
st.subheader("Penggunaan Sepeda oleh Pengguna Casual dan Terdaftar")

user_type_group = day_data[['casual', 'registered']].mean()

fig3, ax3 = plt.subplots()
user_type_group.plot(kind='bar', ax=ax3, color=['skyblue', 'salmon'])
ax3.set_title('Rata-rata Penggunaan Sepeda: Casual vs Registered')
ax3.set_xlabel('Tipe Pengguna')
ax3.set_ylabel('Rata-rata Jumlah Pengguna')
st.pyplot(fig3)

st.markdown("### Insight:")
st.markdown("- **Pengaruh Cuaca**: Cuaca cerah cenderung meningkatkan penggunaan sepeda, sedangkan cuaca mendung dan hujan menurunkan jumlah pengguna.")
st.markdown("- **Musim**: Penggunaan sepeda paling tinggi selama musim gugur dan panas, dan paling rendah selama musim semi.")
st.markdown("- **Pengguna Casual vs Registered**: Pengguna terdaftar menggunakan sepeda lebih sering dibandingkan pengguna kasual, terutama pada hari kerja.")

