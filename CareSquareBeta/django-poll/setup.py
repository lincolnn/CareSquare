from distutils.core import setup

setup(name='django-poll-system',
      version='0.2.0',
      description='The application to organize polling (or voting) on your site.',
      author='RafRaf',
      maintainer='RafRaf',
      author_email='smartrafraf@gmail.com',
      url='http://polltest.pythonism.ru',
      download_url='https://bitbucket.org/RafRaf/django-poll-system',
      packages=['poll', 'poll.templatetags'],
      package_data={'poll': ['fixtures/initial_data.json', 'locale/ru/LC_MESSAGES/*', 'templates/*']},
     )