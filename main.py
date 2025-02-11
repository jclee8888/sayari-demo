from src.fetch_data import fetch_company_profile
from src.process_data import ( 
    extract_company_details,
    classify_company
)


def main():
    # List of companies that respond to RFI. In next iterations, this list could come from csv upload, etc.
    # companies = ["Aerotech Solutions", "Orbital Materials", "Global Aerotech"]
    company = "Aerotech Solutions Inc."
    print(f"Fetching company details for: {company}...")

    # Loop through list of companies
        # for each
            # print name, relevant information, 
            # print sanctions, compliance risk. If sanctioned, disqualify
            # print geographic presence / business locations. (US based companies preferred as Sayari can't give me compliance data like ITAR / ISO)
            # print risk indicators
    company_data = fetch_company_profile(company)
    company_details = extract_company_details(company_data)
    company_classification = classify_company(company_details)


if __name__ == "__main__":
    main()




