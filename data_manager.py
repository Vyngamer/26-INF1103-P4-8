import json
from datetime import datetime

def load(filename):
    try:
        with open(filename,"r") as file:
            records = json.load(file)
    except json.JSONDecodeError:
        records = []
    return records
    
def save(record, filename):
    records = load(filename)

    if records:
        record["record_id"] = records[-1]["record_id"] + 1
    
    else: 
        record["record_id"] = 1001

    record["timestamp"] = datetime.now().isoformat()

    records.append(record)

    with open(filename, "w") as file:
        json.dump(records, file, indent=4)

    return print(f"Records has been saved in {filename}")


# Main Function

filename = "records.json"
load(filename)

#Testing

user_input = {
    "sleep_duration": 5,
    "stress_level": 8,
    "focus_level": 2,
    "academic_workload": 9,
    "mood": "Exhausted",
    "social_activity_level": 3,
    "reflection": "I have many assignments due."
    }

ai_output = {
    "mental_wellness_risk_score": 78,
    "sentiment": "Negative",
    "burnout_risk_score": 82,
    "crisis_alert": False,
    "primary_stressor": "Assignment deadlines",
    "personalized_recommendations": "Prioritise sleep and manage deadlines."
    }

logic_output = {
    "mental_wellness_risk_tier": "High",
    "warnings": ["High Burnout Warning"],
    "counselling_recommendation": True
    }

record = {
    "user_input": user_input,
    "ai_output": ai_output,
    "logic_output": logic_output
    }

save(record, filename)