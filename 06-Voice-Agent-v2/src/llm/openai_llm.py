from Week6.src.llm.prompting import SYSTEM_PROMPT
from Week6.config import OPENAI_MODEL, OPENAI_API
from openai import OpenAI

client = OpenAI(api_key=OPENAI_API)

conversation_history = []

def gpt_respond(user_text, model=OPENAI_MODEL):
    try:
        messages_to_send = [{'role': 'system', 'content': SYSTEM_PROMPT}] + conversation_history + [{'role': 'user', 'content': user_text}]
        response = client.chat.completions.create(
            model=model,
            messages=messages_to_send,
            temperature=0.3
        )
        assistant_reply = response.choices[0].message.content.strip()
        conversation_history.append({'role': 'user', 'content': user_text})
        conversation_history.append({'role': 'assistant', 'content': assistant_reply})
        return assistant_reply
    except Exception:
        return 'cou,dnt generate a proper response!'