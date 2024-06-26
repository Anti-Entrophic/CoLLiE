import sys

sys.path.append("../../../")

from transformers import AutoTokenizer, GenerationConfig, AutoModelForCausalLM

# from collie import CollieConfig, env

model_name_or_path = "huggyllama/llama-7b"

tokenizer = AutoTokenizer.from_pretrained(
    model_name_or_path,
    trust_remote_code=True,
)
model = AutoModelForCausalLM.from_pretrained(model_name_or_path, trust_remote_code=True, ).cuda()
model.eval()
prompt = "Llama is a"
inputs = tokenizer(prompt, return_tensors="pt")
print(inputs)
gen_config = GenerationConfig(max_new_tokens=256, early_stopping=True, eos_token_id=0)

outs = model.generate(inputs["input_ids"].cuda(), generation_config=gen_config)
# if env.local_rank == 0:
print(outs)
print(tokenizer.decode(outs[0], skip_special_tokens=True))

'''
Llama is a small, friendly, family run business, based in the heart of the beautiful Peak District National Park. We are a small team of dedicated professionals who are passionate about what we do. We are proud to be a local business, and we are proud to be able to offer a personal service to our customers.
We are a small team of dedicated professionals who are passionate about what we do. We are proud to be a local business, and we are proud to be able to offer a personal service to our customers.
We are a small team of dedicated professionals who are passionate about what we do. We are proud to be a local business, and we are proud to be able to offer a personal service to our customers. We are a small team of dedicated professionals who are passionate about what we do. We are proud to be a local business, and we are proud to be able to offer a personal service to our customers.
We are a small team of dedicated professionals who are passionate about what we do. We are proud to be a local business, and we are proud to be able to offer a personal service to our customers. We are a small team of dedicated professionals who are passionate about what we do
'''