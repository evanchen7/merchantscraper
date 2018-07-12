# Merchant Competition Checker

## Getting Started

### Prerequisites

In order to run the following scripts, you will need to setup Python 3 on your machine along with its package dependencies.

* [MacOS](http://docs.python-guide.org/en/latest/starting/install3/osx/#install3-osx) - Install Guide
* [Linux](http://docs.python-guide.org/en/latest/starting/install3/linux/#install3-linux) - Install Guide
* [Windows](http://docs.python-guide.org/en/latest/starting/install3/win/#install3-windows) - Install Guide

#### Optional (Highly Recommended): Virtualenv
Virtualenv is a tool that lets you create an isolated Python environment for your project. It creates an environment that has its own installation directories, that doesn’t share dependencies with other virtualenv environments (and optionally doesn’t access the globally installed dependencies either).

To install virtualenv run:
```
$ pip3 install virtualenv
```

This will install the virtual enviroment package
```
$ cd my-project/
$ virtualenv env
```

These commands create a env/ directory in your project where all dependencies are installed. You need to activate it first though (in every terminal instance where you are working on your project)
```
$ source env/bin/activate
```

You should see a (env) appear at the beginning of your terminal prompt indicating that you are working inside the virtualenv. Now when you install something like this
```
$ pip3 install requirements.txt
```
It will get installed in the env/ folder, and not conflict with other projects.

To leave the virtual enviroment run:
```
$ deactivate
```

#### Installing Dependencies

In order for the scripts to run, a couple dependencies need to be installed.

```
$ pip3 install -r requirements.txt
```

This will install all the dependencies defined in the requirements.txt for the project.

#### Chromedriver for Selenium

Selenium requires a browser driver to navigate webpages, user input, JavaScript, etc: http://chromedriver.chromium.org/

MacOS:
```
$ brew cask install chromedriver
```

## Usage

### LocalFilesCompetitionChecker()
| Parameters | Type | Description | Example |
| --- | --- | --- | --- |
| pathToFolder | String | Relative or Absolute path to theme files | '/Users/evanchen/Desktop/Afterpay'
| fileType | String | Name of the file extension | '.liquid', '.js' |
| targetWords | List | Names of competitors, fewer keywords for performant runtime | ['foo', 'afterpay', 'baz', 'bar']
| merchantName | String | Specifies the name of the output text | Defaults: 'concantenated'|

#### Example Input
```
path = '/Users/evanchen/Desktop/Afterpay'
fileType = ['.liquid']
keywords = ['affirm', 'afterpay']
name = 'Afterpay'
```
```
LocalFilesCompetitionChecker(path, fileType, keywords, name)
```
```
$ python LocalFilesCompetitionChecker.py
```

#### Example Output
```
-----BEGIN LOGS-----
Tue May 29 20:59:08 2018

filename: target/templates/collection.liquid LINE:282                <!-- QuadPay Changes Start -->
filename: target/templates/collection.liquid LINE:284                  #quadPayCalculatorWidget {
filename: target/templates/collection.liquid LINE:288                  #quadPayCalculatorWidgetText {
filename: target/templates/collection.liquid LINE:291                  #quadPayCalculatorWidgetLearn {
```

### FrontendMerchantCompetitionChecker()
This script will collect all links found on one page and will search for keywords found in those links. Each link will be rendered by Selenium which will ensure asynchronous javascript loads before scraping the page.

| Parameters | Type | Description | Example |
| --- | --- | --- | --- |
| website | String | Name of the target website | 'https://www.example.com' |
| keywords | List | List of keywords to search for | ['foo', 'baz', 'bar'] |
| linkCount | Int | Number of links to search for before terminating | 30 |
| headlessMode | Boolean | Runs headless mode  | Defaults: False |


## Running the tests
Unit tests are created from Python's unittest module.

Ensure that the path to files are correct
```
$ python LocalFilesTest.py
```

## Built With
* [regex](https://pypi.org/project/regex/) - Alternative regular expression module, to replace re.
* [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/) - Python library for pulling data out of HTML and XML files.
* [selenium](https://pypi.org/project/selenium/) - Web browser module used to automate web interaction from Python.

## To Do
* Allow functions to run from command line
* Implement server to run functions
* Dockerize application

## Authors
* **Evan Chen** - *Initial work* - [evanchen7](https://github.com/evanchen7)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details