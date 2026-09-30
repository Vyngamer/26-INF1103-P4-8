def decide_route(ai_result, tier, warnings):
    """Choose one actionable outcome from the AI assessment and warnings."""
    if ai_result["crisis_alert"]:
        return "Urgent support"

    # This rule combines three distinct AI output fields.
    combined_risk = (
        ai_result["mental_wellness_risk_score"] >= 60
        and ai_result["burnout_risk_score"] >= 70
        and ai_result["sentiment_analysis"] == "Negative"
    )

    if tier == "High" or len(warnings) >= 2 or combined_risk:
        return "Counsellor follow-up"

    return "Self-care guidance"


def assess(record, ai_result):
    """Return the outcome derived from the validated AI fields and input."""
    tier = get_risk_tier(ai_result["mental_wellness_risk_score"])

    warnings = get_warnings(
        ai_result["sentiment_analysis"],
        ai_result["burnout_risk_score"],
        record["sleep"],
        record["workload"],
        record["social"],
        record["focus"],
    )

    route = decide_route(ai_result, tier, warnings)

    return {
        "risk_tier": tier,
        "warnings": warnings,
        "route": route,
        "needs_counselling": route in ("Urgent support", "Counsellor follow-up"),
    }