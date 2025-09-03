from fastapi import APIRouter
from backend.services import Gemini, Scraper, TranslatorService
from backend.models import WikiInput

router = APIRouter()

@router.post("/summarize")
def summarize(topic: WikiInput):
    scraper = Scraper()
    
    wiki_content = scraper.scrape(topic.topic)
    
    trans_zh = TranslatorService(source='en', target='zh-CN')
    content_zh = trans_zh.translate(wiki_content)
    
    gemini = Gemini()
    summarized_content = gemini.ai_summarize(content_zh)
    
    trans_en = TranslatorService(source='zh-CN', target='en')
    summary_en = trans_en.translate(summarized_content)
    
    return {"summary": summary_en}