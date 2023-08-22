import undetected_chromedriver as uc
from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import pytesseract
import subprocess
import requests
import pytesseract
import time
# Set any options you want here, if needed
options = uc.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\admin\AppData\Local\Google\Chrome\User Data\Default")
prefs = {
    "download.default_directory": "C:\\file",  # Change this path to your desired download location
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome
}
options.add_experimental_option("prefs", prefs)
driver = uc.Chrome(options=options)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
wait = WebDriverWait(driver, 10)


# Maximizing the browser window


for i in range(311):
    driver.maximize_window()
    driver.get("https://www.elections.tn.gov.in/index.aspx")
    time.sleep(0.8)
    driver.find_element(By.XPATH, "/html/body/form/header/div[2]/nav/div/ul/li[4]/a").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/form/header/div[2]/nav/div/ul/li[4]/div/div[2]/div[1]/a[2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/form/section/div[2]/div[5]/div[1]/a").click()
    time.sleep(5)
    home = driver.current_window_handle
    po = driver.window_handles
    print(po)
    for hand in po:
        driver.switch_to.window(hand)
        print(driver.title)
        options = driver.find_elements(By.TAG_NAME, "option")

        # Printing the text of each option
    for opt in options:
            print(opt.text)
            if (opt.text == "திருவள்ளூர்"):
                opt.click()
                boo = driver.find_elements(By.TAG_NAME, "option")
                time.sleep(1)
                for bo in boo:
                    print(bo.text)
                    if (bo.text == "திருத்தணி"):
                        bo.click()
                        time.sleep(1)
                        driver.find_element(By.XPATH,
                                            "/html/body/form/div[3]/div/div[3]/div/div/div/div[3]/div/div[2]/div[3]/div/input").click()
                        time.sleep(1)
                        row = len(driver.find_elements(By.TAG_NAME, "tr"))
                        print(row)

                        # executed = False
                        r = 3
                        while r <= row:
                            try:
                                # your main code goes here...
                                driver.get("https://www.elections.tn.gov.in/SSR2022_MR_05012022/ac3.html")
                                link = driver.find_element(By.XPATH,
                                                           f"/html/body/form/table[2]/tbody/tr[{r}]/td[2]/p/a").text
                                time.sleep(1)
                                driver.find_element(By.XPATH,
                                                    f"/html/body/form/table[2]/tbody/tr[{r}]/td[2]/p/a").click()
                                time.sleep(1)
                                print(driver.title)
                                image_element = WebDriverWait(driver, 5).until(
                                    EC.presence_of_element_located(
                                        (By.XPATH,
                                         "/html[1]/body[1]/form[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/img[1]"))
                                )
                                path = r"C:\Users\admin\Pictures\captcha.png"
                                image_element.screenshot(path)
                                print("screenshot done")

                                command = [r"C:\Program Files\Tesseract-OCR\tesseract.exe",
                                           r"C:\Users\admin\Pictures\captcha.png", "stdout",
                                           "--dpi", "300"]
                                result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                                        text=True)
                                captcha_text = result.stdout.strip()

                                time.sleep(1)
                                driver.find_element(By.XPATH,
                                                    "/html/body/form/div[3]/div/div[3]/div/div/div/div[3]/div/div[2]/div[1]/div[2]/input").send_keys(
                                    captcha_text)
                                print("the captcha is : " + captcha_text)
                                driver.find_element(By.XPATH,
                                                    "/html/body/form/div[3]/div/div[3]/div/div/div/div[3]/div/div[2]/div[3]/div/input").click()
                                time.sleep(1)
                                pdf_url = driver.current_url
                                # If everything above succeeded, increment r as per your original pattern:
                                r += 2
                            except UnexpectedAlertPresentException:
                                print(r)
                                # When an exception occurs, don't increment r, so the loop will try again with the same value.
                                continue
                            response = requests.get(pdf_url)
                            with open(fr'C:\file\திருத்தணி\city{r}.pdf', 'wb') as file:
                                file.write(response.content)
                            time.sleep(1)
                            driver.switch_to.frame("frame_134")

                            driver.find_element(By.XPATH, '//*[@id="open-button"]').click()
                            print("i clicked the element")
                            time.sleep(1)
                            # executed = True




# Setting up Tesseract
    pytesseract.pytesseract.tesseract_cmd = r'"C:\Program Files\Tesseract-OCR\tesseract.exe"'

# Navigate to the website
# driver.get("https://www.elections.tn.gov.in/SSR2022_MR_05012022/ac2.html")



# Cleanup (optional)
    driver.quit()
