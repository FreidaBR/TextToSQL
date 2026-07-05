# TextToSQL Agent

## Multi-Agent Text-to-SQL Intelligent Assistant

SQLSense AI is a multi-agent Text-to-SQL system that enables users to interact with relational databases using natural language. Instead of manually writing SQL queries, users can simply ask questions in plain English, and the system intelligently generates, validates, executes, and explains SQL queries.

Developed as a **Proof of Concept (POC)** for the **WinWire AI Internship**, this project demonstrates how multiple AI agents can collaborate to perform intent extraction, schema understanding, SQL generation, validation, execution, automatic error recovery, and business insight generation.

---

# Problem Statement

Organizations store vast amounts of structured data inside relational databases. However, retrieving meaningful information often requires SQL expertise, making databases inaccessible to non-technical users.

SQLSense AI bridges this gap by allowing users to query databases using natural language while providing complete transparency into how every SQL query is generated, validated, executed, and explained through a multi-agent workflow.

---

# Features

- Natural Language to SQL conversion
- Multi-Agent Architecture
- Automatic Database Schema Understanding
- Intelligent Table Selection
- SQL Generation using Google Gemini
- SQL Validation and Safety Checks
- Automatic SQL Recovery and Retry Mechanism
- Query Execution on SQLite
- AI-generated Business Insights
- Explainable Agent Workflow
- Interactive Streamlit Interface

---

# System Architecture

```
                    User Query
                         │
                         ▼
                Intent Agent
      (Extracts user intent)
                         │
                         ▼
               Schema Reader
    (Reads database schema dynamically)
                         │
                         ▼
              Schema Selector
 (Selects only relevant tables and columns)
                         │
                         ▼
               SQL Generator
      (Generates SQL query)
                         │
                         ▼
                Critic Agent
   (Validates generated SQL)
                         │
                         ▼
                SQL Executor
                         │
          ┌──────────────┴──────────────┐
          │                             │
          │ Success                     │ Execution Error
          │                             │
          ▼                             ▼
     Analyst Agent              Recovery Agent
          │                      (Corrects SQL)
          │                             │
          └──────────────┬──────────────┘
                         ▼
                 Retry SQL Execution
                         │
                         ▼
                  Final Response
```

---

# Multi-Agent Workflow

## Intent Agent

- Understands the user's natural language query.
- Extracts structured intent including:
  - Goal
  - Metric
  - Filters
  - Sorting
  - Grouping
  - Confidence Score

---

## Schema Reader

- Reads the SQLite database dynamically.
- Identifies all available tables and columns.
- Eliminates the need for hardcoded schema definitions.

---

## Schema Selector

- Receives the extracted intent and complete database schema.
- Selects only the tables required to answer the user's question.
- Reduces unnecessary context sent to the language model.

---

## SQL Generator

- Generates SQL queries using Google Gemini.
- Supports:
  - JOIN
  - GROUP BY
  - ORDER BY
  - SUM()
  - COUNT()
  - AVG()
  - LIMIT
  - Filtering

---

## Critic Agent

- Validates generated SQL.
- Prevents execution of unsafe SQL commands.
- Ensures only read-only queries are executed.

Blocked Commands:

- DROP
- DELETE
- INSERT
- UPDATE
- ALTER
- TRUNCATE

---

## SQL Executor

- Executes validated SQL queries on the SQLite database.
- Returns structured query results.
- Detects SQL execution failures.

---

## Recovery Agent

- Detects SQL execution failures.
- Uses the execution error together with the database schema to refine the SQL query.
- Automatically retries execution once.
- Prevents infinite retry loops through controlled retry limits.

---

## Analyst Agent

- Summarizes query results.
- Generates business insights.
- Provides recommendations based on returned data.
- Handles failed executions gracefully.

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.11 | Backend Development |
| Streamlit | User Interface |
| SQLite | Relational Database |
| Google Gemini API | Natural Language Understanding & SQL Generation |
| Pandas | Data Processing |
| Faker | Sample Data Generation |
| python-dotenv | Environment Variable Management |
| Git | Version Control |
| GitHub | Source Code Management |

