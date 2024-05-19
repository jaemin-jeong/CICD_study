FROM python:3.12.3

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r cicd_project/requirements.txt

CMD ["python",  "manage.py", "runserver", "0.0.0.0:8000"]

