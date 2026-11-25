# 🏏 Cricbuzz LiveStats

**Real-Time Cricket Insights & SQL-Based Analytics**

A comprehensive cricket analytics dashboard that integrates live data from the Cricbuzz API with a SQL database to create an interactive web application. Built with Python, Streamlit, and MySQL.

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.46.1-FF4B4B)](https://streamlit.io/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0%2B-4479A1)](https://www.mysql.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Page Descriptions](#-page-descriptions)
- [SQL Practice Queries](#-sql-practice-queries)
- [Business Use Cases](#-business-use-cases)
- [Development](#-development)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

- **⚡ Real-time Match Updates** - Live cricket match data from Cricbuzz API
- **📊 Detailed Player Statistics** - Comprehensive batting, bowling, and fielding stats
- **📈 SQL-Driven Analytics** - 25+ practice SQL queries from beginner to advanced
- **🛠️ Full CRUD Operations** - Create, Read, Update, Delete player records
- **📉 Interactive Visualizations** - Charts and graphs using Plotly and Matplotlib
- **🔍 Advanced Search & Filters** - Find players by name, country, role, and more
- **📱 Responsive Design** - Works seamlessly on desktop and mobile devices
- **🗄️ Database-Agnostic** - Supports PostgreSQL, MySQL, and SQLite

---

## 🛠️ Tech Stack

### **Backend**
- **Python 3.11+** - Core programming language
- **Streamlit 1.46.1** - Web application framework
- **MySQL Connector** - Database connectivity
- **SQLAlchemy 2.0.42** - SQL toolkit and ORM

### **Data Processing**
- **Pandas 2.3.1** - Data manipulation and analysis
- **NumPy 2.3.1** - Numerical computing

### **API Integration**
- **Requests 2.32.4** - HTTP library for API calls
- **REST API** - Cricbuzz Cricket API via RapidAPI

### **Visualization**
- **Plotly 6.2.0** - Interactive charts
- **Matplotlib 3.10.5** - Static plots

### **Development Tools**
- **pytest 8.4.1** - Testing framework
- **black 25.1.0** - Code formatter
- **flake8 7.3.0** - Code linter

---

## 📁 Project Structure

```
cricbuzz_livestats/
│
├── app.py                      # Main entry point for the Streamlit app
├── config.py                   # Configuration and environment variables
├── requirements.txt            # Required Python packages
├── README.md                   # Project overview and setup instructions
├── .env                        # Environment variables (API keys, DB credentials)
│
├── pages/                      # Contains individual Streamlit pages
│   ├── home.py                 # Overview and About the Project page
│   ├── live_matches.py         # Displays live match data from Cricbuzz API
│   ├── top_stats.py            # Shows top batting/bowling stats
│   ├── sql_queries.py          # SQL query interface and analytics
│   └── crud_operations.py      # Perform CRUD on player stats
│
├── utils/                      # Utility files
│   └── db_connection.py        # SQL database connection logic
│
├── notebooks/                  # Practice Jupyter notebooks (Optional)
│   └── data_fetching.ipynb     # For testing API calls and pushing to DB
│
├── Api/                        # API integration modules
│   ├── client.py               # Base API client
│   ├── matches.py              # Match-related API endpoints
│   ├── players.py              # Player-related API endpoints
│   └── rankings.py             # Rankings API endpoints
│
├── Services/                   # Business logic layer
│   ├── match_service.py        # Match data processing
│   ├── player_service.py       # Player data processing
│   ├── ranking_service.py      # Rankings processing
│   ├── analytics_service.py    # Analytics calculations
│   └── crud_service.py         # CRUD operations logic
│
└── Database/                   # Database-related files
    ├── connection.py           # Legacy database connection (kept for compatibility)
    ├── Repository.py           # Data access layer
    ├── create_tables.sql       # SQL script to create tables
    └── seed_data.sql           # Sample data for testing
```

---

## 🚀 Installation

### **Prerequisites**
- Python 3.11 or higher
- MySQL 8.0 or higher (or PostgreSQL/SQLite)
- RapidAPI account with Cricbuzz API subscription

### **Step 1: Clone the Repository**

```bash
git clone https://github.com/yourusername/cricbuzz-livestats.git
cd cricbuzz-livestats
```

### **Step 2: Create Virtual Environment**

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### **Step 3: Install Dependencies**

```bash
pip install -r requirements.txt
```

### **Step 4: Set Up Database**

1. Create a MySQL database:
```sql
CREATE DATABASE cricbuzz_db;
```

2. Run the table creation script:
```bash
mysql -u your_username -p cricbuzz_db < Database/create_tables.sql
```

3. (Optional) Load seed data:
```bash
mysql -u your_username -p cricbuzz_db < Database/seed_data.sql
```

### **Step 5: Configure Environment Variables**

Create a `.env` file in the project root:

```env
# RapidAPI Credentials
RAPIDAPI_KEY=your_rapidapi_key_here
RAPIDAPI_HOST=cricbuzz-cricket.p.rapidapi.com
BASE_URL=https://cricbuzz-cricket.p.rapidapi.com

# Database Configuration
DB_HOST=localhost
DB_PORT=3306
DB_NAME=cricbuzz_db
DB_USER=your_db_username
DB_PASSWORD=your_db_password
```

### **Step 6: Run the Application**

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

---

## ⚙️ Configuration

### **API Configuration**

1. Sign up for a free account at [RapidAPI](https://rapidapi.com/)
2. Subscribe to the [Cricbuzz Cricket API](https://rapidapi.com/cricbuzz-official/api/cricbuzz-cricket)
3. Copy your API key to the `.env` file

### **Database Configuration**

The application supports multiple database systems:

**MySQL:**
```python
DB_HOST=localhost
DB_PORT=3306
```

**PostgreSQL:**
```python
DB_HOST=localhost
DB_PORT=5432
```

**SQLite:**
```python
DB_NAME=cricbuzz.db
```

---

## 📖 Usage

### **Running the Application**

```bash
streamlit run app.py
```

### **Navigating the Dashboard**

1. **Home** - Overview of the project and features
2. **Live Matches** - View ongoing cricket matches in real-time
3. **Top Stats** - Analyze top batting and bowling statistics
4. **SQL Queries** - Execute pre-built SQL queries or write custom ones
5. **CRUD Operations** - Manage player data with forms

### **Using the Jupyter Notebook**

```bash
jupyter notebook notebooks/data_fetching.ipynb
```

The notebook includes:
- API testing examples
- Database connection tests
- Data analysis samples
- SQL query practice

---

## 📄 Page Descriptions

### **1. Home Page** (`pages/home.py`)
- Project overview and introduction
- Features and tech stack
- Quick navigation guide
- Project structure diagram

### **2. Live Matches** (`pages/live_matches.py`)
- Real-time match updates from Cricbuzz API
- Detailed scorecards with team information
- Venue details and match status
- Auto-refresh functionality

### **3. Top Stats** (`pages/top_stats.py`)
- Top 10 batsmen by runs scored
- Top 10 bowlers by wickets taken
- Interactive charts and visualizations
- Filter by cricket format (Test, ODI, T20I)

### **4. SQL Queries** (`pages/sql_queries.py`)
- 25+ pre-built SQL queries organized by difficulty
- Beginner (Q1-8): Basic SELECT, WHERE, GROUP BY
- Intermediate (Q9-16): JOINs, subqueries, aggregates
- Advanced (Q17-25): Window functions, CTEs, complex analytics
- Custom query editor with syntax highlighting
- Download results as CSV

### **5. CRUD Operations** (`pages/crud_operations.py`)
- **Create**: Add new player records
- **Read**: Search and filter players
- **Update**: Modify existing player information
- **Delete**: Remove players from database
- Form-based UI for easy data management

---

## 📊 SQL Practice Queries

The project includes **25 SQL practice questions** covering:

### **Beginner Level (Q1-8)**
- Basic SELECT statements
- WHERE clause filtering
- GROUP BY aggregations
- ORDER BY sorting

### **Intermediate Level (Q9-16)**
- JOIN operations
- Subqueries
- Aggregate functions
- Date/time operations

### **Advanced Level (Q17-25)**
- Window functions
- Common Table Expressions (CTEs)
- Complex analytical calculations
- Performance ranking systems
- Time-series analysis

All queries are available in the SQL Queries page with descriptions and examples.

---

## 💼 Business Use Cases

### **1. 📺 Sports Media & Broadcasting**
- Real-time match updates for commentary teams
- Player performance analysis for pre-match discussions
- Historical data trends for match predictions

### **2. 🎮 Fantasy Cricket Platforms**
- Player form analysis and recent performance tracking
- Head-to-head statistics for team selection
- Real-time score updates for fantasy leagues

### **3. 📈 Cricket Analytics Firms**
- Advanced statistical modeling and player evaluation
- Performance trend analysis across different formats
- Data-driven insights for team management

### **4. 🎓 Educational Institutions**
- Teaching database operations with real-world data
- SQL practice with engaging cricket datasets
- API integration and web development learning

### **5. 🎲 Sports Betting & Prediction**
- Historical performance analysis for odds calculation
- Player form and momentum tracking
- Venue-specific performance insights

---

## 🔧 Development

### **Project Guidelines**

- **Coding Standards**: Follow PEP 8 Python style guidelines
- **Error Handling**: Implement proper exception handling for API calls and database operations
- **Security**: Secure database credentials and API keys in `.env` file
- **Modularity**: Separate functions for different operations
- **Documentation**: Clear comments and docstrings for all functions
- **Version Control**: Use Git for code versioning and collaboration

### **Running Tests**

```bash
pytest tests/
```

### **Code Formatting**

```bash
black .
flake8 .
```

### **Database Migrations**

```bash
# Create new migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Name](https://linkedin.com/in/yourprofile)

---

## 🙏 Acknowledgments

- [Cricbuzz API](https://rapidapi.com/cricbuzz-official/api/cricbuzz-cricket) for providing cricket data
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [RapidAPI](https://rapidapi.com/) for API infrastructure

---

## 📞 Support

For support, email your.email@example.com or open an issue on GitHub.

---

## 🎯 Project Timeline

**Completion Time**: 14 days from assignment date

### **Week 1**
- Days 1-2: Setup, API integration, database design
- Days 3-4: Core page development (Home, Live Matches, Top Stats)
- Days 5-7: SQL queries implementation and CRUD operations

### **Week 2**
- Days 8-10: UI/UX improvements and visualizations
- Days 11-12: Testing, bug fixes, and documentation
- Days 13-14: Final review, recording demo video, submission

---

## 📚 Skills Demonstrated

`Python` • `SQL` • `Streamlit` • `JSON` • `REST API` • `Database Management` • `Data Analytics` • `Web Development` • `Sports Technology`

---

**Built with ❤️ using Clean Architecture and Object-Oriented Programming**