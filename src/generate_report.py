from src.process_data import classify_company


def display_report(companies):
    # Prints report of aggregated data in console
    
    print("\n" + "="*40)
    print(f"{'Company Name':<30} | {'US Based':<10} | {'Sanctioned':<12} | {'Indirectly Sanctioned':<22} | {'Eligible':<10} | {'High-Critical Risks'}")
    print("="*40)

    # loop through and classify each company
    for company in companies:
        result = classify_company(company)

        # print the values in the company dictionary
            # ternary to set '✅' or '❌' depending on the values
            # formatted table rows for width

        print(f"{company.get('Company Name', 'Unknown'):<25} | "
              f"{'✅' if company.get('US Based', False) else '❌':<10} | " 
              f"{'✅' if company.get('Sanctioned', False) else '❌':<12} | " 
              f"{'✅' if company.get('Indirectly Sanctioned', False) else '❌':<22} | "
              f"{'✅' if company.get('ELigible', False) else '❌':<10} | "
              f"{', '.join(company.get('High-Critical Risks', [])) if company.get('High-Critical Risks') else 'None'}")

    print("="*40)