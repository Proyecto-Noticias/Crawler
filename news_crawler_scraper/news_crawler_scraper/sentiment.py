import pandas as pd
from textblob import TextBlob

import re
import time

def clean_text(text):
  text = re.sub(r'^RT[\s]+', '', text)
  text = re.sub(r'https?:\/\/.*[\r\n]*', '', text)
  text = re.sub(r'#', '', text)
  text = re.sub(r'@[A-Za-z0-9]+', '', text)
  return text

def get_polarity(text):
  analysis = TextBlob(text)
  if text != '':
    if analysis.detect_language() == 'es':
      result = analysis.translate(from_lang = 'es', to = 'en').sentiment
      time.sleep(2)
      return result