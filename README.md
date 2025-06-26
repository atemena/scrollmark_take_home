# Social Media Comment Agentic Workflow

A lean Python app to analyze social media comments from CSV, extract topics of interest using LLMs, and generate engagement trend reports.

## Setup

1. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up OpenAI API key:**
   - Create a `.env` file in the project root with:
     ```
     OPENAI_API_KEY=sk-...
     ```

## Usage

1. Place your CSV file in the `data/` directory (see `data/example.csv` for format).
2. Run the app from the project root:
   ```bash
   python3 -m src.main --csv data/example.csv --db data/example.sqlite
   ```
   - By default, uses `data/example.csv` and creates/overwrites `data/example.sqlite`.

## Output
- Prints a table of topics, daily engagement, and comment counts.

## Troubleshooting
- **ModuleNotFoundError for `src`**: Always run with `python3 -m src.main ...` from the project root.
- **Missing API key**: Ensure `.env` exists and contains your `OPENAI_API_KEY`.
- **Deprecation warnings**: If you see warnings about `langchain.llms`, update imports to use `langchain_community.llms`.

## Testing

Run all tests:
```bash
pytest
``` 

## Executive Summary
This project analyzes @treehut's Instagram comments from March 2025, focusing on how different post types (Giveaway, Product Launch, Lifestyle, etc.) drive user engagement.

Using LLM-powered caption analysis, the workflow categorizes each post and summarizes how many engaged users (as defined by unique commenters) each post type attracted per day. The result is a modular, extensible workflow that surfaces actionable insights for social media managers, with robust data storage (SQLite), agentic LLM analysis, and clear, automatable reporting.

### Key Findings

- **Giveaway and Product Launch posts** generated the most engagement (over 6,000 comments each)
- **Lifestyle and Pregnancy Routine** post types drew less interaction
- The workflow and database design allow for fast extension and re-analysis as new agent workflows or evaluation metrics are developed
- The project provides a strong foundation for future features such as real-time reporting, deeper prompt tuning, and improved visualizations

### Visualizations
See [report.md](report.md)

## Extension Proposal

1. **Automated Evaluation Framework**
   - Implement LangSmith integration for LLM performance tracking
   - Set up automated prompt tuning and A/B testing
   - Add explainability metrics for post type classification accuracy

2. **Implement Visualizations**
   - Daily/weekly engagement trend charts
   - Interactive dashboards with filtering capabilities
   - Post type performance comparisons over time
   - User engagement heatmaps

3. **Self-Service Platform**
   - Web interface for report generation
   - User authentication and account management
   - Automated report scheduling and delivery
   - Custom branding options for different clients

## AI & Tool Usage
- **Python** - Core scripting and workflow automation
- **LangChain** - Agentic workflow orchestration, LLM analysis
- **OpenAI** - Brainstorming, caption/post-type classification, text understanding
- **Cursor** - AI pair-programming and code refactoring
- **Sqlite3** - Lightweight, portable database for fast development
- **Tabular** - Data manipulation
- **ChatGPT** - Project brainstorming, plan review, and documentation drafting

## Contributing & Extending

### Adding New Agents

The project uses a modular agent architecture. To add a new analysis agent:

1. **Create agent function** in `src/agents.py`:

### Modifying or Extending Reports

To modify or extend reports:

1. **Update report generation logic** in `src/report.py`:
   ```python
   def generate_report(metrics_df, output_file="report.md"):
       # Add new analysis sections
       # Modify existing aggregations
       # Include new visualizations
   ```

2. **Add new metrics** to `src/agents.py`:
   ```python
   def aggregate_post_type_metrics(df, llm=None):
       # Add new aggregation columns
       # Include additional grouping logic
       # Return enhanced metrics dataframe
   ```

3. **Extend data processing** in `src/main.py`:
   ```python
   # Add new data transformations
   # Include additional filtering logic
   # Modify output format
   ```

4. **Update tests** in `tests/test_report.py`:
   ```python
   # Test new report sections
   # Validate new metrics calculations
   # Ensure backward compatibility
   ```

### Adding New Report Types

Create new report templates by:
- Adding new functions in `src/report.py`
- Updating `main.py` to call new report generators
- Creating corresponding test files
- Documenting new report formats in this README



