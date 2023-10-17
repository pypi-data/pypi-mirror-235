"""Functions for getting Sales Tax Data"""
import requests
from bs4 import BeautifulSoup


def post_request(url, payload):
    """Post Request"""
    try:
        r = requests.post(url, data=payload, timeout=30)
        if r.status_code == 200:
            return r
        else:
            print(r.status_code)
    except Exception as e:
        print(e)


class Arkansas:
    """Arkansas Tax Rate Functions"""

    def get(street: str, city: str, zip_code: str):  # pylint: disable=no-self-argument
        """Get Arkansas Tax Rates get(street: str, city: str, zip: str)"""
        form_payload = {
            "Street": street,
            "City": city,
            "State": "AR",
            "State2": "AR",
            "ZIP": zip_code,
        }
        form_url = "https://gis.arkansas.gov/Lookup/Results.php"
        response = post_request(form_url, form_payload)
        soup = BeautifulSoup(response.text, "html.parser")
        taxable_state = soup.find(id="TableCell20").text
        state_tax_rate = soup.find(id="tblCStateRate").text
        taxable_county = soup.find(id="tblCOutCoName").text
        county_tax_rate = soup.find(id="tblCOutCoRate").text
        taxable_city = soup.find(id="tblCOutCiName").text
        city_tax_rate = soup.find(id="tblCOutCiRate").text
        tax_rate_data = {
            "taxable_state": taxable_state,
            "state_tax_rate": state_tax_rate,
            "is_state_taxable": state_tax_rate != "",
            "taxable_county": taxable_county,
            "county_tax_rate": county_tax_rate,
            "is_county_taxable": county_tax_rate != "",
            "taxable_city": taxable_city,
            "city_tax_rate": city_tax_rate,
            "is_city_taxable": city_tax_rate != "",
        }
        return tax_rate_data
