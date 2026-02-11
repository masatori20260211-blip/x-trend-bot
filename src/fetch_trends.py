#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
トレンド取得モジュール
"""

import tweepy
import sys
import os

# 親ディレクトリをパスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.config import (
    API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET,
    INVESTMENT_KEYWORDS, JAPAN_WOEID
)
from src.logger import get_logger

logger = get_logger(__name__)

class TrendFetcher:
    """トレンド取得クラス"""
    
    def __init__(self):
        """初期化"""
        try:
            self.client = tweepy.Client(
                consumer_key=API_KEY,
                consumer_secret=API_SECRET,
                access_token=ACCESS_TOKEN,
                access_token_secret=ACCESS_SECRET
            )
            logger.info("✅ X API認証成功")
        except Exception as e:
            logger.error(f"❌ 認証エラー: {e}")
            raise
    
    def fetch_trends(self):
        """日本のトレンドを取得"""
        try:
            # Twitter API v1.1を使用（v2ではトレンド取得が未対応）
            auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
            auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
            api = tweepy.API(auth)
            
            trends_result = api.get_place_trends(JAPAN_WOEID)
            trends = trends_result[0]['trends']
            
            logger.info(f"📊 トレンド取得成功: {len(trends)}件")
            return trends
        except Exception as e:
            logger.error(f"❌ トレンド取得エラー: {e}")
            return []
    
    def filter_investment_trends(self, trends):
        """投資系トレンドをフィルタリング"""
        investment_trends = []
        
        for trend in trends:
            name = trend['name']
            # キーワードマッチング
            for keyword in INVESTMENT_KEYWORDS:
                if keyword.lower() in name.lower():
                    investment_trends.append(trend)
                    logger.debug(f"✅ 投資系トレンド発見: {name}")
                    break
        
        logger.info(f"💰 投資系トレンド: {len(investment_trends)}件")
        return investment_trends
    
    def get_top_investment_trends(self, max_count=5):
        """上位の投資系トレンドを取得"""
        all_trends = self.fetch_trends()
        if not all_trends:
            return []
        
        investment_trends = self.filter_investment_trends(all_trends)
        
        # ツイート数でソート（ツイート数がない場合は最後に）
        sorted_trends = sorted(
            investment_trends,
            key=lambda x: x.get('tweet_volume') or 0,
            reverse=True
        )
        
        top_trends = sorted_trends[:max_count]
        
        logger.info(f"🔝 上位{len(top_trends)}件の投資系トレンドを取得")
        for i, trend in enumerate(top_trends, 1):
            volume = trend.get('tweet_volume', '不明')
            logger.info(f"  {i}. {trend['name']} (ツイート数: {volume})")
        
        return top_trends


if __name__ == "__main__":
    # テスト実行
    fetcher = TrendFetcher()
    trends = fetcher.get_top_investment_trends()
    
    print("\n" + "="*50)
    print("📈 投資系トレンド（上位5件）")
    print("="*50)
    
    for i, trend in enumerate(trends, 1):
        print(f"\n{i}. {trend['name']}")
        volume = trend.get('tweet_volume')
        if volume:
            print(f"   ツイート数: {volume:,}")
        if trend.get('url'):
            print(f"   URL: {trend['url']}")
