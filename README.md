 🚨 AgentOps AI – Incident Investigator

An AI-inspired **incident analysis system** built using Streamlit that helps analyze IT logs and generate structured incident reports with severity, root cause, and recommendations.


 📌 Problem Statement

In real-world IT operations, engineers deal with large volumes of unstructured incident logs. Manually identifying severity and root cause takes time.

👉 This project automates that process using a smart rule-based intelligence engine.



⚙️ Features

* 🧠 Smart incident log analysis
* 🚨 Severity detection (LOW / MEDIUM / HIGH / CRITICAL)
* 🔍 Root cause identification
* 💡 Automated recommendations
* 📊 Structured incident report
* 🤖 AI-style reasoning explanation
* 🚦 Real-time status indicator
* 📌 Incident ID + timestamp generation



🛠 Tech Stack

* Python
* Streamlit
* Random module (for incident ID)
* Datetime module



🧠 How It Works

1. User pastes incident log
2. System parses keywords (CPU, Memory, Disk, Error)
3. A scoring engine calculates severity
4. Root cause + summary are generated
5. Recommendations are displayed
6. Final structured incident report is shown



 🏗 Architecture

```
User Input (Incident Log)
        ↓
Log Parsing Engine
        ↓
Keyword Detection (CPU / Memory / Disk / Error)
        ↓
Scoring-Based Intelligence System
        ↓
Severity Classification Engine
        ↓
Report Generator
        ↓
Streamlit UI Dashboard
```

---

 🚀 How to Run Locally

```bash
# Clone repo
git clone https://github.com/shanvii3singhh/agentops-ai-incident-investigator.git

# Go to project folder
cd agentops-ai-incident-investigator

# Install dependencies
pip install streamlit

# Run app
streamlit run app.py
```

---

 📊 Example Incident

```
CPU usage is very high and memory error detected
```

 Output:

* Severity: CRITICAL
* Root Cause: Resource exhaustion
* Recommendations: Scale resources, check logs



 🔥 Key Highlights

* No external API required (fully free)
* Fast + lightweight system
* Works in real-time
* Hackathon-ready UI
* Simulates AI reasoning without paid models


 🎯 Future Improvements

* Add real AI model integration (LLM-based analysis)
* Incident history database
* Export report as PDF
* Charts & analytics dashboard
* Email alert system



 👩‍💻 Author

Built by **Shanvi Singh**
For AgentOps Hackathon 🚀



 🏆 Impact

This project demonstrates how **simple rule-based intelligence** can mimic AI-driven incident investigation systems used in real-world DevOps environments.



