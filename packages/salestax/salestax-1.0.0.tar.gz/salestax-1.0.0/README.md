# salestax-python
Python module for gathering sales tax rates
Currently only supports Arkansas. Feel free to submit a pull request to help add other states.

```
from salestax import Arkansas as ar

ar.get("700 W Walnut St", "Rogers", "72756")

{'taxable_state': 'Arkansas', 'state_tax_rate': '6.5%', 'is_state_taxable': True, 'taxable_county': 'Benton', 'county_tax_rate': '1%', 'is_county_taxable': True, 'taxable_city': 'Rogers', 'city_tax_rate': '2%', 'is_city_taxable': True}
```