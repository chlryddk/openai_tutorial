from dotenv import load_dotenv
import os

load_dotenv() #.env파일의 변수를 가져오는 것

openai_api_key = os.getenv("OPEN_API_KEY")
pass