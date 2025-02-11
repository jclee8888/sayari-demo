# to csV?

def format_risk_factors(risk_factors):

    if not risk_factors:
        return "None"
    
    formatted_risks = []
    for key, risk in risk_factors.items():
        level = risk.get("level", "Unknown")
        formatted_risks.append(f"   - {key.replace('_', ' ').title()}: {level}")
    
    return "\n".join(formatted_risks)