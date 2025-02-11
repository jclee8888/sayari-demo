def extract_company_details(company_data):

# Key procurement logic

    if not company_data:
        print('Company data not recieved in extract_company_details')
        return None
    
    # print(f"company_data.label: {company_data.label}")
    # print(f"company_data.sanctioned: {company_data.sanctioned}")
    # print(f"company_data.countries: {company_data.countries}")
    # print(f"company_data.addresses: {company_data.addresses}")

    # print(f"company_data.risk: {company_data.risk}")

    return {
        "label": company_data.label,
        "Sanctioned": company_data.sanctioned,
        "Countries": company_data.countries,
        "Addresses": company_data.addresses,
        "Risk Indicators": company_data.risk
    }

def is_company_sanctioned(company):
    # Checks for any sanctions in place
    print(f"Sanctioned status: {company.get('Sanctioned', False)}")
    return company.get("Sanctioned", False)

def is_us_based(company):
    # Geographic presence / locations. Sayari doesn't offer compliance cert data currently, so this is the next best thing. Assuming US aerospace companies do have certs (ITAR, DFARS, etc.).
    # print("is_us_based")
    return "USA" in company.get("Countries", [])


def get_high_risk_factors(company):
    # Risk indicators. Starting point for internal investigations
    # print("get risk factors")
    risk_factors = company.get("Risk Indicators", {})

    # return only risks with high priority risk factors
    high_risks = [key for key, risk in risk_factors.items() if getattr(risk, "level", "").lower() in ["critical", "high"]]
    
    #indirect sanctions flag. Companies may be owned by parent entities with sanctions
    indirect_sanctions = any(key in ["owned_by_sanctioned_entity", "owned_by_entity_in_export_controls"] for key in high_risks)

    print(f"high_risks: {high_risks}")
    print(f"Indirect sanctions detected: {indirect_sanctions}")
    return high_risks, indirect_sanctions

def classify_company(company):
    # Qualifying candidate companies based off of returned data
    
    # result dictionary
    result = {
        "US Based": is_us_based(company),
        "Sanctioned": is_company_sanctioned(company),
        "Indirectly Sanctioned": False,  # Will check this later
        "Eligible": False,
        "High-Critical Risks": [],
        "Final Classification": ""
    }

    if not company:
        return "No Data"

    # if the company has no US based offices, we're assuming they may not have the necessary certifications
    if not result["US Based"]:
        result["Final Classification"] = "Disqualified (Not U.S. Based)"
        return result

    # if companies are sanctioned, we disqualify them immediately
    if result["Sanctioned"]:
        result["Final Classification"] = "Disqualified (Sanctioned)"
        return result

    risks, indirect_sanctions = get_high_risk_factors(company)
    # storing risks, indirect sanctions to results
    result["High-Critical Risks"] = risks
    result["Indirectly Sanctioned"] = indirect_sanctions

    # if companies are indirectly sanctioned (owned by sanctioned parent entity), we also disqualify them
    if result["Indirectly Sanctioned"]:
        result["Final Classification"] = "Disqualified (Indirect Sanctions)"
        return result

    result["Eligible"] = True
    result["Final Classification"] = "Eligible"
    return result
