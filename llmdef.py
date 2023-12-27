import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
ANTHROPIC_API_KEY= os.environ['ANTHROPIC_API_KEY']

from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from openai import ChatCompletion
import openai


class OpenAIChatbot:
    def __init__(self, api_key=None, model_name=None):
        # 如果没有提供 api_key 或 model_name，则使用默认值
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model_name = model_name or "gpt-3.5-turbo"        
        # 设置API key
        openai.api_key = self.api_key        
        # 初始化消息列表
        self.messages = []

    def talk(self, messages:tuple): 
        self.messages.clear()
        system_message = messages[0]
        user_message = messages[1]
        self.messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]
        return self.get_response()  

    def get_response(self):
        response = ChatCompletion.create(
            model=self.model_name, 
            messages=self.messages
        )
        return response['choices'][0]['message']['content']

class AnthropicChatbot:
    def __init__(self, api_key, model_name=None):
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        self.model_name = model_name  or "claude-instant-1"
        # 初始化消息列表
        self.messages = []

    def talk(self, messages:tuple):
        self.messages.clear()
        system_message = messages[0]
        user_message = messages[1]
        self.messages.append(system_message) 
        self.messages.append(user_message)
        return self.get_response()

    def get_response(self):
        self.anthropic = Anthropic(api_key=self.api_key)
        prompt_formated = HUMAN_PROMPT.join(self.messages) + AI_PROMPT
        completion = self.anthropic.completions.create(
        model=self.model_name,  
        max_tokens_to_sample=300,
        prompt=prompt_formated
        )       
        return completion.completion
    

def choose_llm(model_name):
    if model_name == "gpt_35_turbo":
        return OpenAIChatbot(api_key=OPENAI_API_KEY, model_name="gpt-3.5-turbo")
    elif model_name == "claude_2":
        return AnthropicChatbot(api_key=ANTHROPIC_API_KEY, model_name="claude-2")
    elif model_name == "claude_instant":
        return AnthropicChatbot(api_key=ANTHROPIC_API_KEY, model_name="claude-instant-1")

