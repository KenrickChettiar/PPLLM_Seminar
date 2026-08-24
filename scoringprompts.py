def scoringprompt(eval_data,model_responses):
    from altprag import eval_data
    import json


    all_scoring_prompts = []
    for i in range(len(model_responses)):
        
        prompt = f'''You are an expert evaluator of language
    model responses. Your task is to score how
    well a model’s response captures the idea of
    a response to a given sentence.
    The tested model will see a conversation
    structure like this:
    "context": ...
    "initial turn": ...
    "response_1": ...
    "response_2": ...
    And they are asked to evaluate:
    What is the intention behind ‘response_1’?
    Why or when might someone prefer
    ‘response_1’ over ‘response_2’?
    We have the reference golden intention for
    you: {eval_data.iloc[i]['candidate_sentence_1_intention']}, this is the core idea of the intention
    of response_1.
    Model’s response: {model_responses[i]}
    You should understand that the tested
    models are base models, thus not
    deliberately instructed to format their
    responses and may output random strings
    and sentences. You just need to check the
    content of their responses instead of the
    format.
    Score the model’s response on a scale of 1
    to 10, or Invalid, where:- 10: The model’s response perfectly
    captures the intention described in the
    reference- 1: The model’s response poorly captures
    the intention described in the reference- Invalid: The model’s response is nonsense
    or invalid
    Return ONLY a JSON object with the
    following format:
    {{
    "score": <number between 1 and 10 or
    Invalid>,
    "reason": "<brief explanation of your score,
    no more than 25 words>"
    }}
    Do not include any other text, just the
    JSON object.'''
        all_scoring_prompts.append(prompt)

    return all_scoring_prompts



