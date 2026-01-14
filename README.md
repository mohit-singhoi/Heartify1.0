This is an Ai & ML Based Heart Attack Web Based Prediction System That takes dataset & trained it using 80% of the dataset using ML Model and then test it to rest 20% of the dataset. it takes inputs/symptoms by user/patients and then predict on given symtoms user is in Positive to Heart Attack Risk or Not. This project is currently on the way.


🫀 Heart Attack Prediction – Feature Explanation Guide
1️⃣ Age (age)

What it means:
Age of the patient in years.

Scale:

🟢 Normal: 18 – 40

🟡 Average risk: 41 – 60

🔴 High risk: Above 60

Simple explanation:

“As age increases, the risk of heart disease naturally increases.”

2️⃣ Sex (sex)

What it means:
Biological gender of the patient.

Values:

1 → Male

0 → Female

Risk insight:

Males generally develop heart disease earlier

Females have higher risk after menopause

Simple explanation:

“Gender affects how early heart disease may appear.”

3️⃣ Chest Pain Type (cp)

What it means:
Type of chest pain experienced.

Value	Type	Meaning	Risk
0	Typical Angina	Pain during exertion	🟡
1	Atypical Angina	Unusual chest pain	🟡
2	Non-anginal Pain	Non-heart related pain	🟢
3	Asymptomatic	No pain	🔴 (dangerous)

Simple explanation:

“Sometimes no chest pain can still mean serious heart problems.”

4️⃣ Resting Blood Pressure (trestbps)

What it means:
Blood pressure measured at rest (mm Hg).

Scale:

🟢 Normal: < 120

🟡 Elevated: 120 – 139

🔴 High: ≥ 140

Simple explanation:

“High blood pressure puts extra strain on the heart.”

5️⃣ Cholesterol (chol)

What it means:
Serum cholesterol level (mg/dL).

Scale:

🟢 Normal: < 200

🟡 Borderline: 200 – 239

🔴 High: ≥ 240

Simple explanation:

“High cholesterol can block blood flow to the heart.”

6️⃣ Fasting Blood Sugar (fbs)

What it means:
Blood sugar after fasting.

Values:

0 → ≤ 120 mg/dL (Normal)

1 → > 120 mg/dL (High)

Simple explanation:

“High blood sugar damages blood vessels and increases heart risk.”

7️⃣ Resting ECG (restecg)

What it means:
Electrocardiogram results at rest.

Value	Result	Risk
0	Normal	🟢
1	ST-T abnormality	🟡
2	Left ventricular hypertrophy	🔴

Simple explanation:

“ECG shows how well the heart’s electrical system works.”

8️⃣ Maximum Heart Rate (thalach)

What it means:
Highest heart rate achieved during exercise.

Scale (depends on age):

🟢 Normal: 140 – 190

🟡 Low: 120 – 139

🔴 Very Low: < 120

Simple explanation:

“A heart that cannot reach a good rate during exercise may be weak.”

9️⃣ Exercise Induced Angina (exang)

What it means:
Chest pain during exercise.

Values:

0 → No

1 → Yes

Risk:

Yes → 🔴 High risk

Simple explanation:

“Chest pain during activity is a strong warning sign.”

🔟 ST Depression (oldpeak)

What it means:
Change in ECG during exercise compared to rest.

Scale:

🟢 Normal: 0 – 1

🟡 Moderate: 1 – 2

🔴 Severe: > 2

Simple explanation:

“Higher values mean reduced blood flow to the heart.”

1️⃣1️⃣ Slope of ST Segment (slope)

What it means:
Shape of ECG ST segment during exercise.

Value	Type	Risk
0	Upsloping	🟢
1	Flat	🟡
2	Downsloping	🔴

Simple explanation:

“Downward slope often indicates serious heart problems.”

1️⃣2️⃣ Number of Major Vessels (ca)

What it means:
Number of blocked major blood vessels (0–3).

Scale:

🟢 0 → No blockage

🟡 1 → Mild blockage

🔴 2–3 → Severe blockage

Simple explanation:

“More blocked vessels means less blood reaching the heart.”

1️⃣3️⃣ Thalassemia (thal)

What it means:
Blood disorder related to oxygen transport.

Value	Meaning	Risk
1	Normal	🟢
2	Fixed Defect	🟡
3	Reversible Defect	🔴

Simple explanation:

“Oxygen supply problems can stress the heart.”