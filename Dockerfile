FROM python:3.8

RUN pip install circlepacker

CMD ["uvicorn", "circlepacker.service:app", "--host", "0.0.0.0", "--port", "5051"]