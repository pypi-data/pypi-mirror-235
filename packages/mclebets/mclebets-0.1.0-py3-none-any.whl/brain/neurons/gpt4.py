import openai
import logging

class GPT4:
    def __init__(self):
        openai.api_key = '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'

    def predict(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-4", 
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        
        generated_text = response['choices'][0]['message']['content']
        logging.info(generated_text)
      
        return generated_text

  
