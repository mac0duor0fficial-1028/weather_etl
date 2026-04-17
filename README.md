# 🌤️ Weather ETL Pipeline

> A modular Python ETL pipeline that extracts real-time weather data from the **Tomorrow.io API**, transforms it into clean structured records, and loads it into a **PostgreSQL** database for analysis and storage.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Pipeline Stages](#pipeline-stages)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The **Weather ETL Pipeline** automates the collection and persistence of weather data in three clean stages:

| Stage               | Description                                                           |
| ------------------- | --------------------------------------------------------------------- |
| **Extract**   | Pulls hourly weather data from the Tomorrow.io REST API               |
| **Transform** | Structures and cleans the raw JSON into typed, analysis-ready records |
| **Load**      | Inserts the transformed records into a PostgreSQL database            |

The pipeline is designed to be **lightweight**, **modular**, and easy to extend — making it straightforward to add new data sources, transformation rules, or destination targets.

---

## Architecture

Data moves through four stages in a single linear flow:

```
Tomorrow.io API  ──(hourly JSON)──►  Extract  ──(raw data)──►  Transform  ──(typed records)──►  Load  ──(SQL insert)──►  PostgreSQL
```

| Stage               | Module                               | Responsibility                                                                |
| ------------------- | ------------------------------------ | ----------------------------------------------------------------------------- |
| **Extract**   | `etl_mod/extract_weather_mod.py`   | Calls the Tomorrow.io REST API and returns the raw hourly JSON payload        |
| **Transform** | `etl_mod/transform_weather_mod.py` | Parses the raw response, casts types, drops nulls, and produces clean records |
| **Load**      | `etl_mod/load_weather_mod.py`      | Connects to PostgreSQL and inserts each transformed record                    |

The three stages are orchestrated by `weather_pipeline_mod.py`, which handles errors at each boundary and exits gracefully if a stage returns no data.

---

## Project Structure

```
weather_etl/
├── etl_mod/
│   ├── extract_weather_mod.py   # Calls Tomorrow.io API & returns raw data
│   ├── transform_weather_mod.py # Cleans & structures the raw response
│   └── load_weather_mod.py      # Loads transformed data into PostgreSQL
├── config.py                    # API keys, DB credentials & settings
├── requirements.txt             # Python dependencies
├── weather_pipeline_mod.py      # Orchestrates the E→T→L stages
├── weather_pipeline_run.py      # Entry point to run the pipeline
├── .gitignore
└── README.md
```

---

## Prerequisites

- Python **3.8+**
- A **Tomorrow.io** account with an active API key — [sign up here](https://www.tomorrow.io/)
- A running **PostgreSQL** instance (local or cloud)

---

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/mac0duor0fficial-1028/weather_etl.git
cd weather_etl
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Configuration

Open `config.py` and fill in your credentials:

```python
# Tomorrow.io API
API_KEY = "your_tomorrow_io_api_key"
LOCATION  = "nairobi"               # City name or lat/lon coordinates

# PostgreSQL connection
DB_HOST     = "localhost"
DB_PORT     = 5432
DB_NAME     = "weather_db"
DB_USER     = "your_db_user"
DB_PASSWORD = "your_db_password"
```

> ⚠️ **Never commit real credentials to version control.** Consider loading secrets from environment variables or a `.env` file (with `python-dotenv`) and adding `config.py` to `.gitignore`.

---

## Usage

Run the full ETL pipeline with a single command:

```bash
python weather_pipeline_run.py
```

**Sample output:**

```
Weather ETL pipeline completed successfully
```

If something goes wrong, the pipeline prints a descriptive error message:

```
No data extracted — check API key or network connection
```

---

## Pipeline Stages

### 🔵 Extract — `etl_mod/extract_weather_mod.py`

Sends a request to the Tomorrow.io API and returns the raw **hourly weather** data payload. If the response is empty or the request fails, the pipeline exits gracefully with a warning.

### 🟡 Transform — `etl_mod/transform_weather_mod.py`

Receives the raw hourly data and converts it into structured Python records, handling:

- Field renaming & type casting
- Removal of nulls / incomplete records
- Any unit conversions needed for downstream use

### 🟢 Load — `etl_mod/load_weather_mod.py`

Connects to PostgreSQL and inserts each transformed record into the target table. Uses error handling to catch database connectivity issues before they bubble up.

---

## Tech Stack

| Tool                      | Role                        |
| ------------------------- | --------------------------- |
| **Python 3**        | Core language               |
| **Tomorrow.io API** | Weather data source         |
| **PostgreSQL**      | Data storage                |
| **psycopg2**        | Python ↔ PostgreSQL driver |
| **requests**        | HTTP client for API calls   |

---

## Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

Please make sure your code follows existing style conventions and includes docstrings for any new functions.

---

## License

This project is open source. Feel free to use, modify, and distribute it.

---

<p align="center"><a href="https://github.com/mac0duor0fficial-1028/weather_etl">github.com/mac0duor0fficial-1028/weather_etl</a></p>
