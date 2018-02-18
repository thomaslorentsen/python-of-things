FROM imacatlol/todoist-python
EXEC python -m pip install tornado
WORKDIR /usr/src/app
COPY . .
CMD [ "python", "./main.py" ]
