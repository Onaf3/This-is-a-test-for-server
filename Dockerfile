From python:alpine3.19

WORKDIR ./Containerserver

COPY . .

RUN pip install numpy

EXPOSE 8000

CMD ["sh"]


