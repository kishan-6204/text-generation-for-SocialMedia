from transformers import pipeline

# Function to load the text generation model
def load_generator():
    # No need to pass 'use_auth_token' directly in the pipeline
    generator = pipeline('text-generation', model='gpt2')  # You can replace 'gpt2' with any other model
    return generator

# Function to generate text based on a given prompt
def generate_text(prompt, max_length=50):
    generator = load_generator()
    response = generator(prompt, max_length=max_length, num_return_sequences=1)
    return response[0]['generated_text']
