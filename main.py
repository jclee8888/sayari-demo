from src.fetch_data import fetch_company_profile
from src.process_data import ( 
    extract_company_details,
    classify_company
)
from src.generate_report import display_report


def main():
    # List of companies that respond to RFI. In next iterations, this list could be ingested through .csv upload, etc.
    companies = ["Aerotech Solutions", "Orbital Materials", "Global Aerotech", "Sepehr Energy", "Textron Inc"]
    
    # initialize processed companies list
    processed_companies = []

    # Loop through list of companies
    for company in companies:
        company_data = fetch_company_profile(company)

        if not company_data:
            continue 

        company_details = extract_company_details(company_data)
        if not company_details:
            continue
        
        company_classification = classify_company(company_details)
        processed_companies.append(company_classification)

    display_report(processed_companies)



if __name__ == "__main__":
    main()
