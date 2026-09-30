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