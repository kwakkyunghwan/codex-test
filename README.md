# codex-test

This repository hosts a simple stock condition scanner example. The project
structure is located in the `condition-scanner` directory:

```
condition-scanner/
├── backend/
│   ├── app.py
│   ├── conditions.json
│   └── filter.py
├── frontend/
│   ├── index.html
│   └── style.css
└── data/
    └── stocks.json
```

Run `python condition-scanner/backend/app.py` to start a small Flask server
that filters the sample stock data.
