from deep_translator import GoogleTranslator
import json

class TranslatorService:
    def __init__(self, source='en', target='zh-CN'):
        self.source = source
        self.target = target
        self.translator = GoogleTranslator(source=self.source, target=self.target)

    def translate(self, data: dict) -> str:
        trans_data = {}
        for topic, content in data.items():
            content_trans = []
            for i in content:
                try:
                    result = self.translator.translate(i)
                    content_trans.append(result)
                except Exception as e:
                    print(f"Error translating: {i[:30]}... -> {e}")
                    content_trans.append(i)  # fallback to original
            trans_data[topic] = content_trans
        return trans_data
