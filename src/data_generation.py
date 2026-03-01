import numpy as np
import pandas as pd

np.random.seed(42)
n = 2000

data = pd.DataFrame({
    "student_id": range(1, n+1),
    "attendance_rate": np.random.uniform(40, 100, n),
    "avg_assignment_delay": np.random.uniform(0, 10, n),
    "lms_login_per_week": np.random.uniform(0, 20, n),
    "study_hours_per_week": np.random.uniform(0, 40, n),
    "grade_average": np.random.uniform(40, 95, n),
    "sentiment_score": np.random.uniform(-1, 1, n),
    "stress_level": np.random.uniform(1, 10, n),
    "sleep_hours": np.random.uniform(3, 9, n),
    "extracurricular_participation": np.random.randint(0, 6, n)
})

# Burnout score formula
data["burnout_score"] = (
    0.25*(100 - data["attendance_rate"]) +
    2*(data["avg_assignment_delay"]) +
    1.5*(10 - data["study_hours_per_week"]/4) +
    5*(data["stress_level"]) -
    10*(data["sentiment_score"])
)

data["burnout_score"] = 100 * (data["burnout_score"] - data["burnout_score"].min()) / \
                        (data["burnout_score"].max() - data["burnout_score"].min())

# Burnout level
bins = [0, 33, 66, 100]
labels = ["Low", "Medium", "High"]
data["burnout_level"] = pd.cut(data["burnout_score"], bins=bins, labels=labels)

# Save dataset

import os

output_path = os.path.join(os.path.dirname(__file__), "..", "data", "synthetic_student_data.csv")
data.to_csv(output_path, index=False)

print("Dataset generated successfully!")