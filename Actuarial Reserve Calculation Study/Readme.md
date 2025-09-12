# Actuarial Reserve Calculation Study

## 📌 Project Overview
This actuarial study was conducted for **Hábitat para la Humanidad Honduras** to evaluate the sustainability of its **Damage Coverage and Balance Guarantee Program (PCDGS)**.  
The program protects housing loans by:
- Covering property damages caused by catastrophic events.
- Guaranteeing outstanding loan balances in the event of death or permanent disability of beneficiaries.

The study assessed the program’s **technical rates, reserves, and risk exposures** to ensure long-term viability and strengthen its role as a financial inclusion tool for low-income families in Honduras:contentReference[oaicite:0]{index=0}.

---

## 🏗️ Methodology

### 1. Portfolio Analysis
- Cleaned and validated loan data (∼4,500 active loans, as of June 2024).  
- Assessed eligibility by age and loan term.  
- Analyzed arrears and categorized by type of housing solution (housing units, improvements, condominiums).  

### 2. Risk Analysis
- Separated **minor** (≤ L.25,000) vs **major** (> L.25,000) damages.  
- Estimated **frequency and severity** using historical data (2011–2024).  
- Modeled with:
  - **Weibull distributions** for minor damages.
  - **Empirical sampling** for major damages due to heavy-tailed losses:contentReference[oaicite:1]{index=1}.

### 3. Monte Carlo Simulations
- 10,000 iterations to estimate annual aggregate losses.  
- Considered:
  - Damage frequency (Poisson distribution).  
  - Severity distributions.  
  - Administrative expenses (16.17%).  
  - Insurance contracts (MAPFRE) covering catastrophic risks.  

### 4. Reserve & Rate Calculation
- Compared required reserves under **percentiles P70, P90, P95, P99, P99.5**.  
- Evaluated sufficiency of current technical rate (∼1.03‰ in prior study).  
- Recommended adjustment to **2.0‰** under P99.5 for prudence:contentReference[oaicite:2]{index=2}.

---

## 📊 Key Results
- **Increased risk exposure**: frequency and severity of catastrophic damages higher than 2011–2016 study.  
- **Annual expected loss**: L. 773,000 (doubling previous period).  
- **Insurance analysis**: although payout efficiency was low (∼18% recovery vs premiums), coverage remains essential for risk concentration in housing projects.  
- **Reserve sufficiency**: adopting conservative percentiles ensures resilience against climate change and extreme events.  

---

## ✅ Benefits
- **Financial inclusion**: program reaches over 50% women and mainly beneficiaries aged 30–40.  
- **Resilience**: strengthens Habitat’s ability to face hurricanes, earthquakes, and other disasters.  
- **Sustainability**: ensures long-term viability by aligning premiums, reserves, and exposures.  

---

## 🚀 Deliverables
- Full actuarial study report (`Estudio_actuarial.pdf`).  
- Monte Carlo simulation scripts (Python).  
- Reserve adequacy models.  
- Visualization of frequency, severity, and reserve sufficiency scenarios.

---

## 🔒 Confidentiality Disclosure
This repository contains **methodologies, models, and summarized results** for portfolio demonstration.  
**Individual-level loan data and internal financial records remain confidential** and are not included here.
