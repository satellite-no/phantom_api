# Splunk Phantom SOAR Module

## Introduction 
The Phantom module was developed for easy python communication to and from a Splunk Phantom server using it's native API.

## Getting Started
1.  Clone the repository to your local computer
2.  Copy the "phantom_api" folder to */lib/site-packages* (C:\Users\FRODO\AppData\Local\Programs\Python\Python37-32\Lib\site-packages)
3.	Software dependencies
	a. requests (standard python modules)
4.  Review the documentatoin below on usage.

## Usage and Test
To use phantom_api import the phantom library to your script and create a phantom server object by calling 'PhanServer' with the base URL and api key
for paramaters.
'''
>>> from phantom_api import tmo_phantom
>>> ph = phantom_api.PhanServer('https://phantom-server.local', '12345678910111213141516')
>>> user = ph.get_user(3)
>>> container = ph.get_container(7)
'''


## Contribute
1.  Become more familiar with the project by reading our Contributor's Guide and our development philosophy.
2.  Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug. There is a Contributor Friendly tag for issues that should be ideal for people who are not very familiar with the codebase yet.
3.  Fork the repository on GitHub to start making your changes to the master branch (or branch off of it).
4.  Write a test which shows that the bug was fixed or that the feature works as expected.
