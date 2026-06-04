# Web Security & URL Risk Analysis Tool

A Python-based cybersecurity project that analyzes URLs and website content to identify potentially suspicious, spammy, or unsafe websites. The tool combines URL pattern analysis, web scraping, keyword detection, and risk scoring techniques to generate a comprehensive security assessment report.

---

## Key Features

* URL Risk Analysis
* Web Scraping and Content Inspection
* Suspicious Keyword Detection
* Website Accessibility Verification
* Hyperlink Analysis
* Risk Scoring System
* Detailed Security Reporting
* User-Friendly Console Output

---

## Technology Stack

* Python 3
* Requests
* BeautifulSoup4
* Regular Expressions (Regex)

---

## Project Workflow

1. Accepts a website URL from the user.
2. Validates and analyzes the URL structure.
3. Connects to the target website.
4. Scrapes webpage content for analysis.
5. Detects suspicious keywords and patterns.
6. Calculates a risk score.
7. Classifies the website as Low, Medium, or High Risk.
8. Generates a detailed security report.

---

## Risk Levels

| Spam Score | Risk Level | Description                                                                     |
| ---------- | ---------- | ------------------------------------------------------------------------------- |
| 0 – 3      | LOW        | Website appears safe with minimal suspicious indicators.                        |
| 4 – 7      | MEDIUM     | Website contains some suspicious characteristics and should be used cautiously. |
| 8+         | HIGH       | Website shows multiple risk indicators and may be unsafe.                       |

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Web-Security-URL-Risk-Analysis-Tool.git
cd Web-Security-URL-Risk-Analysis-Tool
```

### 2. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python main.py
```

## Screenshots

### Safe Website Detection

![Safe Website](screenshots/safe_url_output.png)

### Suspicious Website Detection

![Suspicious Website](screenshots/suspicious_url_output.png)

### High Risk Website Detection

![High Risk Website](screenshots/high_risk_output.png)

## Sample Output

```text
========================================
      URL RISK ANALYSIS REPORT
========================================

Website    : https://example.com
Status     : Likely Safe Website
Risk Level : LOW
Spam Score : 1/10

Reasons:
✓ No suspicious activity found

Final Verdict:
No major security concerns detected.

========================================
```

---

## Project Structure

```text
Web-Security-URL-Risk-Analysis-Tool/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── screenshots/
│   ├── safe_url_output.png
│   └── suspicious_url_output.png
|   └── high_risk_output.png
│
└── docs/
    └── project_report.pdf
```

---

## Future Enhancements

* Machine Learning-Based Threat Detection
* WHOIS Domain Reputation Analysis
* SSL Certificate Verification
* Real-Time Threat Intelligence Integration
* Browser Extension Support
* GUI Development using Tkinter

---

## Learning Outcomes

Through this project, the following concepts were explored and implemented:

* Web Scraping using BeautifulSoup
* HTTP Requests and Response Handling
* URL Analysis and Pattern Matching
* Regular Expressions (Regex)
* Risk Scoring Algorithms
* Exception Handling in Python
* Cybersecurity Fundamentals
* Data Extraction and Content Analysis
* Software Documentation and GitHub Project Management

---
