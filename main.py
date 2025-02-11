from src.fetch_data import fetch_company_profile
from src.process_data import ( 
    extract_company_details,
    classify_company
)


def main():
    # List of companies that respond to RFI. In next iterations, this list could come from csv upload, etc.
    # companies = ["Aerotech Solutions", "Orbital Materials", "Global Aerotech", "Sepehr Energy"]
    companies = ["Aerotech Solutions", "Sepehr Energy"]

    # Loop through list of companies

    for company in companies:
        print(f"Fetching company details for: {company}...")

        company_data = fetch_company_profile(company)
        company_details = extract_company_details(company_data)
        company_classification = classify_company(company_details)


if __name__ == "__main__":
    main()
