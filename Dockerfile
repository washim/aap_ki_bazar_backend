FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /aap_ki_bazar
COPY . /aap_ki_bazar/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD /aap_ki_bazar/run.sh
