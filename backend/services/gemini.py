from google import genai
import json

class Gemini:
    @staticmethod
    
    def ai_summarize(wiki_content):
        GEMINI_API_KEY = "AIzaSyA6Cp5XEjka65SzuljCfLKAMVuPfvK9yxk"
        
        client = genai.Client(api_key=GEMINI_API_KEY)
        summary = {}
        for topic,content in wiki_content.items():
            
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"""
                            You are a Wikipedia summarizer.

                            Task:
                            - Summarize the following content clearly and concisely.
                            - The summary should be written in Chinese.
                            - Focus on the most important facts and information.
                            - Do not add opinions or irrelevant details.
                            - Keep it short but informative.

                            Content:
                            {topic}:{content}
                            
                            """
            )
            
            summary[topic] = response
            
        try:
            summary_text = response.candidates[0].content.parts[0].text
        except Exception:
            summary_text = str(response)  # fallback if structure changes

 

        return summary
