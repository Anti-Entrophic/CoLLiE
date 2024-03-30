import sys
sys.path.append("../../../")

from transformers import AutoTokenizer, GenerationConfig, AutoModelForCausalLM
from collie.models import QWenLMHeadModel
# model_name_or_path = "Qwen/Qwen-7B"
model_name_or_path = "../../../../../../share/storage/moss/Qwen-7B-Chat/"
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, trust_remote_code=True)

# model = QWenLMHeadModel.from_pretrained(model_name_or_path, torch_dtype="auto", trust_remote_code=True).cuda()
model = QWenLMHeadModel.from_pretrained(model_name_or_path, torch_dtype="auto").cuda()
model.eval()

prompt = "Llama is a"
inputs = tokenizer(prompt, return_tensors="pt")
print(inputs)

gen_config = GenerationConfig(max_new_tokens=256, early_stopping=True, eos_token_id=0)

outs = model.generate(inputs["input_ids"].cuda(), generation_config=gen_config)
# if env.local_rank == 0:
print(outs)
print(tokenizer.decode(outs[0], skip_special_tokens=True))