#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
設定ファイル読み込み
"""

import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込み
load_dotenv()

# X API認証情報
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

# 投資系キーワードリスト
INVESTMENT_KEYWORDS = [
    # 株式・市場
    '株', '株価', '日経', 'TOPIX', 'マザーズ', 'グロース', '東証',
    '株式', '銘柄', '相場', '暴落', '急騰', '上場', 'IPO', 'ストップ高',
    'ストップ安', '売買代金', '出来高', 'PER', 'PBR', 'ROE',
    
    # 投資一般
    '投資', '投資家', '資産運用', 'ポートフォリオ', '配当', '利回り',
    '投資信託', 'NISA', 'iDeCo', '積立', '分散投資', 'リスク管理',
    'インデックス', 'アクティブ', '投信',
    
    # 仮想通貨
    'ビットコイン', 'BTC', 'イーサリアム', 'ETH', '仮想通貨', '暗号資産',
    'リップル', 'XRP', 'crypto', 'アルトコイン', 'NFT', 'web3',
    'ブロックチェーン', 'DeFi', 'DAO', 'メタバース', 'ステーブルコイン',
    'マイニング', 'ウォレット', '取引所',
    
    # FX・為替
    'FX', '為替', 'ドル円', 'ユーロ', '円安', '円高', '外貨', '通貨',
    'スワップ', 'レバレッジ', 'スプレッド', 'pips',
    
    # 経済指標
    '金利', '利上げ', '利下げ', 'GDP', 'CPI', 'インフレ', 'デフレ',
    '雇用統計', '日銀', 'FRB', 'Fed', 'FOMC', '金融政策', '量的緩和',
    'テーパリング', 'YCC', '政策金利', '消費者物価', '景気',
    
    # 企業・経済
    '決算', '業績', '四半期', '営業利益', '純利益', '売上高', 'EPS',
    'M&A', '合併', '買収', 'IR', '株主総会', '増配', '減配', '自社株買い',
    '増資', '株式分割', '企業価値',
    
    # その他金融
    '債券', '国債', '社債', '金', 'ゴールド', '原油', '商品先物',
    '不動産', 'REIT', 'ファンド', 'ヘッジファンド', 'ETF', 'インフレ連動債',
    
    # 市場イベント
    '配当落ち', '権利確定', 'SQ', 'MSCI', 'オプション', '先物',
    
    # 投資家・著名人
    'バフェット', 'ソロス', '個人投資家', '機関投資家', 'アナリスト',
    
    # その他
    '資産', '財テク', '節税', '確定申告', '損益通算', 'ロスカット',
    'ナンピン', '押し目買い', '利確', '損切り'
]

# 日本のWOEID（Where On Earth ID）
JAPAN_WOEID = 23424856

# 投稿設定
MAX_TRENDS_TO_POST = int(os.getenv('MAX_TRENDS_TO_POST', '5'))
DRY_RUN = os.getenv('DRY_RUN', 'false').lower() == 'true'

def validate_config():
    """設定の検証"""
    if not all([API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET]):
        raise ValueError("認証情報が設定されていません。.envファイルを確認してください。")
    return True
