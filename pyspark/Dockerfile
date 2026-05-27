FROM python:3.9-slim
RUN pip install psycopg2-binary
COPY jobs /opt/jobs
CMD ["python", "/opt/jobs/analytics_masivo.py"]
