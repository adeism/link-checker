# 🔗 LinkChecker

> 🚀 A powerful Python script to verify and automatically update your download links.

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/downloads/)
[![Requests](https://img.shields.io/badge/Requests-Latest-green.svg)](https://docs.python-requests.org/en/latest/)


## ✨ Features

- 🔍 Smart URL validation and verification
- 🔄 Automatic search for newer versions of dead links
- 📝 Detailed reporting of active and dead links
- 💡 Intelligent pattern matching for version updates
- ⚡ Fast parallel processing with timeouts
- 🛡️ Robust error handling
- 📋 Preserves file comments and formatting

## 🚀 Quick Start

### Prerequisites

- 🐍 Python 3.x
- 📦 requests library

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/linkchecker.git
cd linkchecker
```

2. Install dependencies:
```bash
pip install requests
```

## 📖 Usage

1. Create your `link.txt` file:
```txt
# Your Download Links
apache=https://example.com/apache-2.4.zip
php=https://example.com/php-7.4.zip
```

2. Run the script:
```bash
python linkchecker.py
```

## 📄 File Structure

### Input Format (`link.txt`)
```txt
# Comments start with #
package-name=download-url

# Example:
mysql=https://example.com/mysql-8.0.zip
```

### Output Files

📁 The script generates two files:

1. `active_links_with_updates.conf`
   - ✅ Contains all working links
   - 🆕 Includes any found updates

2. `dead_links_report_with_updates.txt`
   - ❌ Lists all dead links
   - 📝 Includes error details
   - 🔍 Shows attempted fixes

## 🛠️ How It Works

1. 📖 **File Reading**
   - Parses `link.txt` line by line
   - Preserves comments and formatting

2. 🔍 **Link Verification**
   - Checks URL accessibility
   - Follows redirects
   - Handles timeouts

3. 🔄 **Update Process**
   - Detects dead links
   - Searches for newer versions
   - Updates links automatically

4. 📝 **Reporting**
   - Generates comprehensive reports
   - Details success and failures
   - Provides error explanations

## ⚠️ Error Handling

The script handles multiple scenarios:
- 🚫 Invalid URL formats
- 📡 Network connection issues
- ⏱️ Request timeouts (10s)
- 🔒 HTTP error responses
- 📝 Malformed input lines

