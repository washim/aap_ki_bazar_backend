FROM python:3
2	ENV PYTHONUNBUFFERED=1
3	WORKDIR /aap_ki_bazar
4	COPY . /aap_ki_bazar/
5	RUN pip install -r requirements.txt
6	EXPOSE 8000
7	CMD /aap_ki_bazar/run.sh