---

# Project Structure

```
TEXTTOSQL/

│
├── agents/
│   ├── intent_agent.py
│   ├── schema_selector.py
│   ├── sql_agent.py
│   ├── critic_agent.py
│   ├── recovery_agent.py
│   └── analyst_agent.py
│
├── database/
│   ├── create_database.py
│   ├── sample_data.py
│   └── ecommerce.db
│
├── utils/
│   ├── context.py
│   ├── db.py
│   ├── executor.py
│   ├── gemini.py
│   ├── parser.py
│   ├── schema_reader.py
│   └── validator.py
│
├── app.py
├── orchestrator.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

# Example Queries

- Show top 5 products by sales
- Which customers placed the highest number of orders?
- Show total revenue for each month
- List all products in the Electronics category
- Which city has the highest number of customers?
- Show the top spending customers

---

# Explainability

SQLSense AI provides complete transparency by displaying:

- User Intent
- Selected Database Tables
- Generated SQL Query
- Query Results
- AI-generated Business Analysis
- Agent Logs
- Recovery Process (if retry occurs)

Users can understand every stage of the decision-making process instead of receiving only the final answer.

---

# Agentic Reasoning

Unlike traditional Text-to-SQL systems that rely on a single AI prompt, SQLSense AI decomposes the task into multiple specialized agents.

Each agent performs a dedicated responsibility:

- Intent Understanding
- Schema Analysis
- Table Selection
- SQL Generation
- SQL Validation
- SQL Execution
- Error Recovery
- Business Analysis

This modular architecture improves transparency, maintainability, robustness, and explainability while demonstrating agentic AI reasoning.

---

# Safety Measures

The system executes only read-only SQL queries.

Potentially destructive SQL statements are automatically blocked, including:

- DROP
- DELETE
- UPDATE
- INSERT
- ALTER
- TRUNCATE

This ensures the integrity of the underlying database.

---

# Challenges and Solutions

| Challenge | Solution |
|-----------|----------|
| Mapping natural language to SQL | Intent Agent extracts structured intent before SQL generation |
| Dynamic schema understanding | Schema Reader automatically parses the SQLite database |
| Selecting relevant tables | Schema Selector identifies only the required tables |
| SQL generation | SQL Generator creates optimized SQL using Gemini |
| SQL validation | Critic Agent validates SQL before execution |
| SQL execution failures | Recovery Agent refines failed SQL and retries execution automatically |
| Explainability | Displays intent, SQL, reasoning, insights, and agent logs |
| Safe execution | Restricts execution to read-only SQL queries |

---

# Future Improvements

- PostgreSQL support
- MySQL support
- Interactive data visualizations
- Conversational multi-turn querying
- Query history
- Query caching
- Advanced SQL optimization
- Role-based database authentication
- Support for multiple retry strategies

---

# Installation

## Clone the repository

```bash
git clone https://github.com/FreidaBR/TextToSQL.git
```

## Navigate to the project

```bash
cd TextToSQL
```

## Create a virtual environment

```bash
python -m venv venv
```

## Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure the API key

Create a `.env` file.

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

# Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

---

# Sample Output

The application displays:

- Extracted Intent
- Selected Tables
- Generated SQL
- SQL Execution Results
- AI-generated Analysis
- Agent Logs
- Recovery Logs (if applicable)

---

# Screenshots
<img width="923" height="454" alt="image" src="https://github.com/user-attachments/assets/7ce4441d-e6fe-4d4f-8067-e35c395aa86d" />



---

# Author

**Freida B Rodrigues**

B.Tech Computer Science and Engineering

Developed as a **Proof of Concept (POC)** for the **WinWire AI Internship**.
