# Python CLI Scraper

A simple command-line scraper built with Python.

It fetches posts from the JSONPlaceholder API, parses them, and outputs data in JSON or text format.

## Features

- Fetch posts from API
- Parse only `id` and `title`
- Output in JSON
- Output in text
- Save output to file
- Tested with pytest

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run default JSON output:

```bash
python main.py
```

Run text output:

```bash
python main.py --format text
```

Save JSON output:

```bash
python main.py --save output.json
```

Save text output:

```bash
python main.py --format text --save output.txt
```

Run tests:

```bash
pytest
```