"""保険コンパス - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "保険コンパス"
BLOG_DESCRIPTION = "生命保険・医療保険・自動車保険・地震保険を年代別に徹底比較。保険スクエアbang!・保険見直しラボ等の無料相談も解説、最適な保険選びを支援。"
BLOG_URL = "https://musclelove-777.github.io/hoken-compass/"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/hoken-compass"

TARGET_CATEGORIES = [
    "生命保険の選び方",
    "医療保険・がん保険",
    "自動車保険比較",
    "地震・火災保険",
    "学資・年金保険",
    "ペット保険",
    "保険見直し・乗り換え",
    "年代別おすすめプラン",
]

THEME = {
    "primary": "#264653",
    "accent": "#2a9d8f",
    "gradient_start": "#264653",
    "gradient_end": "#2a9d8f",
}

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_FALLBACK_MODEL = "gemini-2.5-flash-lite"

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

MAX_ARTICLE_LENGTH = 4000
SEO_KEYWORD_DENSITY = 0.02
