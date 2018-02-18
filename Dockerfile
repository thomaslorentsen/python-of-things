FROM imacatlol/todoist-python
RUN python -m pip install tornado
WORKDIR /usr/src/app
COPY . .
CMD [ "python", "./main.py" ]
