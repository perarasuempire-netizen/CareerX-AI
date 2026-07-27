companies = [

    {
        "name": "Zoho",
        "location": "Chennai, Tamil Nadu",
        "roles": ["Software Developer","Backend Developer","AI Engineer"],
        "website": "https://www.zoho.com"
    },

    {
        "name": "Tata Consultancy Services (TCS)",
        "location": "Chennai / Bengaluru",
        "roles": ["Software Developer","Data Analyst","Cloud Engineer"],
        "website": "https://www.tcs.com"
    },

    {
        "name": "Infosys",
        "location": "Bengaluru",
        "roles": ["Software Developer","AI Engineer","Consultant"],
        "website": "https://www.infosys.com"
    },

    {
        "name": "Wipro",
        "location": "Bengaluru",
        "roles": ["Software Developer","Cloud Engineer"],
        "website": "https://www.wipro.com"
    },

    {
        "name": "HCLTech",
        "location": "Chennai / Bengaluru",
        "roles": ["Software Developer","Cloud Engineer"],
        "website": "https://www.hcltech.com"
    },

    {
        "name": "Cognizant",
        "location": "Chennai",
        "roles": ["Software Developer","Data Engineer"],
        "website": "https://www.cognizant.com"
    },

    {
        "name": "Accenture",
        "location": "Bengaluru / Chennai",
        "roles": ["AI Engineer","Cloud Engineer","Developer"],
        "website": "https://www.accenture.com"
    },

    {
        "name": "Capgemini",
        "location": "Bengaluru / Chennai",
        "roles": ["Software Developer","Data Analyst"],
        "website": "https://www.capgemini.com"
    },

    {
        "name": "IBM",
        "location": "Bengaluru",
        "roles": ["AI Engineer","Data Scientist"],
        "website": "https://www.ibm.com"
    },

    {
        "name": "Microsoft",
        "location": "Bengaluru",
        "roles": ["AI Engineer","Cloud Engineer"],
        "website": "https://www.microsoft.com"
    },

    {
        "name": "Google",
        "location": "Bengaluru",
        "roles": ["AI Engineer","Software Developer"],
        "website": "https://www.google.com"
    },

    {
        "name": "Amazon",
        "location": "Bengaluru",
        "roles": ["Software Developer","Data Scientist"],
        "website": "https://www.amazon.jobs"
    },

    {
        "name": "NVIDIA",
        "location": "Bengaluru",
        "roles": ["AI Engineer","Machine Learning Engineer"],
        "website": "https://www.nvidia.com"
    },

    {
        "name": "Cisco",
        "location": "Bengaluru",
        "roles": ["Network Engineer","Cloud Engineer"],
        "website": "https://www.cisco.com"
    },

    {
        "name": "SAP Labs",
        "location": "Bengaluru",
        "roles": ["Software Developer","Data Engineer"],
        "website": "https://www.sap.com"
    },

    {
        "name": "Oracle",
        "location": "Bengaluru",
        "roles": ["Database Engineer","Cloud Engineer"],
        "website": "https://www.oracle.com"
    },

    {
        "name": "Dell Technologies",
        "location": "Bengaluru",
        "roles": ["Software Developer","Cloud Engineer"],
        "website": "https://www.dell.com"
    },

    {
        "name": "Intel",
        "location": "Bengaluru",
        "roles": ["AI Engineer","Software Engineer"],
        "website": "https://www.intel.com"
    },

    {
        "name": "Samsung R&D Institute",
        "location": "Bengaluru",
        "roles": ["AI Engineer","Software Developer"],
        "website": "https://research.samsung.com"
    },

    {
        "name": "PayPal",
        "location": "Chennai",
        "roles": ["Backend Developer","Software Developer"],
        "website": "https://www.paypal.com"
    },

    {
        "name": "Freshworks",
        "location": "Chennai",
        "roles": ["Software Developer","AI Engineer"],
        "website": "https://www.freshworks.com"
    },

    {
        "name": "Chargebee",
        "location": "Chennai",
        "roles": ["Backend Developer","Software Developer"],
        "website": "https://www.chargebee.com"
    },

    {
        "name": "Mindtree",
        "location": "Chennai/Bengaluru",
        "roles": ["Developer","Cloud Engineer"],
        "website": "https://www.ltimindtree.com"
    },

    {
        "name": "LTIMindtree",
        "location": "Bengaluru",
        "roles": ["Software Developer","Data Engineer"],
        "website": "https://www.ltimindtree.com"
    },

    {
        "name": "Tech Mahindra",
        "location": "Chennai/Bengaluru",
        "roles": ["Software Developer","Network Engineer"],
        "website": "https://www.techmahindra.com"
    }

]


def recommend_companies(skills, career):

    result = []

    career_keywords = career.lower().split()


    for company in companies:

        for role in company["roles"]:

            role_text = role.lower()


            # Flexible matching
            if any(
                keyword in role_text
                for keyword in career_keywords
            ):

                result.append(company)
                break



    # If no match, return top companies
    if len(result) == 0:

        result = companies[:10]


    return result[:10]