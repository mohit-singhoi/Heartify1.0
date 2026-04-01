This is an Ai & ML Based Heart Attack Web Based Prediction System That takes dataset & trained it using 80% of the dataset using ML Model and then test it to rest 20% of the dataset. it takes inputs/symptoms by user/patients and then predict on given symtoms user is in Positive to Heart Attack Risk or Not. This project development  is currently on the way.



# 🫀 Heart Attack Prediction – Feature Explanation Guide

This guide explains the features used in the Heart Attack Prediction system and what their values mean for risk assessment.

---

## 1️⃣ Age (`age`)
**Meaning:** Age of the patient in years  
**Scale & Risk:**
- 🟢 Normal: 18 – 40  
- 🟡 Average risk: 41 – 60  
- 🔴 High risk: Above 60  
**Simple Explanation:** "As age increases, the risk of heart disease naturally increases."

---

## 2️⃣ Sex (`sex`)
**Meaning:** Biological gender of the patient  
**Values & Risk:**
- 1 → Male (develop heart disease earlier)  
- 0 → Female (higher risk after menopause)  
**Simple Explanation:** "Gender affects how early heart disease may appear."

---

## 3️⃣ Chest Pain Type (`cp`)
| Value | Type               | Risk    |
|-------|------------------|---------|
| 0     | Typical Angina     | 🟡      |
| 1     | Atypical Angina    | 🟡      |
| 2     | Non-anginal Pain   | 🟢      |
| 3     | Asymptomatic       | 🔴      |
**Simple Explanation:** "Sometimes no chest pain can still mean serious heart problems."

---

## 4️⃣ Resting Blood Pressure (`trestbps`)
**Scale & Risk:**
- 🟢 < 120 → Normal  
- 🟡 120 – 139 → Elevated  
- 🔴 ≥ 140 → High  
**Simple Explanation:** "High blood pressure puts extra strain on the heart."

---

## 5️⃣ Cholesterol (`chol`)
**Scale & Risk:**
- 🟢 < 200 → Normal  
- 🟡 200 – 239 → Borderline  
- 🔴 ≥ 240 → High  
**Simple Explanation:** "High cholesterol can block blood flow to the heart."

---

## 6️⃣ Fasting Blood Sugar (`fbs`)
**Values & Risk:**
- 0 → ≤ 120 mg/dL → Normal  
- 1 → > 120 mg/dL → High  
**Simple Explanation:** "High blood sugar damages blood vessels and increases heart risk."

---

## 7️⃣ Resting ECG (`restecg`)
| Value | Result                        | Risk |
|-------|-------------------------------|------|
| 0     | Normal                        | 🟢   |
| 1     | ST-T abnormality              | 🟡   |
| 2     | Left ventricular hypertrophy  | 🔴   |
**Simple Explanation:** "ECG shows how well the heart’s electrical system works."

---

## 8️⃣ Maximum Heart Rate (`thalach`)
**Scale & Risk:**
- 🟢 140 – 190 → Normal  
- 🟡 120 – 139 → Low  
- 🔴 < 120 → Very Low  
**Simple Explanation:** "A heart that cannot reach a good rate during exercise may be weak."

---

## 9️⃣ Exercise Induced Angina (`exang`)
**Values & Risk:**
- 0 → No  
- 1 → Yes → 🔴 High risk  
**Simple Explanation:** "Chest pain during activity is a strong warning sign."

---

## 🔟 ST Depression (`oldpeak`)
**Scale & Risk:**
- 🟢 0 – 1 → Normal  
- 🟡 1 – 2 → Moderate  
- 🔴 > 2 → Severe  
**Simple Explanation:** "Higher values mean reduced blood flow to the heart."

---

## 1️⃣1️⃣ Slope of ST Segment (`slope`)
| Value | Type           | Risk |
|-------|----------------|------|
| 0     | Upsloping       | 🟢   |
| 1     | Flat            | 🟡   |
| 2     | Downsloping     | 🔴   |
**Simple Explanation:** "Downward slope often indicates serious heart problems."

---

## 1️⃣2️⃣ Number of Major Vessels (`ca`)
**Scale & Risk:**
- 0 → No blockage → 🟢  
- 1 → Mild blockage → 🟡  
- 2–3 → Severe blockage → 🔴  
**Simple Explanation:** "More blocked vessels means less blood reaching the heart."

---

## 1️⃣3️⃣ Thalassemia (`thal`)
**Values & Risk:**
- 1 → Normal → 🟢  
- 2 → Fixed Defect → 🟡  
- 3 → Reversible Defect → 🔴  
**Simple Explanation:** "Oxygen supply problems can stress the heart."



