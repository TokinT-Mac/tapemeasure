FROM python:2-onbuild

EXPOSE 2599

CMD ["python", "./tape.py"]
