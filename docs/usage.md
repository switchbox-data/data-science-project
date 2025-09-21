# Usage

Generate a project non-interactively with `--data` flags:

```bash
copier copy --defaults --force \
  --data author="Your Name" \
  --data email="you@example.com" \
  --data author_github_handle="your-gh" \
  --data project_name="awesome" \
  --data project_slug="awesome" \
  --data project_description="Awesome project" \
  --data python_data_science="y" --data python_package="y" \
  . /path/to/awesome
```

Or let Copier prompt you:

```bash
copier copy . /path/to/awesome
```
