import openai

# Replace 'your_openai_api_key_here' with your actual OpenAI API key
openai.api_key = 'your_openai_api_key_here'

def evaluate_code_change(description):
    """
    Use OpenAI to evaluate a code change or new feature's impact on a DIS.
    
    Parameters:
    - description (str): A detailed description of the code change or new feature.
    
    Returns:
    - str: The AI's evaluation.
    """
    
    prompt = (f"Given a distributed information system (DIS), evaluate the following change "
              f"and determine its potential impact level (High, Medium, Low, None) and justification: \n\n"
              f"Change Description: {description}\n\n"
              f"Evaluation:")
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use the most capable model available
            prompt=prompt,
            max_tokens=150,  # Adjust based on how detailed you want the response to be
            n=1,
            stop=None,
            temperature=0.7  # Adjust to make responses more or less creative
        )
        
        evaluation = response.choices[0].text.strip()
        return evaluation
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

# Example usage

description_of_change = (
    "Introducing a new caching layer to reduce database load for frequently accessed "
    "queries. This cache is expected to have a time-to-live (TTL) of 10 minutes to ensure "
    "data consistency. It will be deployed as part of our backend services that handle "
    "user profile information."
)

evaluation = evaluate_code_change(description_of_change)
print("AI Evaluation:", evaluation)
