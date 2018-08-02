from setuptools import setup


setup(
    name='instabot',
    packages=['instabot', 'instabot.bot', 'instabot.api'],
    version='0.4.2',
    description='Cool Instagram bot scripts and API python wrapper.',
    author='Daniil Okhlopkov, Evgeny Kemerov',
    author_email='ohld@icloud.com, eskemerov@gmail.com',
    url='https://github.com/instagrambot/instabot',
    download_url='https://github.com/instagrambot/instabot/tarball/0.4.2',
    keywords=['instagram', 'bot', 'api', 'wrapper'],
    classifiers=[],
    install_requires=['tqdm', 'requests-toolbelt', 'requests', 'schedule', 'future', 'six', 'huepy'],
)
