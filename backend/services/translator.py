from googletrans import Translator
import json

class TranslatorService:
    def __init__(self, source='en', target='zh-cn'):
        self.translator = Translator()
        self.source = source
        self.target = target

    def translate(self, data):
        trans_data = {}
        for topic, content in data.items():
            content_trans = []
            for i in content:
                try:
                    result = self.translator.translate(i, src=self.source, dest=self.target)
                    content_trans.append(result.text)
                except Exception as e:
                    print(f"Error translating: {i[:30]}... -> {e}")
                    content_trans.append(i)
            trans_data[topic] = content_trans
        return json.dumps(trans_data, indent=2, ensure_ascii=False)
