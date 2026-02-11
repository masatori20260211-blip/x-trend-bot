#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
メイン実行スクリプト - トレンド取得から投稿までの完全フロー
"""

import sys
import os

# 親ディレクトリをパスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.config import MAX_TRENDS_TO_POST, validate_config
from src.fetch_trends import TrendFetcher
from src.generate_tweet import TweetGenerator
from src.post_tweet import TweetPoster
from src.logger import get_logger

logger = get_logger(__name__)

def main():
    """メイン処理"""
    logger.info("="*50)
    logger.info("🚀 X投資系トレンドBotを起動")
    logger.info("="*50)
    
    try:
        # 設定の検証
        validate_config()
        logger.info("✅ 設定の検証完了")
        
        # ステップ1: トレンド取得
        logger.info("\n📊 ステップ1: トレンド取得中...")
        fetcher = TrendFetcher()
        trends = fetcher.get_top_investment_trends(max_count=MAX_TRENDS_TO_POST)
        
        if not trends:
            logger.warning("⚠️ 投資系トレンドが見つかりませんでした")
            return False
        
        logger.info(f"✅ {len(trends)}件の投資系トレンドを取得")
        
        # ステップ2: 投稿文生成
        logger.info("\n📝 ステップ2: 投稿文生成中...")
        generator = TweetGenerator()
        tweet_text = generator.generate_tweet(trends)
        
        if not tweet_text:
            logger.error("❌ 投稿文の生成に失敗しました")
            return False
        
        logger.info(f"✅ 投稿文生成完了（{len(tweet_text)}文字）")
        logger.info(f"\n投稿内容:\n{'-'*50}\n{tweet_text}\n{'-'*50}")
        
        # ステップ3: 投稿実行
        logger.info("\n📤 ステップ3: 投稿実行中...")
        poster = TweetPoster()
        result = poster.safe_post_tweet(tweet_text)
        
        if result:
            logger.info("✅ 投稿成功！")
            logger.info("="*50)
            logger.info("🎉 処理完了")
            logger.info("="*50)
            return True
        else:
            logger.error("❌ 投稿失敗")
            return False
            
    except Exception as e:
        logger.error(f"❌ エラーが発生しました: {e}", exc_info=True)
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
