import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from config import OpenAISettings
from prompts import LINKDIEN_POSTER_PROMPT, SYSTEM_PROMPT

load_dotenv()

class LinkedInPostGenerator:
    def __init__(self):
        try:
            self.client = AzureOpenAI(
                azure_endpoint=OpenAISettings.azure_endpoint,
                azure_deployment=OpenAISettings.azure_deployment,
                api_version=OpenAISettings.api_version,
                api_key=OpenAISettings.api_key
            )
        except Exception as ex:
            print(f"[LinkedInPostGenerator] Initialization Exception: {ex}")

    def generate_post(self, article_summary: str, perspectives: list) -> dict:
        try:
            perspectives_text = '\n'.join([f"- {p}" for p in perspectives])
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content":SYSTEM_PROMPT},
                    {"role": "user", "content": LINKDIEN_POSTER_PROMPT.format(article_summary=article_summary,perspectives_text=perspectives_text)}
                ],
                n=1,
                temperature=0.4
            )

            content = response.choices[0].message.content.strip()
            if "Confidence Score:" in content:
                post_text, confidence = content.rsplit("Confidence Score:", 1)
                return {
                    "linkedin_post": post_text.strip(),
                    "confidence_score": int(confidence.strip())
                }
            else:
                return {
                    "linkedin_post": content,
                    "confidence_score": None
                }
        except Exception as ex:
            print(f"[LinkedInPostGenerator] Error generating post: {ex}")
            return {"linkedin_post": None, "confidence_score": None}

# Example Usage
