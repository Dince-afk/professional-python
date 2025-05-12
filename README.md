# Professional Python Project

## How to use

Install uv to manage dependencies and run the project

[uv installation](https://docs.astral.sh/uv/getting-started/installation)

Run the script

In production.

```bash
uv run main.py
```

During development.

````bash
PYTHON_ENV=development nodemon --exec uv run main.py```
````

or run bash script

```bash
./dev.sh
```
