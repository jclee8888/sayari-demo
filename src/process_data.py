def extract_company_details(company_data):
# Key procurement logic

    if not company_data:
        print('Company data not recieved in extract_company_details')
        return None
    
    return {
        "label": company_data.label,
        "Sanctioned": company_data.sanctioned,
        "Countries": company_data.countries,
        "Addresses": company_data.addresses,
        "Risk Indicators": company_data.risk
    }

def is_company_sanctioned(company):
    # Checks for any sanctions in place
    return company.get("Sanctioned", False)

def is_us_based(company):
    # Geographic presence / locations. Sayari doesn't offer compliance cert data currently, so this is the next best thing. Assuming US aerospace companies do have certs (ITAR, DFARS, etc.).
    return "USA" in company.get("Countries", [])


def get_high_risk_factors(company):
    # Risk indicators. Starting point for internal investigations
    risk_factors = company.get("Risk Indicators", {})

    # return only risks with high priority risk factors
    high_risks = [
        key for key, risk in risk_factors.items() 
        if getattr(risk, "level", "").lower() in ["critical", "high"]
    ]
    
    #indirect sanctions flag. Companies may be owned by parent entities with sanctions
    indirect_sanctions = any(
        key in [
            "owned_by_sanctioned_entity",
            "owned_by_entity_in_export_controls",
            "linked_to_sanctioned_entity",
            "supplier_of_sanctioned_entity"
        ]
        for key in risk_factors
    )

    return high_risks, indirect_sanctions

def classify_company(company):
    # Qualifying candidate companies based off of returned data

    # result dictionary
    result = {
        "Company Name": company.get("label", "unknown"),
        "US Based": is_us_based(company),
        "Sanctioned": is_company_sanctioned(company),
        "Indirectly Sanctioned": False, 
        "Eligible": False,
        "High-Critical Risks": [],
        "Final Classification": ""
    }


    if not company:
        return "No Data"

    risks, indirect_sanctions = get_high_risk_factors(company)

    # store identified risks and indirect sanctions in results dictionary
    result["High-Critical Risks"] = risks
    result["Indirectly Sanctioned"] = indirect_sanctions


    # if the company has no US based offices, we're assuming they may not have the necessary certifications
    if not result["US Based"]:
        result["Final Classification"] = "Disqualified (Not U.S. Based)"
        return result

    # if companies are sanctioned, we disqualify them immediately
    if result["Sanctioned"]:
        result["Final Classification"] = "Disqualified (Sanctioned)"
        return result

    # if companies are indirectly sanctioned (owned by sanctioned parent entity), we also disqualify them
    if result["Indirectly Sanctioned"]:
        result["Final Classification"] = "Disqualified (Indirect Sanctions)"
        return result

    # else we set company to 'eligible' if:  1) it is US based; 2) not directly sanctioned; and 3) not indirectly sanctioned
    result["Eligible"] = True
    result["Final Classification"] = "Eligible"

    return result
