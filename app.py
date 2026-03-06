import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Student Burnout Detection Dashboard")

# Load dataset
df = pd.read_csv("data/synthetic_student_data.csv")

st.subheader("Dataset Preview")
st.write(df.head())

# Burnout distribution
st.subheader("Burnout Level Distribution")

fig, ax = plt.subplots()
df["burnout_level"].value_counts().plot(kind="bar", ax=ax)
plt.xlabel("Burnout Level")
plt.ylabel("Number of Students")
plt.title("Burnout Level Distribution")

st.pyplot(fig)

# Study hours vs burnout
st.subheader("Study Hours vs Burnout")

fig2, ax2 = plt.subplots()
ax2.scatter(df["study_hours_per_week"], df["burnout_score"])
plt.xlabel("Study Hours")
plt.ylabel("Burnout Level")

st.pyplot(fig2)

# Stress level distribution
st.subheader("Stress Level Distribution")

fig3, ax3 = plt.subplots()
df["stress_level"].hist(ax=ax3)
plt.xlabel("Stress Level")
plt.ylabel("Frequency")

st.pyplot(fig3)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🎓 Student Burnout Detection Dashboard")

# Load dataset
df = pd.read_csv("data/synthetic_student_data.csv")

st.write("Dataset Preview")
st.dataframe(df.head())

# -------------------------
# Burnout Distribution
# -------------------------

st.subheader("Burnout Level Distribution")

fig1, ax1 = plt.subplots()
df["burnout_level"].value_counts().plot(kind="bar", ax=ax1)
ax1.set_xlabel("Burnout Level")
ax1.set_ylabel("Number of Students")

st.pyplot(fig1)

# -------------------------
# Study Hours vs Burnout
# -------------------------

st.subheader("Study Hours vs Burnout Score")

fig2, ax2 = plt.subplots()
ax2.scatter(df["study_hours_per_week"], df["burnout_score"])
ax2.set_xlabel("Study Hours per Week")
ax2.set_ylabel("Burnout Score")

st.pyplot(fig2)

# -------------------------
# Sleep vs Burnout
# -------------------------

st.subheader("Sleep Hours vs Burnout Score")

fig3, ax3 = plt.subplots()
ax3.scatter(df["sleep_hours"], df["burnout_score"])
ax3.set_xlabel("Sleep Hours")
ax3.set_ylabel("Burnout Score")

st.pyplot(fig3)

# -------------------------
# Stress Level Distribution
# -------------------------

st.subheader("Stress Level Distribution")

fig4, ax4 = plt.subplots()
df["stress_level"].value_counts().plot(kind="bar", ax=ax4)
ax4.set_xlabel("Stress Level")
ax4.set_ylabel("Number of Students")

st.pyplot(fig4)

# -------------------------
# Grade vs Burnout
# -------------------------

st.subheader("Grade Average vs Burnout Score")

fig5, ax5 = plt.subplots()
ax5.scatter(df["grade_average"], df["burnout_score"])
ax5.set_xlabel("Grade Average")
ax5.set_ylabel("Burnout Score")

st.pyplot(fig5)

# -------------------------
# Attendance vs Burnout
# -------------------------

st.subheader("Attendance Rate vs Burnout Score")

fig6, ax6 = plt.subplots()
ax6.scatter(df["attendance_rate"], df["burnout_score"])
ax6.set_xlabel("Attendance Rate")
ax6.set_ylabel("Burnout Score")

st.pyplot(fig6)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🎓 Student Burnout Detection Dashboard")

# Load dataset
df = pd.read_csv("data/synthetic_student_data.csv")

st.write("Dataset Preview")
st.dataframe(df.head())

# -------------------------
# Burnout Distribution
# -------------------------

st.subheader("Burnout Level Distribution")

fig1, ax1 = plt.subplots()
df["burnout_level"].value_counts().plot(kind="bar", ax=ax1)
ax1.set_xlabel("Burnout Level")
ax1.set_ylabel("Number of Students")

st.pyplot(fig1)

# -------------------------
# Study Hours vs Burnout
# -------------------------

st.subheader("Study Hours vs Burnout Score")

fig2, ax2 = plt.subplots()
ax2.scatter(df["study_hours_per_week"], df["burnout_score"])
ax2.set_xlabel("Study Hours per Week")
ax2.set_ylabel("Burnout Score")

st.pyplot(fig2)

# -------------------------
# Sleep vs Burnout
# -------------------------

st.subheader("Sleep Hours vs Burnout Score")

fig3, ax3 = plt.subplots()
ax3.scatter(df["sleep_hours"], df["burnout_score"])
ax3.set_xlabel("Sleep Hours")
ax3.set_ylabel("Burnout Score")

st.pyplot(fig3)

# -------------------------
# Stress Level Distribution
# -------------------------

st.subheader("Stress Level Distribution")

fig4, ax4 = plt.subplots()
df["stress_level"].value_counts().plot(kind="bar", ax=ax4)
ax4.set_xlabel("Stress Level")
ax4.set_ylabel("Number of Students")

st.pyplot(fig4)

# -------------------------
# Grade vs Burnout
# -------------------------

st.subheader("Grade Average vs Burnout Score")

fig5, ax5 = plt.subplots()
ax5.scatter(df["grade_average"], df["burnout_score"])
ax5.set_xlabel("Grade Average")
ax5.set_ylabel("Burnout Score")

st.pyplot(fig5)

# -------------------------
# Attendance vs Burnout
# -------------------------

st.subheader("Attendance Rate vs Burnout Score")

fig6, ax6 = plt.subplots()
ax6.scatter(df["attendance_rate"], df["burnout_score"])
ax6.set_xlabel("Attendance Rate")
ax6.set_ylabel("Burnout Score")

st.pyplot(fig6)