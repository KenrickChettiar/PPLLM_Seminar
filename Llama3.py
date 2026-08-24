
def generateLlama3(all_prompts,file_name):
	from transformers import AutoTokenizer, AutoModelForCausalLM
	import json



	model_intentions = []

	tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-3B-Instruct")
	model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-3B-Instruct", device_map="auto")

	for i in range (len(all_prompts)):
		messages = [
			{"role": "user", "content": all_prompts[i]},
		]
		inputs = tokenizer.apply_chat_template(
			messages,
			add_generation_prompt=True,
			tokenize=True,
			return_dict=True,
			return_tensors="pt",
		).to(model.device)

		outputs = model.generate(**inputs, max_new_tokens=256)
		resp = tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:])
		diction = {f"prompt_{i+1}":resp[:-10]}
		model_intentions.append(diction)


	with open(f"{file_name}.json","w") as f:
		json.dump(model_intentions,f, ensure_ascii=False, indent=4)
