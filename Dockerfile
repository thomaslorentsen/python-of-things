FROM imacatlol/todoist-python
WORKDIR /usr/src/app
COPY . .
CMD [ "python", "./main.py" ]
