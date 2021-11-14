# CSS503_Supra_Team_9

The vision of our team is, first of all, to collect high-quality data on electronic and household appliances for the daily use of people. We also hope that our little research can help people in some way. In the process of collecting data, we used not only local Kazakhstani sites, but also used foreign sites to provide an alternative to the analytics of the collected data.
Here is a list of sites we used:
* www.mechta.kz
* www.sanmi.kz
* www.evrika.com
* www.bestbuy.com

We collected data from different categories(TVs, Smartphones, Laptops, Cleaners, Fridges).
During the collection of data we used the following libraries:
```python
import requests
from bs4 import BeautifulSoup
import csv
``` 

Here is some examples how our dataset looks like.
Dataset of smartphones:

![alt text](https://github.com/adilbekishev/CSS503_Supra_Team_9/blob/main/phones.PNG)

Dataset of refrigerators:

![alt text](https://github.com/adilbekishev/CSS503_Supra_Team_9/blob/main/fridges.PNG)

Depending on the categories of equipment, some characteristics differ, for example, such devices as smartphones and laptops can have much more characteristics that the store provides, in contrast to the same refrigerators.

For example, here is a diagram showing the average price of a TV depending on its brand:

![alt text](https://github.com/adilbekishev/CSS503_Supra_Team_9/blob/main/tv_price_brand.PNG)

The work that was done during this project gave some of us the opportunity to learn how to use the Python language, and some of us to remember what we once knew. Also, the work required learning how to use libraries for analyzing and visualizing data, and we also used Google Sheets for data visualization.
