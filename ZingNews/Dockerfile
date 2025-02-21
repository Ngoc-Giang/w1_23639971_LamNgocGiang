FROM python:3.9
WORKDIR /app
COPY . .
EXPOSE 3000
# CMD ["python", "crawling_spider.py"]
CMD ["sh", "-c", "python crawling_spider.py & python crawlin_spider2.py"]
