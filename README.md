# Medical Expert System: Forward and Backward Chaining

A beginner-friendly Flask mini project that demonstrates rule-based inference. The labels are illustrative patterns, not validated medical diagnoses.

## Requirements
- Python 3.10 or newer
- Internet only if Flask needs to be installed

## Run on Windows (PowerShell)

1. Extract this ZIP to a folder, for example `Desktop\medical_chaining_mini_project`.
2. Open PowerShell in that folder.
3. Create a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use this instead:

   ```powershell
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   .\.venv\Scripts\python.exe app.py
   ```

4. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Start the website:

   ```powershell
   python app.py
   ```

6. Open `http://127.0.0.1:5000` in your browser.
7. Select sample symptoms and press **Run inference engine**.

## What to demonstrate

- **Forward chaining:** Begins with selected symptoms (facts), checks every rule, and displays any rule whose required symptoms are all present.
- **Backward chaining:** Begins with one selected goal, checks the symptoms required by that rule, and shows which required symptoms are present or missing.
- The table shows a trace for each rule.

## Files
- `app.py` — Flask routes, sample rules, forward chaining and backward chaining functions
- `templates/index.html` — form and results page
- `static/style.css` — page styling
- `requirements.txt` — Python dependency

## Important safety limitation
This is a logic/inference demonstration for coursework only. The rules are invented for teaching and are not based on clinical guidelines, datasets, or medical validation. Do not use the output to diagnose, treat, or rule out any condition. For real symptoms, contact a qualified healthcare professional; seek urgent local care for severe or rapidly worsening symptoms.
