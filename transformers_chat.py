import time
from transformers import AutoModelForCausalLM, AutoTokenizer

start_time = time.time()
checkpoint = "HuggingFaceTB/SmolLM2-135M-Instruct"

device = "cpu" # "cuda" for GPU usage or "cpu" for CPU usage
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
# for multiple GPUs install accelerate and do `model = AutoModelForCausalLM.from_pretrained(checkpoint, device_map="auto")`
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)

messages = [
    {"role": "system", "content": "You are a helpful assistant named SmolLM. Be happy, funny and friendly."},
    {"role": "user", "content": "Hey, can you write a story about time, space and the fabric of reality?"}
]
input_text=tokenizer.apply_chat_template(messages, tokenize=False)
print(input_text)
inputs = tokenizer.encode(input_text, return_tensors="pt").to(device)
outputs = model.generate(inputs, max_new_tokens=1024, temperature=0.5, top_p=0.9, do_sample=True)
print(tokenizer.decode(outputs[0]))

end_time = time.time()
print(f"Elapsed time: {end_time - start_time}s | Memory footprint: {model.get_memory_footprint() / 1e6:.2f} MB")
