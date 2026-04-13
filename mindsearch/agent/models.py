import os
from dotenv import load_dotenv
from lagent.llms import (
    GPTAPI,
    INTERNLM2_META,
    HFTransformerCasualLM,
    LMDeployClient,
    LMDeployServer,
)

internlm_server = dict(
    type=LMDeployServer,
    path="internlm/internlm2_5-7b-chat",
    model_name="internlm2_5-7b-chat",
    meta_template=INTERNLM2_META,
    top_p=0.8,
    top_k=1,
    temperature=0,
    max_new_tokens=8192,
    repetition_penalty=1.02,
    stop_words=["<|im_end|>"],
)

internlm_client = dict(
    type=LMDeployClient,
    model_name="internlm2_5-7b-chat",
    url="http://127.0.0.1:23333",
    meta_template=INTERNLM2_META,
    top_p=0.8,
    top_k=1,
    temperature=0,
    max_new_tokens=8192,
    repetition_penalty=1.02,
    stop_words=["<|im_end|>"],
)

internlm_hf = dict(
    type=HFTransformerCasualLM,
    path="internlm/internlm2_5-7b-chat",
    meta_template=INTERNLM2_META,
    top_p=0.8,
    top_k=None,
    temperature=1e-6,
    max_new_tokens=8192,
    repetition_penalty=1.02,
    stop_words=["<|im_end|>"],
)

gpt4 = dict(
    type=GPTAPI,
    model_type="gpt-4-turbo",
    key=os.environ.get("OPENAI_API_KEY", ""),
    api_base="https://api.openai.com/v1/chat/completions",
)

gemini = dict(
    type=GPTAPI,
    model_type="gpt-3.5-turbo",
    key=os.environ.get("GEMINI_API_KEY", ""),
    api_base="https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
    max_new_tokens=4096,
    temperature=0.7,
)

groq = dict(
    type=GPTAPI,
    model_type="gpt-3.5-turbo",
    key=os.environ.get("GROQ_API_KEY", ""),
    api_base="https://api.groq.com/openai/v1/chat/completions",
    max_new_tokens=4096,
    temperature=0.7,
)

qwen = dict(
    type=GPTAPI,
    model_type="qwen-max-longcontext",
    key=os.environ.get("QWEN_API_KEY", ""),
    api_base="https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions",
    top_p=0.8,
    top_k=1,
    temperature=0,
    max_new_tokens=4096,
    repetition_penalty=1.02,
    stop_words=["<|im_end|>"],
)

internlm_silicon = dict(
    type=GPTAPI,
    model_type="internlm/internlm2_5-7b-chat",
    key=os.environ.get("SILICON_API_KEY", ""),
    api_base="https://api.siliconflow.cn/v1/chat/completions",
    top_p=0.8,
    top_k=1,
    temperature=0,
    max_new_tokens=8192,
    repetition_penalty=1.02,
    stop_words=["<|im_end|>"],
)
