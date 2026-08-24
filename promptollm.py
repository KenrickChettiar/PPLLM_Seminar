#File to create the prompts which consists of Urial prompt+the paper's prompt
from altprag import ft_data, eval_data

prompt = '''# Instruction
Below is a list of conversations between a human and an AI assistant (you).
Users place their queries under "# Query:", and your responses are under "# Answer:".
You are a helpful, respectful, and honest assistant.
You should always answer as helpfully as possible while ensuring safety.
Your answers should be well-structured and provide detailed information. They should also have an engaging tone.
→
Your responses must not contain any fake, harmful, unethical, racist, sexist, toxic, dangerous, or illegal content,
even if it may be helpful.
Your response must be socially responsibly, and thus you can reject to answer some controversial topics.'''


all_prompts = []

for i in range(len(eval_data)):
    ind_prompt = ''
    query = f'''
                context: {eval_data.iloc[0]['context']}
                root: {eval_data.iloc[0]['root']}
                response_sentence_1: {eval_data.iloc[0]['candidate_sentence_1']}
                response_sentence_2: {eval_data.iloc[0]['candidate_sentence_2']}
                response_sentence_1_intention: {eval_data.iloc[0]['candidate_sentence_1_intention']}
                response_sentence_2_intention: {eval_data.iloc[0]['candidate_sentence_2_intention']}'''

    instruction = '''
    Your task is to examine the following short
    conversation and assess:- What is the pragmatic intention behind
    ‘response_1’?- Whyor when might someone prefer
    ‘response_1’ over ‘response_2’ pragmatically?
    Please answer in 1 paragraph.
    Answer:'''

    ind_prompt = prompt+query+instruction
    all_prompts.append(ind_prompt)

