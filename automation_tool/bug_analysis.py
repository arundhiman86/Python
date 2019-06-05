"""
This module is written to automate the process of bug analysis
"""
import sys
import re
import time
import os
import configparser
import urllib.request

from subprocess import call
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
Loading user defined variable from the configuration file config.ini
'''
conf = configparser.ConfigParser()
CONFFILE = "config2.ini"
conf.read(CONFFILE)


def driver_load():
    """
    This function will call Chrome browser and will open a pre-defined TDP link

    :return:

    It will return the Webdriver for further processing
    """
    driver = webdriver.Firefox()
    lin = '{}'.format(conf.get('params', 'head1'))
    linc = lin + number
    driver.get(linc)
    try:
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located(
                (By.ID, "jazz_app_internal_LoginWidget_0_userId")))
    except Exception:
        print("Timeout:- Not able to find Login Details")
    return driver


def login():
    """
    The function will login the user to the provided url as provided in
    configuration file.

    :return:

    This function will not return anything

    """

    user1 = driver.find_element_by_id('{}'.format(conf.get('web',
                                                           'get_userid')))
    pass1 = driver.find_element_by_id('{}'.format(conf.get('web',
                                                           'get_passid')))
    user1.send_keys('{}'.format(conf.get('creds', 'user')))
    pass1.send_keys('{}'.format(conf.get('creds', 'passwd')))
    driver.find_element_by_xpath('{}'.format(conf.get('web',
                                 'button'))).click()


def main():
    """
    The main function will get the details about the bug number
    as provided by the user, it will further search for the latest jenkins link
    mentioned in the comments of the bug and will fetch out three error
    reports:
        1. console output
        2. filtered fuel logs
        3. full fuel logs

    It will futher process the above mentioned logs for "ERROR" keyword
    and will create three new files in the mentioned directory within
    configuration file for further processing by the Development Engineer:
        1. console_error.log
        2. fuel_filtered_error.log
        3. fuel_full_error.log

    :return:

    This function will retrun nothing
    """

    login()
    try:
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((
            By.CLASS_NAME, "SectionContent")))
        # TODO add exception handling
        time.sleep(15)
        htm2 = driver.execute_script('{}'.format(conf.get('web',
                                                          'inner_html')))
        l2_tag = re.findall('{}'.format(conf.get('params', 'regex2')),
                            htm2)
        ser2 = re.search('{}'.format(conf.get('params', 'search2')),
                         l2_tag[0])
        jenk = re.sub(r'href="', '', ser2.group(0))
        driver.get(jenk)
        home = '{}'.format(conf.get('params', 'home_dir'))
        bug = home + number
        if not os.path.exists(bug):
            os.makedirs(bug)
        link = driver.find_element_by_partial_link_text(
            'Console Output')
        console = link.get_attribute("href")
        console_full = console + "Full"
        driver.get(console_full)
        try:
            WebDriverWait(driver, 120).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "console-output")))
        except Exception:
            print("Not able to find Console Output")
        console_output = driver.find_element_by_class_name(
            "console-output").text
        confu = os.path.join(bug, "console_output_full.log")
        with open(confu, 'w') as file_:
            file_.write(console_output)
        print("console output stored")
        driver.execute_script("window.history.go(-1)")
        try:
            WebDriverWait(driver, 120).until(
                EC.presence_of_element_located(
                    (By.LINK_TEXT, "Build Artifacts")))
            driver.find_element_by_xpath(
                "//a[contains(@href,'artifact/')]").click()
            try:
                WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located(
                        (By.LINK_TEXT, "logs")))
                driver.find_element_by_xpath(
                    "//a[contains(@href,'logs')]").click()
            except:
                print("Not able to find logs in Artifacts")
        except:
            print("Not able to find Build Artifacts")
        try:
            WebDriverWait(driver, 120).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "fileList")))
            elems = driver.find_elements_by_xpath(
                "//a[contains(@href, 'fail_error_')]")
            url_list = []
            for elem in elems:
                ref = elem.get_attribute("href")
                actl = ref.split("/*", 1)[0]
                if actl in url_list:
                    continue
                else:
                    url_list.append(actl)
            print(url_list)
            for l1 in url_list:
                if "filtered.log" in l1:
                    driver.get(l1)
                    fuel_filtered_log = driver.page_source
                    filt = os.path.join(bug, "filtered.log")
                    with open(filt, 'w') as f2:
                        f2.write(fuel_filtered_log)
                else:
                    print(l1)
                    full = os.path.join(bug,
                                        "fuel_snapshot_full.tar.gz")
                    content = urllib.request.urlretrieve(l1, full)
                    print("Download Complete now executing shell script")
                    call(['./script.sh', bug])
        except Exception:
            print("Not able to find Jenkins File List")
    except Exception:
        print("Unable to load discussion content try again!")

if __name__ == '__main__':
    number = input("Enter Bug Number: ")
    driver = driver_load()
    main()
