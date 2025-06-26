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