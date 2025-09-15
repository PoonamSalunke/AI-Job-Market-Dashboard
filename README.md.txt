🚀 AI Job Market Trends Analysis

📌 Project Overview
This project analyzes trends in the **AI job market** using a real-world dataset of job postings.  
The goal is to uncover insights such as:
- Salary trends across experience levels
- Job distribution by location
- Remote work opportunities
- In-demand skills
- Industry and education requirements

The project also includes a **Power BI Dashboard** for interactive exploration.

---

📂 Project Structure
AI-Job-Market-Trends-Analysis/
│── data/ # Raw & cleaned datasets
│── notebooks/ # Jupyter notebooks for analysis
│ └── analysis.ipynb
│── scripts/ # Python scripts
│ ├── scrape_jobs.py # Example web scraping script
│ └── clean_data.py # Data cleaning script
│── visuals/ # Exported plots and charts
│── reports/ # PDF / PPT reports
│── dashboard/ # Power BI dashboard files
│── requirements.txt # Python dependencies
│── .gitignore # Ignored files for Git
│── README.md # Project documentation



---

⚙️ Installation & Setup

1. **Clone the repo**:
   ```bash
   git clone https://github.com/your-username/AI-Job-Market-Trends-Analysis.git
   cd AI-Job-Market-Trends-Analysis
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
📊 How to Run
Clean the dataset:

bash
Copy code
python scripts/clean_data.py
Run the Jupyter Notebook:

bash
Copy code
jupyter notebook notebooks/analysis.ipynb
Explore the Dashboard:

Open the Power BI file inside /dashboard/ (when added).

Interact with visuals for salary, skills, and trends.

🔍 Key Insights
Senior-level jobs have the highest salaries.

Remote jobs are increasing in demand.

Python, SQL, and Machine Learning are the most requested skills.

Certain regions are emerging hubs for AI talent.

🛠️ Tools & Technologies
Python (Pandas, NumPy, Matplotlib, Seaborn)

BeautifulSoup + Requests (for web scraping demo)

Power BI (dashboard visualization)

Jupyter Notebook (exploratory analysis)

📌 Next Steps
Add more scraping sources for live job data

Expand Power BI dashboard with interactive filters

Automate data refresh pipeline

✨ Author
👩‍💻 Poonam Salunke
📍 Data Analyst | Fresher MCS Post-Graduate
🔗 LinkedIn Profile- https://www.linkedin.com/in/poonam-salunke-p1/