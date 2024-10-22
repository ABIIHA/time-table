import streamlit as st
import pandas as pd
from datetime import datetime

st.title("Student's Daily Timetable")

# Input: Number of subjects
num_subjects = st.number_input('Enter number of subjects:', min_value=1, max_value=10, value=6)

# Input: Subject details
subjects = []
for i in range(num_subjects):
    subject = st.text_input(f'Subject {i+1} name:', f'Subject {i+1}')
    start_time = st.time_input(f'Start time for {subject}:', datetime.now().time())
    end_time = st.time_input(f'End time for {subject}:', datetime.now().time())
    subjects.append({"Subject": subject, "Start Time": start_time, "End Time": end_time})

# Convert to DataFrame
df = pd.DataFrame(subjects)

# Display the timetable
st.subheader("Your Daily Timetable")
st.write(df)

# Allow download as CSV
csv = df.to_csv(index=False)
st.download_button(label="Download timetable as CSV", data=csv, file_name='timetable.csv', mime='text/csv')
