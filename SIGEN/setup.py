from setuptools import setup

setup(name='SIGEN',
      version='0.900000031',
      include_package_data=True,
      description='SIGEN',
      packages=[
          'SIGEN',
          'SIGEN.views',
          'SIGEN.configs',
          'SIGEN.forms',
          'SIGEN.functions'
          ],
      install_requires=[
          'flask',
          'flask-wtf',
          'flask-login',
          'wtforms',
          'sqlalchemy',
          'bcrypt',
          'pymysql',
          'werkzeug',
          'requests',
          ],
      zip_safe=False)
