#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
投稿文生成モジュール
"""

import random
from datetime import datetime

class TweetGenerator:
    """投稿文生成クラス"""
    
    # 投稿テンプレート
    TEMPLATES = [
        "📊 今注目の投資トレンド\n\n{trends}\n\n#投資 #トレンド #{timestamp}",
        "💰 投資家が注目しているトピック\n\n{trends}\n\n#資産運用 #投資情報 #{timestamp}",
        "🔥 いま話題の投資関連ワード\n\n{trends}\n\n#株式投資 #仮想通貨 #{timestamp}",
        "📈 投資系トレンドランキング\n\n{trends}\n\n#マーケット #投資 #{timestamp}",
        "⚡️ リアルタイム投資トレンド\n\n{trends}\n\n#金融 #投資家 #{timestamp}",
    ]
    
    # 絵文字リスト
    EMOJIS = ['📊', '💰', '📈', '💹', '🔥', '⚡️', '💎', '🚀', '📉', '💵']
    
    def __init__(self):
        """初期化"""
        pass
    
    def generate_tweet(self, trends, max_length=280):
        """
        投稿文を生成
        
        Args:
            trends: トレンドのリスト
            max_length: 最大文字数
            
        Returns:
            投稿文
        """
        if not trends:
            return None
        
        # タイムスタンプ（ハッシュタグ用）
        timestamp = datetime.now().strftime("%m%d")
        
        # トレンドリストを文字列に変換
        trend_lines = []
        for i, trend in enumerate(trends, 1):
            name = trend['name']
            volume = trend.get('tweet_volume')
            
            # 絵文字をランダムに選択
            emoji = random.choice(self.EMOJIS)
            
            if volume:
                line = f"{emoji} {name} ({volume:,}ツイート)"
            else:
                line = f"{emoji} {name}"
            
            trend_lines.append(line)
        
        trends_text = "\n".join(trend_lines)
        
        # テンプレートをランダムに選択
        template = random.choice(self.TEMPLATES)
        
        # 投稿文を生成
        tweet = template.format(
            trends=trends_text,
            timestamp=timestamp
        )
        
        # 文字数チェック
        if len(tweet) > max_length:
            # 長すぎる場合はトレンド数を減らす
            return self.generate_tweet(trends[:-1], max_length)
        
        return tweet
    
    def generate_simple_tweet(self, trends):
        """
        シンプルな投稿文を生成
        
        Args:
            trends: トレンドのリスト
            
        Returns:
            投稿文
        """
        if not trends:
            return None
        
        lines = ["📊 投資系トレンド\n"]
        
        for i, trend in enumerate(trends[:5], 1):
            name = trend['name']
            volume = trend.get('tweet_volume')
            
            if volume:
                lines.append(f"{i}. {name} ({volume:,})")
            else:
                lines.append(f"{i}. {name}")
        
        lines.append("\n#投資 #トレンド")
        
        return "\n".join(lines)
    
    def generate_detailed_tweet(self, trend):
        """
        個別トレンドの詳細投稿文を生成
        
        Args:
            trend: 単一のトレンド
            
        Returns:
            投稿文
        """
        name = trend['name']
        volume = trend.get('tweet_volume')
        url = trend.get('url', '')
        
        if volume:
            tweet = f"🔥 いま話題: {name}\n\n💬 {volume:,}件のツイート\n\n"
        else:
            tweet = f"🔥 いま話題: {name}\n\n"
        
        tweet += "#投資 #トレンド #マーケット"
        
        return tweet


if __name__ == "__main__":
    # テスト実行
    test_trends = [
        {'name': 'ビットコイン', 'tweet_volume': 12450},
        {'name': '日経平均', 'tweet_volume': 8230},
        {'name': '円安', 'tweet_volume': 15680},
        {'name': 'NISA', 'tweet_volume': 5420},
        {'name': '金利', 'tweet_volume': None},
    ]
    
    generator = TweetGenerator()
    
    print("="*50)
    print("📝 投稿文生成テスト")
    print("="*50)
    
    print("\n【パターン1: ランダムテンプレート】")
    tweet1 = generator.generate_tweet(test_trends)
    print(tweet1)
    print(f"\n文字数: {len(tweet1)}")
    
    print("\n" + "="*50)
    print("【パターン2: シンプル】")
    tweet2 = generator.generate_simple_tweet(test_trends)
    print(tweet2)
    print(f"\n文字数: {len(tweet2)}")
    
    print("\n" + "="*50)
    print("【パターン3: 個別詳細】")
    tweet3 = generator.generate_detailed_tweet(test_trends[0])
    print(tweet3)
    print(f"\n文字数: {len(tweet3)}")
