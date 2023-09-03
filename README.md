# Code Analyzer

This program analyzes Python code files to provide statistics on various aspects of the code, including the total lines, actual lines of code, excluded lines, lines with hash comments, lines with triple quotes comments, and empty lines.

## Prerequisites

Before using this program, make sure you have the following:

- Python 3 installed on your system.

- Required liblaries installed.

## Setup

1. Clone the repository to your local machine or download the source code.

   ```shell
   git clone https://github.com/Weyaxi/code-analyzer/
   ```

2. Navigate to the appropriate directory by executing the following command:

   ```shell
   cd code-analyzer
   ```

3. Install the required dependencies by running the following command:

   ```shell
   pip3 install -r requirements.txt
   ```

## Usage

You can use this program to analyze a Python code file by running the following command:

```shell
python3 main.py --path <path_to_file>
```

Replace `<path_to_file>` with the path to the Python code file you want to analyze.

The program will provide statistics on the code's structure, including total lines, actual lines of code, excluded lines, lines with hash comments, lines with triple quotes comments, and empty lines.

## Code Analysis
The program analyzes the code file and provides the following information:

- Total lines of your code.
- Actual lines of your code (excluding excluded lines).
- Number of lines excluded from your code.
- Number of lines with hash (#) comments.
- Number of lines with triple quotes (""") comments.
- Number of empty lines in your code.
