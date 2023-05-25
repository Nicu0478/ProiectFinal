import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome = webdriver.Chrome()

class Login(unittest.TestCase):

#se verifica conectarea cu credentialele corecte
    def test_login_corect(self):
        chrome.get("https://www.saucedemo.com/")
        chrome.find_element(By.ID, "user-name").send_keys("standard_user")
        chrome.find_element(By.NAME,"password").send_keys("secret_sauce")
        chrome.find_element(By.ID, "login-button").click()

        expected = "https://www.saucedemo.com/inventory.html"
        actual = chrome.current_url
        self.assertEquals(actual, expected, "Nu suntem pe site-ul dorit")
        sleep(3)

#se verifica log-in cu credentiale incorecte

    def test_credentiale_incorecte(self):
        chrome.get("https://www.saucedemo.com/")
        chrome.find_element(By.ID, "user-name").send_keys("incorect_user")
        chrome.find_element(By.NAME, "password").send_keys("incorect_password")
        chrome.find_element(By.ID, "login-button").click()

        actual = chrome.find_element(By.XPATH, "//h3[@data-test='error']").text
        expected = "Epic sadface: Username and password do not match any user in this service"

        self.assertEquals(expected, actual,"Am reusit sa ne logam cu credentiale incorecte")
        sleep(3)

#v-om testa daca invitatii la nunta sunt peste 76, nunta va avea loc

def verificam_invitati(numar_invitati):
    if numar_invitati > 76:
        return True
    else:
        return False
class Numarul_De_Invitati(unittest.TestCase):
    def test_nunta_invitati(self):
        rezultat = verificam_invitati(100)
        self.assertTrue(rezultat)

    def test_cu_mai_putini_invitati(self):
        rezultat = verificam_invitati(50)
        self.assertFalse(rezultat)


#test de compilare formular
class TestCompilareFormular(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://formy-project.herokuapp.com/form")

    def tearDown(self):
        self.driver.quit()

    def test_compilare(self):
        numele = self.driver.find_element(By.ID, "first-name")
        numele.send_keys("Nicu")
        prenume = self.driver.find_element(By.ID, "last-name")
        prenume.send_keys("Palamariu")
        meseria = self.driver.find_element(By.ID, "job-title")
        meseria.send_keys("Lowest Level of Automation Junior")
        studii = self.driver.find_element(By.ID, "radio-button-1")
        studii.click()
        sex = self.driver.find_element(By.ID, "checkbox-1")
        sex.click()
        sleep(3)

#Testare de buton Dropdown
class TestDropdown(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://formy-project.herokuapp.com/")
        sleep(3)

    def tearDown(self):
        self.driver.quit()

    def test_dropdown(self): #<- Gasește link-ul "Dropdown" si face click pe el
        dropdown_link = self.driver.find_element(By.LINK_TEXT, "Dropdown")
        dropdown_link.click()
        sleep(3)
     #Găsește elementul dropdown cu ID-ul "dropdownMenuButton" și face clic pe el
        dropdown = self.driver.find_element(By.ID, "dropdownMenuButton")
        dropdown.click()
        sleep(3)

#testare de click pe java script dupa seletorul Partial Link Text
class TestJavaScript(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/")
        sleep(3)

    def tearDown(self):
        self.driver.quit()

    def test_java_script_link(self):
        java_script_link = self.driver.find_elements(By.PARTIAL_LINK_TEXT, 'Java')[1]
        java_script_link.click()
        sleep(3)


#testare compilare lista cu datele personale si profesia
class TestForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
        sleep(3)

    def tearDown(self):
        self.driver.quit()

    def test_fill_form(self):
        first_name = self.driver.find_element(By.NAME, "firstname")
        first_name.send_keys("Nicu")
        last_name = self.driver.find_element(By.NAME, 'lastname')
        last_name.send_keys('Palamariu')
        gender = self.driver.find_element(By.ID, "sex-0")
        gender.click()
        profesia = self.driver.find_element(By.ID, "profession-1")
        profesia.click()
        sleep(3)



        




