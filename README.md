# AlwaysUpdate ~ Web Crawler and Scraper 📰


# Getting started 🚀
## Things that you need to have installed in your system: 🛠️
 * Python 3.7
 * pip
 * virtualenv
 * AlwaysUpdate ~ DataScience API 
 
## Configuration 🔧
### Virtual enviroment
```bash
virtualenv venv --python=python.3.7
source venv/bin/activate
```
### Dependencies installation
```bash
pip install -r requirements.txt
```

### System Variables
```bash
export API_URL="$DATASCIENCE_API_HOST/api/v1/"
export GOOGLE_APPLICATION_CREDENTIALS="credentials.json"
```


### Execution

You can execute the crawler with a POST request, in that case you must start the uvicorn server:
```bash
cd news_crawler_scraper
uvicorn app.main:app --reload 
```

If you don't want to work with the server you can use:
```bash
python go_spyder_$JOURNAL_NAME.py
```

Journals: 
* eltiempo
* lanacion
* eluniversal
* xataka


## Contributing ✒️
Pull requests are welcome!. And if you have an idea for a feature and dont have time to do this, feel free to open a issue!


## License 📄
[MIT](https://choosealicense.com/licenses/mit/)


