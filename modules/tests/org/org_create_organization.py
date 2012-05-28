from tests.web2unittest import SeleniumUnitTest
from tests import *

class org_create_organization(SeleniumUnitTest):
    def test_create_organization(self):

        browser = self.browser
        org_table = self.current.s3db.org_organisation
        name = "Romanian Food Assistance Association (Test)"
        query = ((org_table.name == name) & (org_table.deleted == "F"))
        org_id = self.current.db(query).select(org_table.id,limitby=(0, 1)).first()
        if org_id:
            print "test_create_organization - Not run as Organization name already exists in the db"
            return False
        driver = self.browser
        self.login(account="normal", nexturl="org/organisation/create")
#        driver.find_element_by_link_text("Organizations").click()
#        driver.find_element_by_link_text("New").click()
        driver.find_element_by_id("org_organisation_name").click()
        driver.find_element_by_id("org_organisation_name").clear()
        driver.find_element_by_id("org_organisation_name").send_keys(name)
        driver.find_element_by_id("org_organisation_acronym").clear()
        driver.find_element_by_id("org_organisation_acronym").send_keys("RFAAT")
        driver.find_element_by_id("org_organisation_type").send_keys("Institution")
        driver.find_element_by_id("org_organisation_region").clear()
        driver.find_element_by_id("org_organisation_region").send_keys("???")
        driver.find_element_by_id("org_organisation_country").send_keys("Romania")
        driver.find_element_by_id("org_organisation_website").clear()
        driver.find_element_by_id("org_organisation_website").send_keys("www.rfaat.com")
        driver.find_element_by_id("org_organisation_comments").clear()
        driver.find_element_by_id("org_organisation_comments").send_keys("This is a Test Organization")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Home").click()
