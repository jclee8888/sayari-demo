def extract_company_details(company_data):

    if not company_data:
        print('company data not recieved in extract_company_details')
        return None
    
    # print(f"company_data.label: {company_data.label}")
    # print(f"company_data.sanctioned: {company_data.sanctioned}")
    # print(f"company_data.countries: {company_data.countries}")
    # print(f"company_data.addresses: {company_data.addresses}")
    print(f"company_data.risk: {company_data.risk}")

    return {
        "label": company_data.label,
        "Sanctioned": company_data.sanctioned,
        "Countries": company_data.countries,
        "Addresses": company_data.addresses,
        "Risk Indicators": company_data.risk
    }


def is_company_sanctioned(company):
    # Checks for any sanctions in place
    return company.sanctioned("sanctioned", False)


def is_us_based(company):
    # Geographic presence / locations. Sayari doesn't offer compliance cert data currently, so this is the next best thing. Assuming US aerospace companies do have certs (ITAR, DFARS, etc.).
    return "USA" in company.countries


def get_high_risk_factors(company):
    # Risk indicators. Starting point for internal investigations
    risk_factors = company.risk_factors
    # return only risks with high priority risk factors
    high_risks = [key for key, risk in risk_factors.items() if risk.get("level") in ["high", "elevated"]]
    return high_risks


def classify_company(company):
    if not company:
        return "No Data"

    # disqualify if sanctioned
    if is_company_sanctioned:
        return "Disqualified"

    # verify company at least has an office in USA
    if is_us_based(company):
        return "Likely Eligible"

    # looks at the risk factors
    if get_high_risk_factors(company):
        return "Requires Further Review"


    return "Requires Further Review"
    
