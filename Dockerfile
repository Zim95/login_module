FROM python:3.7

RUN mkdir app/
COPY . app/

WORKDIR /app/

RUN pip install -r requirements.txt
RUN sed -i '18 a from .utils import cached_property' /usr/local/lib/python3.7/site-packages/werkzeug/__init__.py

CMD ["gunicorn", "app:app", "-c", "./gunicorn-config.py", "--reload"]