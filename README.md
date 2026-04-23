# 🌳 PyTree

An ultra-fast terminal utility that generates a visual tree structure of public functions within your Python projects.


## ✨ Features

- 🚀 **Turbo Performance**: Built with `awk` for near-instant processing, even in large-scale projects.
- ⚡ **Async Support**: Automatically detects and visually marks `async def` functions.
- 📂 **Tree Structure**: Displays functions grouped by file, excluding `__pycache__` and hidden directories.
- 📊 **Code Insights**: Shows the total Lines of Code (LOC) for each script.
- 🎨 **Rich Visuals**: Colored terminal output and seamless HTML report export.
- 🤖 **System Aware**: Displays the current OS environment and Python version in the header.

## 🚀 Installation

1. **Download the script:**
   ```bash
   curl -O https://githubusercontent.com
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

Simply run the command in your project folder:
```bash
pytree
```

To analyze a specific directory:
```bash
pytree ./src
```

### 📄 HTML Reports (`pyreport`)
To generate a professional-looking HTML report with colors preserved, use the `pyreport` function.

**Prerequisite:** Install `aha` (Ansi HTML Adapter).
- Linux: `sudo apt install aha`
- macOS: `brew install aha`

**Add this to your `.bashrc` or `.zshrc`:**
```bash
pyreport() {
    local filename="pytree_report_$(date +%Y%m%d_%H%M).html"
    pytree | aha --black > "$filename"
    echo "✅ Report generated: $filename"
}
```

## 📱 Termux Specifics (Android)

PyTree works perfectly on **Termux**. Since the file structure is different, follow these steps:

1. **Install dependencies:**
   ```bash
   pkg install coreutils grep sed findutils aha
   ```

2. **Install PyTree:**
   ```bash
   mv pytree $PREFIX/bin/
   chmod +x $PREFIX/bin/pytree
   ```

3. **Open reports on Android:**
   After generating a report with `pyreport`, you can open it in your mobile browser:
   ```bash
   termux-open pytree_report_*.html
   ```

## 📋 Example Output

```text
PyTree @ GNU/Linux | Python v3.11.5
------------------------------------------
📂 ./app/core.py [145 lines]
  ├── initialize_system()
  ├── run_worker() ⚡(async)

📂 ./utils/logger.py [30 lines]
  ├── log_event()
  ├── setup_colors()
```

## 📄 License
This project is licensed under the MIT License.
