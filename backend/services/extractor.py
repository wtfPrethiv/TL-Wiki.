class Extractor:
    def __init__(self, gemini_response):
        self.data = gemini_response
    
    def extract(self) -> dict:
        extracted = {}
        for section, response_obj in self.data.items():
            try:
                candidates = getattr(response_obj, "candidates", [])
                if not candidates:
                    continue

                first_candidate = candidates[0]
                content = getattr(first_candidate, "content", None)
                if not content:
                    continue

                parts = getattr(content, "parts", [])
                if not parts:
                    continue

                first_part = parts[0]
                text = getattr(first_part, "text", None)
                if text:
                    extracted[section] = text.strip()

            except Exception as e:
                print(f"Skipping {section} due to error: {e}")

        return extracted