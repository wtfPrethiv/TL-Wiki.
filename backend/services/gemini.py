from google import genai
import json

class Gemini:
    @staticmethod
    
    def ai_summarize(wiki_content):
        GEMINI_API_KEY = "YOUR GEMINI API KEY HERE"
        
        client = genai.Client(api_key=GEMINI_API_KEY)
        summary = {}
        for topic,content in wiki_content.items():
            
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"""
                            You are a Wikipedia summarizer.

                            Task:
                            
                            - Summarize the following content clearly and concisely.
                            - Focus on the most important facts and information.
                            - Do not add opinions or irrelevant details.
                            - Keep it short but informative.
                            - Do not include raw formatting characters such as '\\n', '*', '-', or bullet points.
                            - The final output should be plain sentences/paragraphs only.

                            Content:
                            
                            {topic}:{content}
                            
                            """
            )
            
            summary[topic] = response
            
        try:
            summary_text = response.candidates[0].content.parts[0].text
        except Exception:
            summary_text = str(response)

 

        return summary
