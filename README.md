# myproject

A basic Python project.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

## Usage

```bash
myproject            # Hello, world!
myproject Ada        # Hello, Ada!
python -m myproject --version
```

## Development

```bash
pytest               # run tests
ruff check .         # lint
ruff format .        # format
```

## Layout

```
myproject/
├── pyproject.toml       # metadata, dependencies, tool config
├── README.md
├── .gitignore
├── src/myproject/
│   ├── __init__.py      # package code
│   └── __main__.py      # CLI entry point
└── tests/
    └── test_basic.py
```
