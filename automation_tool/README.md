# Automation tool for bug analysis

### TechStack

The automation tool uses open Source tool Selenium with python

* **[Python 3.5]** - Python is an interpreted high-level programming language for general-purpose programming.
* **[Selenium 3.x]** - Selenium WebDriver is a collection of open source APIs which are used to automate the testing of a web application

### Installation

**Python Installtion**
Follow Steps as mentioned in the link below:
https://www.python.org/downloads/operating-systems/

**Selenium Installtion**
You can download Python bindings for Selenium from the PyPI page for selenium package. However, a better approach would be to use pip to install the selenium package. Python 3.6 has pip available in the standard library. Using pip, you can install selenium like this:

```sh
$ pip install selenium
```

**Selenium Drivers**

Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires geckodriver, which needs to be installed before the below examples can be run. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.

Failure to observe this step will give you an error selenium.common.exceptions.WebDriverException: Message: ‘geckodriver’ executable needs to be in PATH.

Other supported browsers will have their own drivers available. Links to some of the more popular browser drivers follow.

**Note:-** 
Kindly check the compatibility of the driver version with selenium before you proceed with the installation.

| Browser | Driver Download Link                                                          |
| ------- | ----------------------------------------------------------------------------- |
| Chrome  | [https://sites.google.com/a/chromium.org/chromedriver/downloads][PlDb]        |
| Edge    | [https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/][PlGh] |
| Firefox | [https://github.com/mozilla/geckodriver/releases][PlGd]                       |
| Safari  | [https://webkit.org/blog/6900/webdriver-support-in-safari-10/][PlOd]          |

### Before running the tool

Edit the config file to provide the basic parameters in **config.ini** file such as:
username, password and the project link.
```sh
$ vim config.ini
```

### Running the tool

```sh
$ python3 bug_analysis.py
```

