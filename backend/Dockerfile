FROM docker.io/library/python:3.13-alpine

WORKDIR /app
COPY server.py .

USER 65532:65532
EXPOSE 8000
CMD ["python", "-u", "server.py"]
