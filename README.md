
# 🚨 AgentOps AI – Incident Investigator

AgentOps AI is a lightweight incident investigation platform that helps engineers analyze raw IT incident logs and generate structured incident reports. The system automatically evaluates incident severity, identifies likely root causes, and provides actionable recommendations to accelerate troubleshooting and incident response.

---

## 💡 Problem Statement

During system outages and operational failures, engineers often spend valuable time manually reviewing logs, determining incident severity, and identifying possible root causes.

This process is:

* Time-consuming
* Inconsistent across teams
* Difficult during high-pressure incidents

AgentOps AI addresses this challenge by transforming unstructured logs into actionable incident insights.

---

## 🚀 Solution

AgentOps AI analyzes incident logs using a rule-based intelligence pipeline that:

* Extracts critical operational signals
* Evaluates incident impact
* Assigns severity levels
* Detects probable root causes
* Generates remediation recommendations
* Produces structured incident reports

---

## ⚙️ Key Features

* Automated incident log analysis
* Severity classification (LOW, MEDIUM, HIGH, CRITICAL)
* Rule-based root cause detection
* Actionable recommendation generation
* Structured incident reporting
* Real-time analysis through Streamlit
* Incident ID and timestamp generation

---

## 🛠 Tech Stack

* Python
* Streamlit
* Datetime
* Random

---

## 🧠 How It Works

1. The user submits an incident log.
2. The system extracts important keywords and indicators.
3. A scoring engine evaluates the potential impact.
4. Severity is classified based on predefined rules.
5. Root cause patterns are identified.
6. Recommendations are generated.
7. A structured incident report is displayed.

---

## 🏗 Architecture

┌─────────────────────────────────────────────────────────────┐
│                     AgentOps AI                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Incident Logs                                              │
│         │                                                   │
│         ▼                                                   │
│  Log Parsing & Analysis                                     │
│         │                                                   │
│         ▼                                                   │
│  Rule-Based Scoring Engine                                  │
│         │                                                   │
│    ┌────┴────────────┐                                      │
│    ▼                 ▼                                      │
│ Severity         Root Cause                                │
│ Analysis         Detection                                 │
│    └───────┬────────┘                                      │
│            ▼                                                │
│  Recommendation Generator                                   │
│            ▼                                                │
│  Structured Incident Report                                 │
│            ▼                                                │
│  Streamlit Dashboard                                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘

---

## 📸 Screenshots

### Input Screen

(Add Screenshot)

### Incident Report

(Add Screenshot)

---

## 🚀 Example

### Input

CPU usage is very high and memory error detected in production system

### Output

**Severity:** CRITICAL

**Category:** System Resource Failure

**Root Cause:** High CPU utilization combined with memory pressure leading to resource exhaustion.

**Recommendations:**

* Scale system resources
* Investigate memory leaks
* Enable monitoring and alerting

---

## 📈 Impact

AgentOps AI reduces the effort required to investigate incidents by converting raw operational logs into structured and actionable reports. This enables faster incident triage, more consistent analysis, and improved operational awareness.

---

## 🔮 Future Enhancements

* LLM-powered incident analysis
* Historical incident tracking
* PDF report exports
* Dashboard analytics
* Slack and email integrations

---

## ⚡ Installation

git clone <repository-url>

cd agentops-ai

pip install -r requirements.txt

streamlit run app.py
