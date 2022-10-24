FROM python:slim
ENV TOKEN='здесь необходимо указать свой TOKEN'
COPY . .
RUN pip install -r requirements.txt
CMD python bot.py
