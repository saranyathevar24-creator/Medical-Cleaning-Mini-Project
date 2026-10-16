from flask import Flask, render_template, request

app = Flask(__name__)

# Educational example rules only — not clinically validated.
# Each rule is a set of symptoms used to demonstrate inference.
RULES = {
    "Common cold pattern": {"runny_nose", "sneezing", "sore_throat"},
    "Flu-like pattern": {"fever", "body_aches", "fatigue", "headache"},
    "Allergy-like pattern": {"sneezing", "itchy_eyes", "runny_nose"},
    "Stomach-upset pattern": {"nausea", "vomiting", "stomach_pain"},
    "Respiratory-irritation pattern": {"cough", "sore_throat"},
}

SYMPTOMS = {
    "fever": "Fever",
    "cough": "Cough",
    "sore_throat": "Sore throat",
    "runny_nose": "Runny nose",
    "sneezing": "Sneezing",
    "body_aches": "Body aches",
    "fatigue": "Fatigue",
    "headache": "Headache",
    "itchy_eyes": "Itchy eyes",
    "nausea": "Nausea",
    "vomiting": "Vomiting",
    "stomach_pain": "Stomach pain",
}

def forward_chaining(facts):
    """Start with known symptoms and find rules whose conditions are met."""
    matched = []
    trace = []
    for conclusion, required in RULES.items():
        present = sorted(required & facts)
        missing = sorted(required - facts)
        if required.issubset(facts):
            matched.append(conclusion)
            trace.append({
                "rule": conclusion,
                "status": "Matched",
                "present": [SYMPTOMS[s] for s in present],
                "missing": []
            })
        else:
            trace.append({
                "rule": conclusion,
                "status": "Not matched",
                "present": [SYMPTOMS[s] for s in present],
                "missing": [SYMPTOMS[s] for s in missing]
            })
    return matched, trace

def backward_chaining(goal, facts):
    """Start with a target conclusion and check whether its required facts exist."""
    required = RULES.get(goal, set())
    present = sorted(required & facts)
    missing = sorted(required - facts)
    success = required.issubset(facts)
    return {
        "goal": goal,
        "success": success,
        "present": [SYMPTOMS[s] for s in present],
        "missing": [SYMPTOMS[s] for s in missing],
        "message": (
            f"The rule for '{goal}' is satisfied in this demonstration."
            if success else
            f"The rule for '{goal}' is not satisfied; some required symptoms were not selected."
        )
    }

@app.route("/", methods=["GET", "POST"])
def index():
    selected = set()
    forward_results = []
    trace = []
    backward_result = None
    goal = ""
    submitted = False

    if request.method == "POST":
        submitted = True
        selected = set(request.form.getlist("symptoms"))
        goal = request.form.get("goal", "")
        forward_results, trace = forward_chaining(selected)
        if goal in RULES:
            backward_result = backward_chaining(goal, selected)

    return render_template(
        "index.html",
        symptoms=SYMPTOMS,
        selected=selected,
        rules=RULES,
        forward_results=forward_results,
        trace=trace,
        backward_result=backward_result,
        goal=goal,
        submitted=submitted
    )

if __name__ == "__main__":
    app.run(debug=True)
