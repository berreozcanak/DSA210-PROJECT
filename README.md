# DSA 210: Introduction to Data Science - Term Project
**Term:** 2025-2026 Spring
**Student:** Berre Özçanak  
**Student ID:** 32693  

---

## Project Proposal: Study Environment, Focus, and Productivity

### Motivation and Problem Statement
The goal of this project is to investigate how various environmental factors—specifically location, noise level, and background audio—are associated with self-reported focus and productivity levels among university students[cite: 10]. [cite_start]Since students often struggle to find "optimal" study conditions, this analysis aims to identify whether specific environments (e.g., library vs. café) correlate with higher satisfaction and longer study durations[cite: 5].

### Data Collection Strategy
In accordance with the project guidelines that allow personal or self-collected datasets, I am working with a self-generated dataset[cite: 17].

* **Data Source:** Data is being sourced from university students at Sabancı University and other institutions.
* **Collection Method:** Data is collected via a digital survey (Google Forms) distributed through student communication channels.
* **Form Link:** [View Survey](https://docs.google.com/forms/d/e/1FAIpQLSfagRjNy8rFeBq2zyq9Wf3JXuBWCWk9n6SQZwIEdwVh-OqRLg/viewform?usp=publish-editor)
* **Variables:** * **Independent:** Study location, noise level (1–5 scale), audio type (none, instrumental, lyrical).
    * **Control:** Sleep hours, daily screen time.
    * **Dependent:** Focus and productivity scores (1–10 scale).

### Data Characteristics
* **Sample Size:** Currently 17 samples collected; aiming for a minimum of **100 samples** for statistical robustness.
* **Format:** Raw results will be exported as a `.csv` file and processed using **Python**.
* **Features:** The final dataset will consist of approximately **15–20 features**, including both categorical and numerical data.

### Planned Methodology
The project will follow the full data science pipeline:
1.  **EDA:** Visualizing the distribution of study habits using Python libraries (e.g., Pandas, Matplotlib, Seaborn).
2.  **Hypothesis Testing:** Analyzing if noise levels significantly impact focus scores using statistical techniques.
3.  **Machine Learning:** Implementing a **Random Forest Classifier** to predict "High" vs. "Low" productivity sessions based on environmental inputs.
