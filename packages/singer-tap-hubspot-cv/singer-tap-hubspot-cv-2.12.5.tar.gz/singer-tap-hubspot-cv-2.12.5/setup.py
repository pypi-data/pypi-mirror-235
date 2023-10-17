#!/usr/bin/env python

from setuptools import setup

setup(name='singer-tap-hubspot-cv',
      version='2.12.5',
      description='Singer.io tap for extracting data from the HubSpot API',
      author='Stitch',
      url='http://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_hubspot'],
      install_requires=[
          'attrs==16.3.0',
          'singer-python==5.13.0',
          'requests==2.20.0',
          'backoff==1.8.0',
          'requests_mock==1.3.0',
      ],
      extras_require= {
          'dev': [
              'pylint==2.5.3',
              'nose==1.3.7',
          ]
      },
      entry_points='''
          [console_scripts]
          singer-tap-hubspot=tap_hubspot:main
      ''',
      packages=['tap_hubspot'],
      package_data = {
          'tap_hubspot/schemas': [
              "campaigns.json",
              "companies.json",
              "contact_lists.json",
              "contacts.json",
              "deals.json",
              "email_events.json",
              "engagements.json",
              "forms.json",
              "keywords.json",
              "owners.json",
              "subscription_changes.json",
              "workflows.json",
          ],
      },
      include_package_data=True,
)
