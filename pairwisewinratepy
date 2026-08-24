from Llama3 import model_intentions
from altprag import eval_data

placeholder = ''

all_scoring_prompts = []
for i in range(len(model_intentions)):
    
    prompt = f'''You are an expert evaluator of language model analysis. Your task is to compare two model analysis of the intention of response_1, 

which is a response to the "initial turn", and choose which one better aligns with the golden label’s intention. 

The conversation structure is: 

"context": ... "initial turn": ... "response_1": ... "response_2": ... "golden_label": ... 

The models are asked to evaluate: What is the intention behind ‘response_1’? Why or when might someone prefer ‘response_1’ over ‘response_2’? 

Model 1’s response: {placeholder} Model 2’s response: {placeholder} 

Choose which response better captures the intention described in the golden label. 

After comparing the two responses, you also need to categorize how the better response is better than the other. 

Here are the categories: 

### **Category #1: Cognitive-Pragmatic Competence** 

description: The better response goes beyond the literal meaning of the sentence and 

identifies the speaker’s underlying social goal, such as softening a refusal or signaling indirect disagreement. 

### **Category #2: Pragmalinguistic Competence** 

description: The better response identifies and explains rhetorical techniques—like humor, 

irony, or self-deprecation—and clarifies how these strategies function to manage emotion 

or social tension. 

### **Category #3: Sociopragmatic Competence** 

204 

description: The better response shows sensitivity to the social context, including roles, 

relationships, or timing, and explains why the speaker’s choice fits the situation appropriately. 

If you feel the better response does not fall into any of the categories, 

you can choose "Invalid", and explain how it better than the other in the "reason" field. 

Return ONLY a JSON object with the following format: 

{{ 

"choice": "1" or "2" or "Invalid", 

"reason": "<brief explanation in 20 words or less>", 

"category": "1" or "2" or "3" or "Invalid" 

}}
You should understand that the tested models might be base models, 

thus not deliberately instructed to format their responses and may output random strings and sentences. You need to purely focus on the content and compare them instead of having preference on the format
Return "Invalid" if: 

- Either response is empty, nonsense, unrelated to the question, or as long as you feel it is not answering the question 

- You cannot make a clear choice between the two responses'''
    all_scoring_prompts.append(prompt)
print(all_scoring_prompts)

