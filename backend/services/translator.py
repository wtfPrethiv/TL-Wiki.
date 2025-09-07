from deep_translator import GoogleTranslator

class TranslatorService:
    
    def __init__(self, source='en', target='zh-CN'):
        self.source = source
        self.target = target
        self.translator = GoogleTranslator(source=self.source, target=self.target)
        self.max_chars = 5000  # Google Translate limit

    def chunk_text(self, text: str):
        chunks = []
        while len(text) > self.max_chars:
            split_at = text.rfind(" ", 0, self.max_chars)
            if split_at == -1:
                split_at = self.max_chars
            chunks.append(text[:split_at])
            text = text[split_at:].lstrip()
        if text:
            chunks.append(text)
        return chunks

    def translate(self, data: dict) -> dict:
        trans_data = {}
        for topic, content in data.items():
            content_trans = []
            for i in content:
                try:
                    chunks = self.chunk_text(i)
                    translated_chunks = [self.translator.translate(c) for c in chunks]
                    result = " ".join(translated_chunks)
                    content_trans.append(result)
                except Exception as e:
                    print(f"Error translating: {i[:30]}... -> {e}")
                    content_trans.append(i)
            trans_data[topic] = content_trans
        return trans_data
