# AlwaysUpdate ~ Web Crawler and Scraper 📰

![Always Update](https://avatars3.githubusercontent.com/u/72758625?s=200&v=4)

AlwaysUpdate is an e-NewsPaper from Argentina, Colombia, Venezuela and Mexico, that update its news every day.

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

## Demo

[![Alt text for your video](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/473ce9d0-9aa9-4f36-8807-07d561fe329b/video.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201104T163553Z&X-Amz-Expires=86400&X-Amz-Signature=5686e73ea4d4bec8167d27584b9060564d7093e45eaea4bfd9940c3a3e51ff84&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22video.png%22)](https://www.youtube.com/watch?v=kDm-sx_sU5o)

## License 📄
[MIT](https://choosealicense.com/licenses/mit/)


