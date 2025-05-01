FROM python:3.12.4-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

#RUN python manage.py migrate
#RUN python fill_db.py

#ENTRYPOINT ["python", "manage.py", "runserver"]

RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]

