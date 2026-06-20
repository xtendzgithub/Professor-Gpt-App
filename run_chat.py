import sys
from openai import OpenAI

# NOTE: Using the API key from your notebook. Replace with env var for safety.
client = OpenAI(api_key="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")

gptmodel = "gpt-5.5"

try:
    resp = client.chat.completions.create(
        model=gptmodel,
        messages=[{"role": "user", "content": "Suggest me 3 name ideas for a girl"}]
    )
    print('CALL SUCCESS')
    print(resp)
except Exception as e:
    print('CALL ERROR:', e)
    sys.exit(1)
