from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

model = HuggingFaceEndpoint(
    model="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
    huggingfacehub_api_token=os.getenv("HF_API"),
    max_new_tokens=512,
    temperature=0.7,
    top_k=250,
    top_p=0.8,
    repetition_penalty=1.1
)

class Model:
    def __init__(
            self,
            model_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
            max_new_tokens=512,
            temperature=0.7,
            top_k=250,
            top_p=0.7,
            repetition_penalty=1.1
    ):
        self.model_id = model_id
        self.max_new_tokens = max_new_tokens
        self.temperature=temperature
        self.top_k = top_k
        self.top_p = top_p
        self.repetition_penalty = repetition_penalty

        self.model = self._initialize_model()

    def _initialize_model(self):
        try:
            model = HuggingFaceEndpoint(
                model=self.model_id,
                huggingfacehub_api_token=os.getenv("HF_API"),
                max_new_tokens=self.max_new_tokens,
                temperature=self.temperature,
                top_k=self.top_k,
                top_p=self.top_p,
                repetition_penalty=self.repetition_penalty
            )
            return model
        except Exception as e:
            print(f"Ошибка иницилизации модели: {e}")
            return None
        
    def generate(self, prompt, **kwargs):
        if not self.model:
            raise ValueError("Модель не иницилизирована")
        
        generation_params = {
            'max_new_tokens': self.max_new_tokens,
            'temperature': self.temperature,
            'top_k': self.top_k,
            'top_p': self.top_p,
            'repetition_penalty': self.repetition_penalty
        }
        generation_params.update(kwargs=kwargs)

        cur_model = HuggingFaceEndpoint(
            model=self.model_id,
            huggingfacehub_api_token=os.getenv("HF_API"),
            **generation_params
        )
        return cur_model.invoke(prompt)