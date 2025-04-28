FROM python:latest
WORKDIR /app
COPY req.txt .
RUN pip install -r req.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
