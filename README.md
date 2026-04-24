# 🌳 PyTree

A powerful Python utility that analyzes and visualizes the structure of your Python projects, showing public functions, their locations, sizes, and external call dependencies.

## ✨ Features

- 🔍 **AST-Based Analysis**: Uses Python's Abstract Syntax Tree for accurate function extraction and call graph analysis
- ⚡ **Async Support**: Automatically detects and marks `async def` functions
- 📂 **Smart Filtering**: Excludes `__pycache__`, `.git`, `.venv`, and `node_modules` directories; filters out private functions (those starting with `_`)
- 📊 **Call Graph Analysis**: Tracks external function calls across files, showing where each function is used
- 🎨 **Multiple Output Formats**: Terminal output, JSON, CSV, and HTML reports
- 💾 **Detailed Metrics**: Displays Lines of Code (LOC) for each function and file
- 🤖 **System Aware**: Shows the current OS and Python version in the header
- 🔄 **Reverse Analysis**: Identify unused functions or see which files call each function

## 🚀 Installation

1. **Download the script:**
   ```bash
   curl -O https://raw.githubusercontent.com/Troptrap/PyTree/refs/heads/main/pytree
   ```

2. **Make it executable:**
   ```bash
   chmod +x pytree
   ```

3. **Move it to your local bin (to run it from anywhere):**
   ```bash
   sudo mv pytree /usr/local/bin/
   ```

## 🛠️ Usage

### Basic Usage

Analyze the current directory:
```bash
pytree
```

Analyze a specific directory:
```bash
pytree ./src
```

Or using the `-d` flag:
```bash
pytree -d ./src
```

### 🔄 Reverse Analysis

See which functions are unused or track all external calls to each function:
```bash
pytree --reverse
```

Or:
```bash
pytree -r
```

**Output highlights:**
- Functions with ✘ and `UNUSED` are never called by other files
- Functions with call counts show exactly how many external files call them

### 📤 Export Reports

Export analysis to various formats:

```bash
# Export as JSON (default)
pytree --export json

# Export as CSV
pytree --export csv

# Export as HTML
pytree --export html

# Export with custom filename
pytree --export my_analysis.json
pytree --export project_report.html
```

Supported formats:
- **JSON**: Full data including call details (best for programmatic use)
- **CSV**: Tabular format for spreadsheet analysis
- **HTML**: Beautiful formatted report for sharing (GitHub-friendly dark theme)

## 📋 Example Output

### Terminal (Default Mode)
```
PyTree Engine @ Linux | Python v3.11.5
--------------------------------------------------
📂 ./app/core.py [145 lines]
  ├── initialize_system() (42 loc)
  ├── run_worker() ⚡(async) (38 loc)

📂 ./utils/logger.py [30 lines]
  ├── log_event() (8 loc)
  ├── setup_colors() (12 loc)
```

### Terminal (Reverse Mode)
```
PyTree Engine @ Linux | Python v3.11.5
--------------------------------------------------
📂 ./app/core.py [145 lines]
  ├── initialize_system() -> 3 calls:
  │   └── ./main.py:24
  │   └── ./app/worker.py:45
  │   └── ./utils/bootstrap.py:12
  ├── run_worker() -> ✘ UNUSED

📂 ./utils/logger.py [30 lines]
  ├── log_event() -> 7 calls:
  │   └── ./app/core.py:89
```

## 📄 License
This project is licensed under the MIT License.
