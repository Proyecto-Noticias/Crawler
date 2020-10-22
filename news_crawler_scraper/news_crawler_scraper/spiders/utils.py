from bs4 import BeautifulSoup

def format_body(text):
        html_body = ''
        for t in text:
            html_body += str(t)

        soup = BeautifulSoup(html_body, features="html.parser")

        # get text
        text = soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

        return text