FROM python

COPY . /cherga.py

WORKDIR /cherga.py

CMD ["python3", "cherga"]
