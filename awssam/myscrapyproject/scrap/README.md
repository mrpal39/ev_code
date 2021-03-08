# Django Dynamic Scraper Tutorial

This sample project tutorial is based on django-dynamic-scraper v.13.  

## Setup

Since Python 3.6 is the stable route for this script, I have decided to use `pyenv` (on Debian 10) to switch the local Python interpreter to Python 3.6.10.  

I have prepared [an install/uninstall script for `pyenv` on Debian 10](https://github.com/0xboz/install_pyenv_on_debian).  

Once `pyenv` is installed, navigate to `example_project` dir and run:  

```shell
pyenv install 3.6.10  #  Install Python 3.6.10
pyenv local 3.6.10  #  Designate Python 3.6.10 as the default interpreter in this dir while creating a file named `.python-version`
pyenv virtualenv django-dynamic-scraper-venv  #  Create a venv for this example project
pyenv activate django-dynamic-scraper-venv  #  Start this venv
```

## Requirements.txt

In the venv created above, run *(note: make sure you are in `example_project` dir)*:

```shell
(django-dynamic-scraper-venv) pip install -U pip
(django-dynamic-scraper-venv) pip install -r requirements.txt
```

## Run

In `example_project` dir (with venv on), run:  

```shell
(django-dynamic-scraper-venv) python manage.py migrate
(django-dynamic-scraper-venv) python manage.py createsuperuser  # Pick your own username and password
```

Start the dev server.  

```shell
(django-dynamic-scraper-venv) python manage.py runserver
```

Go to the admin page `http://127.0.0.1:8000/admin`  

Once you are at the admin dashboard, you can either configure manually according to the document or import the data from `open_news_dds_v013.json` by running this command in the terminal.  

```shell
(django-dynamic-scraper-venv) python manage.py loaddata open_news/open_news_dds_v013.json
```

I would recommend importing the json file, since the details in the doc are out of date as of this writing.  

*Note: You might run into this error when importing.*  

`django.db.utils.OperationalError: Problem installing fixtures: no such table: dynamic_scraper_scrapedobjattr__old`

Check out `Data Importing Issues` for further reading.

However, if you prefer to go with the manual way, you might wanna make a few adjustments according to [a solution I posted on StackOverflow](https://stackoverflow.com/a/61856215).

Finally, you should be good to go by running this command below.

```shell
(django-dynamic-scraper-venv) scrapy crawl article_spider -a id=1 -a do_action=yes
```

## Data Importing Issues

`example_project` is working. The preset data is stored in `example_project/open_news/open_news_dds_v013.json`. However, there is an issue in importing by running  

 `python manage.py loaddata open_news/open_news_dds_v013.json`

 when using `SQLite`, probably due to the compatibility issue. You might use `open_news_dds_v013.json` as a reference to configure Django admin dashboard manually or use MySQL/MariaDB/PostgreSQL instead. However, I have not tested those databases yet.  

## Stay Connected

Join [0xboz's Discord](https://discord.gg/JHt7UQu) and find out more.
