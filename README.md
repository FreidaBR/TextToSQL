# TextToSQL

### Multi-Agent Text-to-SQL Intelligent Assistant

SQLSense AI is a multi-agent system that enables users to query relational databases using natural language. Instead of manually writing SQL queries, users can ask questions in plain English, and the system generates, validates, executes SQL queries, and presents meaningful insights.

Developed as a Proof of Concept (POC) for the WinWire AI Internship, the project demonstrates agentic reasoning, schema understanding, SQL generation, validation, execution, and explainability.

---

# Problem Statement

Organizations store large amounts of structured data in relational databases, but retrieving information requires SQL knowledge. SQLSense AI bridges this gap by allowing users to interact with databases using natural language while providing transparency into every step of the query generation process.

---

# Features

- Natural Language to SQL conversion
- Automatic database schema understanding
- Multi-agent workflow
- SQL validation and safety checks
- Query execution on SQLite
- AI-generated business insights
- Explainable reasoning
- Interactive Streamlit interface

---

# System Architecture

```
                    User Query
                         │
                         ▼
                Intent Agent
      (Understands the user's request)
                         │
                         ▼
              Schema Reader
     (Reads database schema automatically)
                         │
                         ▼
            Schema Selector
 (Chooses only relevant tables and columns)
                         │
                         ▼
               SQL Generator
      (Generates optimized SQL query)
                         │
                         ▼
                SQL Critic
   (Validates and refines SQL query)
                         │
                         ▼
               SQL Executor
      (Executes query safely)
                         │
                         ▼
              Analyst Agent
 (Generates business insights and explanations)
```

---

# Multi-Agent Workflow

## Intent Agent
- Understands the user's natural language query.
- Extracts the goal, filters, grouping, sorting, and confidence score.

## Schema Reader
- Reads the SQLite database automatically.
- Extracts tables, columns, and relationships.

## Schema Selector
- Selects only the tables relevant to the user's request.
- Reduces unnecessary context sent to the language model.

## SQL Generator
- Converts the structured intent into a valid SQLite query.
- Uses only the selected schema for SQL generation.

## SQL Critic
- Validates generated SQL.
- Prevents unsafe queries.
- Corrects invalid SQL when required.

## SQL Executor
- Executes validated SQL.
- Returns results in a structured format.

## Analyst Agent
- Summarizes the query results.
- Generates business insights and recommendations.

---

# Technologies Used

- Python 3.11
- SQLite
- Streamlit
- Google Gemini API
- Pandas
- Faker
- python-dotenv

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
└── .env
```

---

# Example Queries

- Show the top 5 products by sales
- Which customers placed the highest number of orders?
- Show total revenue for each month
- List all products in the Electronics category
- Which city has the highest number of customers?

---

# Explainability

SQLSense AI provides transparency throughout the execution pipeline by displaying:

- Extracted user intent
- Selected database tables
- Generated SQL query
- Query results
- AI-generated business insights
- Agent workflow logs

This allows users to understand how the final answer was generated.

---

# Safety Measures

The system executes only read-only SQL queries and blocks potentially destructive SQL commands such as:

- DROP
- DELETE
- UPDATE
- INSERT
- ALTER
- TRUNCATE

---

# Challenges and Solutions

| Challenge | Solution |
|-----------|----------|
| Mapping natural language to SQL | Intent Agent extracts structured intent before SQL generation |
| Selecting relevant tables | Schema Selector identifies only the required tables |
| SQL validation | Critic Agent validates generated SQL before execution |
| Schema understanding | Automatic schema parsing using SQLite PRAGMA |
| Explainability | Displays intent, SQL, reasoning, logs, and insights |
| Safe execution | Restricts execution to read-only SQL queries |

---

# Future Improvements

- PostgreSQL and MySQL support
- Query history
- SQL optimization suggestions
- Retry mechanism for failed SQL generation
- Interactive data visualizations
- Role-based database access
- Support for complex nested SQL queries
- Query result caching for improved performance

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

---

# Screenshots
<img width="946" height="455" alt="image" src="https://github.com/user-attachments/assets/700cffcc-13d2-42c0-a78d-17af12340163" />


---

# Author

Freida Rodrigues

B.Tech Computer Science and Engineering

Developed as a Proof of Concept for the WinWire AI Internship.
