import os
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import pandas as pd

options = uc.ChromeOptions()
options.headless = False  # İstəsən True elə, başsız işləsin

driver = uc.Chrome(options=options)

driver.get("https://bina.az/baki/alqi-satqi/menziller?page=3")
time.sleep(7)  # JavaScript yüklənməsi üçün gözləyək

ads = driver.find_elements(By.CLASS_NAME, "products-i")

data = []

for menzil in ads:
    try:
        title = menzil.find_element(By.CLASS_NAME, "product-name")
        price = menzil.find_element(By.CLASS_NAME, "product-price")
        datetime = menzil.find_element(By.CLASS_NAME, "product-datetime")
        attrs = menzil.find_element(By.CLASS_NAME, "product-attributes")

        data.append({
            "Title": title,
            "Price": price,
            "Datetime": datetime,
            "Attributes": attrs
        })
    except:
        continue

print(f"Toplanan elan sayi:{len(data)}")
df = pd.DataFrame(data)
df.to_excel("menzil_listings.xlsx", index=False)

if os.path.exists("menzil_listings.xlsx"):
    print("Excel faylı uğurla yaradıldı.")
    os.startfile("menzil_listings.xlsx")
else:
    print("Fayl yaradıla bilmədi.")
       
driver.quit()
print("Hazırdır, fayl yaradıldı.")