"""Build all wiki pages from content definitions."""
import os

OUT = r'D:\yuzucity-wiki'

def page(slug, title, icon, subtitle, body, breadcrumb=None):
    crumb = ''
    if breadcrumb:
        crumb_items = ['<a href="index.html">🏙️ ホーム</a>']
        for label in breadcrumb:
            crumb_items.append('<span class="breadcrumb-sep">›</span>')
            crumb_items.append(f'<span>{label}</span>')
        crumb = f'<nav class="breadcrumb">{"".join(crumb_items)}</nav>'

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Yuzu City Wiki</title>
<link rel="stylesheet" href="styles.css">
</head>
<body data-page="{slug}">
<header class="topbar" id="topbar"></header>
<div class="app">
  <aside class="sidebar" id="sidebar"></aside>
  <main>
    {crumb}
    <section>
      <div class="section-header">
        <h1 class="section-title"><span class="section-title-icon">{icon}</span>{title}</h1>
        <p class="section-subtitle">{subtitle}</p>
      </div>
      {body}
    </section>
    <div id="pageNav"></div>
  </main>
</div>
<footer>
  🍋 <strong>Yuzu City Wiki</strong> · 非公式ガイド &nbsp;|&nbsp;
  <a href="https://x.com/yuzu_server" target="_blank">𝕏 @yuzu_server</a> ·
  <a href="https://discord.gg/gHCeUWFyyc" target="_blank">Discord</a>
</footer>
<script src="common.js"></script>
</body>
</html>"""


def home_page():
    body = """
<div class="hero large">
  <div class="hero-content">
    <div class="hero-icon">🍋</div>
    <h1 class="hero-title">YUZU CITY</h1>
    <p class="hero-subtitle">『あったらいいなこんなもの。』を叶える街</p>
    <span class="hero-tagline">FiveM ロールプレイサーバー · 2026年5月1日 OPEN</span>
  </div>
</div>

<div class="card" style="background:linear-gradient(135deg,rgba(244,196,48,.08),rgba(74,222,128,.05));margin-top:2rem;">
  <h3 class="card-title">🍋 サーバー紹介</h3>
  <p>『あったらいいなこんなもの。』を叶える街。自作スクリプト多数、初心者から上級者まで不便なく楽しめる街を目指しています。
    職業RPを中心とし、警察・救急・整備士・飲食店・ギャングなど、それぞれの役割を演じながら生活していきます。
  </p>
</div>

<div class="stats">
  <div class="stat"><div class="stat-num">17:00〜3:00</div><div class="stat-label">街の開放時間</div></div>
  <div class="stat"><div class="stat-num">19:00〜0:00</div><div class="stat-label">運営対応時間</div></div>
  <div class="stat"><div class="stat-num">20:00 / 1:00</div><div class="stat-label">サーバー再起動</div></div>
  <div class="stat"><div class="stat-num">面接制</div><div class="stat-label">入国審査</div></div>
</div>

<div class="notice notice-info">
  <div class="notice-title">ℹ️ サーバー接続について</div>
  運営の入国面接を通過した方のみ街に参加可能です。接続情報は審査通過後にDiscord内でご案内されます。
</div>

<h2 style="margin:2rem 0 1rem;font-size:1.4rem;">🔧 主な特徴</h2>
<div class="card-grid">
  <div class="card"><div class="card-title">🎭 職業RP中心</div><p>警察(PD) / 救急(EMS) / 個人医 / メカニック / 飲食店 / ギャングなど多彩な職業</p></div>
  <div class="card"><div class="card-title">💻 自作スクリプト多数</div><p>独自開発のシステムによる差別化されたゲームプレイ体験</p></div>
  <div class="card"><div class="card-title">👥 初心者歓迎</div><p>RP経験者から初めての方まで、幅広く参加可能</p></div>
  <div class="card"><div class="card-title">🤝 交流重視</div><p>身内固まりすぎを抑制し、新しい交流やストーリー作りを推奨</p></div>
</div>

<h2 style="margin:2rem 0 1rem;font-size:1.4rem;">📋 みんなで楽しく遊ぶために</h2>
<div class="card">
  <ul class="styled-list">
    <li>モラルを持った行動を心がけましょう</li>
    <li>相手のRPを壊す行動は控えましょう</li>
    <li>ルールは事前に確認しましょう</li>
    <li>暴言・煽り・迷惑行為はやめましょう</li>
  </ul>
</div>

<h2 style="margin:2rem 0 1rem;font-size:1.4rem;">📚 wiki カテゴリ</h2>
<div class="card-grid">
  <a href="guide.html" class="card" style="text-decoration:none;color:inherit;"><div class="card-title">📖 初心者ガイド</div><p style="color:var(--text-dim);">マイク設定・キー配置・緊急時対応など基本操作</p></a>
  <a href="commands.html" class="card" style="text-decoration:none;color:inherit;"><div class="card-title">⌨️ コマンド一覧</div><p style="color:var(--text-dim);">/name、/911、/help など14種類のコマンド</p></a>
  <a href="terms.html" class="card" style="text-decoration:none;color:inherit;"><div class="card-title">💬 配信用語集</div><p style="color:var(--text-dim);">衛星=配信、瞑想=再起動など隠語16種</p></a>
  <a href="rules-general.html" class="card" style="text-decoration:none;color:inherit;"><div class="card-title">📜 一般ルール</div><p style="color:var(--text-dim);">RMT・MOD・チート・ゴースティング等の禁止事項</p></a>
  <a href="rules-combat.html" class="card" style="text-decoration:none;color:inherit;"><div class="card-title">⚔️ 戦闘ルール</div><p style="color:var(--text-dim);">RDM・Combat log・ドライブバイ・無線撃ちなど</p></a>
  <a href="rules-vehicle.html" class="card" style="text-decoration:none;color:inherit;"><div class="card-title">🚗 車両ルール</div><p style="color:var(--text-dim);">禁止車両・禁止カスタム・窃盗禁止</p></a>
  <a href="job-pd.html" class="card" style="text-decoration:none;color:inherit;"><div class="card-title">🚓 警察 (PD)</div><p style="color:var(--text-dim);">対応手順・MDT記入・強盗ペナルティ表など</p></a>
  <a href="job-ems.html" class="card" style="text-decoration:none;color:inherit;"><div class="card-title">🚑 EMS（救急）</div><p style="color:var(--text-dim);">事件対応・物資管理・治療費ルール</p></a>
  <a href="job-doctor.html" class="card" style="text-decoration:none;color:inherit;"><div class="card-title">⚕️ 個人医</div><p style="color:var(--text-dim);">闇医者の業務範囲・治療料金・参加可能犯罪</p></a>
  <a href="job-mechanic.html" class="card" style="text-decoration:none;color:inherit;"><div class="card-title">🔧 メカニック</div><p style="color:var(--text-dim);">修理・部品料金表（27項目）</p></a>
  <a href="job-food.html" class="card" style="text-decoration:none;color:inherit;"><div class="card-title">🍔 飲食店</div><p style="color:var(--text-dim);">商品登録・値段ルール・開業条件</p></a>
  <a href="job-crime.html" class="card" style="text-decoration:none;color:inherit;"><div class="card-title">💀 犯罪ルール</div><p style="color:var(--text-dim);">人質・受注・利確・歪み対応など</p></a>
  <a href="news.html" class="card" style="text-decoration:none;color:inherit;"><div class="card-title">📢 お知らせ</div><p style="color:var(--text-dim);">最新情報・ルール改定タイムライン</p></a>
  <a href="updates.html" class="card" style="text-decoration:none;color:inherit;"><div class="card-title">🔄 機能変更</div><p style="color:var(--text-dim);">サーバー機能のアップデート履歴</p></a>
  <a href="streams.html" class="card" style="text-decoration:none;color:inherit;"><div class="card-title">📺 配信中</div><p style="color:var(--text-dim);">住民のTwitch・YouTube配信状況</p></a>
  <a href="socials.html" class="card" style="text-decoration:none;color:inherit;"><div class="card-title">𝕏 住民SNS</div><p style="color:var(--text-dim);">住民のX(Twitter)アカウント一覧</p></a>
  <a href="dealer.html" class="card" style="text-decoration:none;color:inherit;"><div class="card-title">🚗 ディーラー</div><p style="color:var(--text-dim);">街で購入可能な車両・バイク・航空機・ボート</p></a>
  <a href="icarus.html" class="card" style="text-decoration:none;color:inherit;"><div class="card-title">🍰 Icarus</div><p style="color:var(--text-dim);">食べ物・飲み物メニュー</p></a>
</div>
"""
    return page('index', '街の概要', '🏙️',
                'Yuzu City は職業RPを中心にしたFiveMロールプレイサーバーです', body)


def guide_page():
    body = """
<h2 style="margin:1rem 0;font-size:1.2rem;">🎤 マイク・音声</h2>
<div class="card"><p><strong>マイクの設定：</strong>声が聞こえないようならDiscord内VCを使用してレクチャーしてもらってもOK。</p></div>
<div class="card">
  <p><strong>声の大きさ切替：</strong>半角キー（<code>/</code>）で5段階を切替（初期キー）</p>
  <table style="margin-top:.8rem;">
    <tr><td>Mute</td><td>声なし</td></tr>
    <tr><td>Whisper</td><td>ささやき声</td></tr>
    <tr><td>Normal</td><td>普通の声</td></tr>
    <tr><td>Shouting</td><td>大声</td></tr>
    <tr><td>Super Shouting</td><td>超大声</td></tr>
  </table>
</div>

<h2 style="margin:2rem 0 1rem;font-size:1.2rem;">🎛️ よく使うキー</h2>
<div class="notice">⚠️ 初期キーは使いにくい場合が多いので、キーの設定は経験者に聞いてみよう。サーバーで変更可能なため要確認。</div>
<div class="cmd-item"><span class="cmd-name">Tab</span><span class="cmd-desc">インベントリを開く</span></div>
<div class="cmd-item"><span class="cmd-name">F2</span><span class="cmd-desc">セカンダリーバッグ</span></div>
<div class="cmd-item"><span class="cmd-name">M</span><span class="cmd-desc">スマホを開く</span></div>
<div class="cmd-item"><span class="cmd-name">@</span><span class="cmd-desc">声ボリューム切替</span></div>
<div class="cmd-item"><span class="cmd-name">I</span><span class="cmd-desc">UI設定（ミニマップや体力ゲージの見え方変更）</span></div>
<div class="cmd-item"><span class="cmd-name">特定キー</span><span class="cmd-desc">パルクール（乗り越え）※サーバーごとに異なる</span></div>

<h2 style="margin:2rem 0 1rem;font-size:1.2rem;">📱 携帯アプリ</h2>
<div class="card-grid">
  <div class="card"><div class="card-title">SNS</div>Twitter風アプリ</div>
  <div class="card"><div class="card-title">STATE</div>お店の出勤状態がわかる</div>
  <div class="card"><div class="card-title">イエローページ</div>連絡先一覧</div>
  <div class="card"><div class="card-title">ダークチャット</div>※犯罪RP向け</div>
</div>
<div class="notice notice-warning">⚡ 犯罪・ギャング情報は絶対に口外しないようにしてください。</div>

<h2 style="margin:2rem 0 1rem;font-size:1.2rem;">🚨 緊急時の対応</h2>
<div class="card">
  <h4 style="color:var(--leaf);margin-bottom:.5rem;">ダウン時（一般）</h4>
  <p>救急隊が出勤しているなら <code>Gキー長押し</code> ／ いない時は <code>/help</code> で NPCドクターが起こしに来てくれる🏥</p>
</div>
<div class="card">
  <h4 style="color:var(--danger);margin-bottom:.5rem;">ダウン時（犯罪シーン中）</h4>
  <p><code>Hキー長押し</code> で個人医（闇医者）を呼ぼう！</p>
</div>

<h2 style="margin:2rem 0 1rem;font-size:1.2rem;">📻 その他の便利機能</h2>
<div class="card-grid">
  <div class="card"><div class="card-title">📻 ラジオの使い方</div>無線機を購入 → 周波数合わせる → 通話可能！無線機はコンビニで購入可。</div>
  <div class="card"><div class="card-title">⛽ ガソリンの入れ方</div>ガソリンスタンドで給油可能。ジェリ缶所持なら、車近くで補充可能。</div>
  <div class="card"><div class="card-title">🚗 車横転の復帰</div><code>/flipvehicle</code> で車を元に戻せます。</div>
  <div class="card"><div class="card-title">🏷️ 名前の設定・変更</div><code>/name</code> で変更可能。基本的に犯罪中以外は名前表示推奨。</div>
</div>
"""
    return page('guide', '初心者ガイド', '📖',
                'これだけ覚えれば安心！基本操作と便利機能',
                body, breadcrumb=['初心者ガイド'])


def commands_page():
    cmds = [
        ('/name', '周りから自分の名前を非表示にできる'),
        ('/map [番地]', '指定の番地に自動でマッピング'),
        ('/givekeys [ID]', '近くまたは指定プレイヤーに車のキーを譲渡'),
        ('/311 [文章]', '死んだ状態でもEMSに連絡。ダウン者を病院へ運ぶ際に使用'),
        ('/911 [文章]', '死んだ状態でも警察に連絡。強盗が歪んだ際に使用'),
        ('/411 [文章]', '死んだ状態でも個人医に連絡'),
        ('/help', '救急隊が少ない場合ポンコツ医者を呼ぶ'),
        ('/dice [1〜5]', 'サイコロを1〜5個振る'),
        ('/rps [1〜3]', 'グーチョキパー'),
        ('/preview', '乗車中に車両の外装カスタム一覧を一時閲覧'),
        ('/checkveh', '近くの車両の性能パーツを確認'),
        ('/checkdamage', '近くの車両の損傷具合を確認'),
        ('/checkmods', '車両に搭載できる外装パーツの量を確認'),
        ('/flipvehicle', '横転した車両を元に戻す'),
    ]
    items = '\n'.join(
        f'<div class="cmd-item"><span class="cmd-name">{n}</span><span class="cmd-desc">{d}</span></div>'
        for n, d in cmds
    )
    return page('commands', 'コマンド一覧', '⌨️',
                '街で使える便利なコマンド集',
                items, breadcrumb=['コマンド一覧'])


def terms_page():
    terms = [
        ('衛星', '配信'),('喉', 'マイク'),('筋肉', 'キーボード'),('六法', 'Discord'),
        ('瞑想', '再起動'),('魂抜け', '離席'),('心無き', 'NPC'),('歪み', 'バグ'),
        ('夢の世界', '現実'),('白市民', '犯罪をしない人や警察'),
        ('黒市民', '犯罪者やギャング'),('観測者', '配信閲覧者'),
        ('心の目', 'スタッシュなどの中身を見るときに使うAltキー'),
        ('PD', '警察'),('EMS', '救急'),('法律', 'サーバールール'),
    ]
    items = '\n'.join(
        f'<div class="term-item"><span class="term-key">{k}</span><span class="term-arrow">→</span><span class="term-val">{v}</span></div>'
        for k, v in terms
    )
    body = f'<div class="term-grid">{items}</div>'
    return page('terms', '配信用語集', '💬',
                '配信者・視聴者の隠語・略称',
                body, breadcrumb=['配信用語集'])


def rule_item(rid, title, desc, pill_class='pill-danger', pill_label='違反'):
    return f'<div class="rule-item"><span class="rule-id">{rid}</span><div><div class="rule-title">{title}</div><div class="rule-desc">{desc}</div></div><span class="pill {pill_class}">{pill_label}</span></div>'


def rules_general_page():
    rules = [
        ('G-001', 'RMT（リアルマネートレード）禁止', '現実のお金を用いたアイテムの売買を禁止'),
        ('G-002', '視認性変更MODの使用禁止', 'Citizen、No Prop、No Water、Tracer、Bloodfx などのMODは一切禁止'),
        ('G-003', '高画質MODの使用禁止', 'NVE、reshade、QUANT V を含む高画質MOD全般の使用を禁止'),
        ('G-004', 'ROB行為の禁止', '他プレイヤーのインベントリ、車両などからアイテムを強奪する行為を禁止'),
        ('G-005', 'ゴースティング行為の禁止', '他の配信や通話での別視点などから外部情報を得る事を禁止'),
        ('G-006', 'チート・ツールの使用禁止', 'ゲームの仕様を不当に改変して有利になるプログラムや改造の使用を禁止'),
        ('G-007', 'レティクル表示の禁止', '外部ツール、ゲーム内のコマンドでのレティクル表示を禁止'),
        ('G-008', 'グリッチ・バグの悪用禁止', 'ゴーストピーク、スピードブースト、グリッチロールなどの使用を禁止。怪しいものは運営に確認', 'pill-warning', '警告→BAN'),
        ('G-009', 'ゲーム外VCの使用禁止', 'Discord などで通話を行った状態で街に入ることを禁止'),
        ('G-010', '無断DM・フレンド申請の禁止', '相手の同意なく Discord での個別連絡やフレンド申請を送る行為を禁止'),
        ('G-011', '全体チャットの使用禁止', '街のプレイヤー全員が見れるチャットの使用を禁止'),
        ('G-012', '違反発見時のクリップ提出義務', '禁止事項を行なっていたプレイヤーを発見した際は、原則クリップの提出を必須とする', 'pill-info', '手続き'),
    ]
    items = '\n'.join(rule_item(*r) for r in rules)
    return page('rules-general', '一般ルール', '📜',
                'サーバー全体に適用される基本ルール',
                items, breadcrumb=['ルール', '一般'])


def rules_rp_page():
    body = rule_item('RP-001', '手錠中のラジオ・アイテム使用禁止',
                     '手錠をかけられている状態で、ラジオやアイテムを使用する行為を禁止')
    return page('rules-rp', 'RPルール', '🎭',
                'ロールプレイ全般に関するルール',
                body, breadcrumb=['ルール', 'RP'])


def rules_combat_page():
    rules = [
        ('CB-001', 'RDM（ランダムデスマッチ）禁止', '無差別に他プレイヤーを殺す行為を禁止'),
        ('CB-002', 'Combat log 禁止', '意図的にゲームを切断する行為を禁止'),
        ('CB-003', 'ドライブバイ禁止', '車両に乗っている状態（トラックの荷台も含む）で銃を撃つ行為を禁止'),
        ('CB-004', '無線撃ち禁止', '戦闘中に無線を使用し、エモートで銃を隠しながら行動する行為を禁止'),
        ('CB-005', 'エモートによる所持品隠し禁止', '銃器や回復アイテムなどをエモートで不自然に隠す行為を禁止'),
    ]
    items = '\n'.join(rule_item(*r) for r in rules)
    return page('rules-combat', '戦闘・PvPルール', '⚔️',
                '戦闘行為に関するルール',
                items, breadcrumb=['ルール', '戦闘'])


def rules_vehicle_page():
    rules = [
        ('VH-001', '緊急車両・個人車両の窃盗禁止', '緊急車両（EMS、PDの車両）および個人車両の窃盗を禁止'),
        ('VH-002', '禁止車両',
         '防弾ガラス・防弾タイヤが装着されている車両、武装が標準搭載されている車両、殺傷能力を有する車両、飛行機能を有する車両の使用を禁止<br><span style="color:var(--text-muted);font-size:.8rem;">※耐弾性能のみの車両は対象外</span>'),
        ('VH-003', '禁止カスタム', '防弾ガラス化、武装追加、殺傷能力付与、爆発耐性追加カスタムを禁止'),
    ]
    items = '\n'.join(rule_item(*r) for r in rules)
    return page('rules-vehicle', '車両ルール', '🚗',
                '車両の使用・カスタムに関するルール',
                items, breadcrumb=['ルール', '車両'])


def rules_relationship_page():
    body = """
<div class="card-grid">
  <div class="card"><div class="card-title">🤝 相互同意が前提</div>必ずお互いの合意のもとで行うこと。一方的なアプローチや、相手が嫌がっているのに続ける行為は禁止。</div>
  <div class="card"><div class="card-title">🎭 OOC感情と混同しない</div>あくまでRP（演技）として楽しむ。現実の感情を持ち込む、相手にそれを求める行為は禁止。</div>
  <div class="card"><div class="card-title">🚫 関係強要の禁止</div>告白・交際・関係の進展などを無理に迫る行為は禁止。断られた場合はRPとしても受け入れる。</div>
  <div class="card"><div class="card-title">👥 他プレイヤーへの配慮</div>過度なイチャつき、周囲のRPを阻害する行為は控える。公共の場では節度ある行動を。</div>
</div>
<div class="notice notice-warning">
  <div class="notice-title">⚠️ 禁止事項</div>
  <ul style="margin:.5rem 0 0 1.2rem;">
    <li>相手の許可なくDMや外部連絡先を聞き出す行為</li>
    <li>恋愛RPを利用した執拗な付きまとい、ハラスメント行為</li>
    <li>関係を利用した晒し・嫌がらせ</li>
    <li>RPを理由にした現実への干渉行為</li>
  </ul>
</div>
<div class="notice notice-info">
  恋愛RPが原因でトラブルが発生した場合、個人間での解決を無理に行わず、必ずチケットを切り運営へ相談してください。
</div>
"""
    return page('rules-relationship', '恋愛RPの注意事項', '💕',
                '恋愛RPは禁止していません。トラブル防止のためルール遵守を',
                body, breadcrumb=['ルール', '恋愛RP'])


def job_pd_page():
    body = """
<div class="tab-group">
  <button class="tab active" onclick="showTab('pd',this,0)">基本</button>
  <button class="tab" onclick="showTab('pd',this,1)">犯罪シーン</button>
  <button class="tab" onclick="showTab('pd',this,2)">給料・昇格</button>
</div>

<div class="tab-content active" data-group="pd">
""" + '\n'.join([
        rule_item('PD-002', '車両カラー', 'パトカーは白黒のみ。パール色は自由', 'pill-info', '基本'),
        rule_item('PD-003', 'EMS到着前のPD対応', '倒れてから5分経過後に光を見るのはOK（EMSに拾われている場合は禁止）', 'pill-info', '基本'),
        rule_item('PD-004', '死亡時の対応', '死亡時は即EMSに通知。①死んだ場所から動かさない ②/311 犯罪名+正確な位置（屋上・海中など）', 'pill-info', '基本'),
        rule_item('PD-018', 'パトロール', 'パトロールあり（張り込み禁止）', 'pill-info', '基本'),
        rule_item('PD-021', 'NPC車両使用禁止', 'NPC車両使用禁止'),
        rule_item('PD-022', '汚職禁止', '押収品使用・横流し禁止'),
        rule_item('PD-023', 'ギャング抗争への介入不可', 'ギャング同士の抗争には警察介入不可', 'pill-info', '基本'),
        rule_item('PD-024', '市民事故対応', 'シーン中に市民と事故が起きた場合、犯罪者より市民を優先して修理費＋治療費を支払い、後で経費申請', 'pill-info', '基本'),
        rule_item('PD-029', 'MDT記入義務', '検挙時の必須記入：日付/時間/犯罪名/関わった警察官の名前/逮捕した犯人の名前', 'pill-info', '手続き'),
    ]) + """
</div>

<div class="tab-content" data-group="pd">
""" + '\n'.join([
        rule_item('PD-005', 'ヘリ使用制限', '大型3台 / 中型2台 / 小型使用不可', 'pill-warning', '条件'),
        rule_item('PD-006', '窓開け禁止', '走行中の窓開け禁止'),
        rule_item('PD-007', '先打ち禁止', '先打ち禁止（大型犯罪はOK）。人質なしの場合は発砲OK', 'pill-warning', '条件'),
        rule_item('PD-009', '軽強盗ルール', '共有ガレージ車両のみ使用可（犯罪車・スーパーカー禁止）', 'pill-info', '基本'),
        rule_item('PD-010', '準大型強盗ルール', 'ライオット or トランスポーター 1台まで', 'pill-info', '基本'),
        rule_item('PD-011', '大型強盗ルール', 'ライオット or トランスポーター 2台まで', 'pill-info', '基本'),
        rule_item('PD-012〜014', '人質交渉', '心あり：2分 or 30秒+カスタム ／ 心なし：1分 or 30秒+カスタム ／ 人質ありシーン中は犯罪者発砲禁止のためテーザー使用OK', 'pill-info', '基本'),
        rule_item('PD-015〜017', '通知コール', '1: 事故死 ／ 2: 近くに敵がいる ／ 3: 遠くへ行った', 'pill-info', '基本'),
        rule_item('PD-020', 'ゾンビアタック禁止', 'シーン中死亡→復帰不可。犯罪現場へ向かう途中の死亡も同様'),
        rule_item('PD-025', '犯罪開始時のタイマー', '犯罪タイマーが0になるまでに積極的に詰める動きを心がける', 'pill-info', '基本'),
    ]) + """
</div>

<div class="tab-content" data-group="pd">
""" + '\n'.join([
        rule_item('PD-026', '罰金分配', '罰金の半分は署長金庫、残りは現場参加人数で均等割り', 'pill-leaf', '給料'),
        rule_item('PD-027', 'ボーナス', '上層部がMDT確認後にボーナス支給。集計期間は日曜〜土曜、翌日曜以降に付与。検挙関与率が高いほど支給額UP', 'pill-leaf', '給料'),
        rule_item('PD-028', '昇格基準', '一定の検挙数を超え、上層部の判断により昇格', 'pill-info', '基本'),
    ]) + """
</div>

<h2 style="margin:2.5rem 0 1rem;font-size:1.3rem;">📋 強盗カテゴリ別ペナルティ表</h2>
<div class="table-wrap">
  <table>
    <thead><tr><th>カテゴリ</th><th>強盗</th><th>プリズン</th><th>罰金</th><th>インパウンド</th></tr></thead>
    <tbody>
      <tr><td><span class="pill pill-muted">特殊</span></td><td>npc強盗（PDきません）</td><td>なし</td><td>-</td><td>-</td></tr>
      <tr><td colspan="5" style="background:rgba(244,196,48,.04);font-weight:600;font-size:.85em;color:var(--yuzu);">軽強盗：犯罪者1〜2人 / 警察最低受注4人〜</td></tr>
      <tr><td><span class="pill pill-leaf">軽</span></td><td>boosting犯罪 (D,C,B)</td><td>なし</td><td>40万 / 60万 / 80万</td><td>20万・10分</td></tr>
      <tr><td><span class="pill pill-leaf">軽</span></td><td>コンビニ（撃ち合いなし）</td><td>なし</td><td>90万</td><td>20万・10分</td></tr>
      <tr><td><span class="pill pill-leaf">軽</span></td><td>墓荒らし</td><td>なし</td><td>50万</td><td>20万・10分</td></tr>
      <tr><td><span class="pill pill-leaf">軽</span></td><td>atm強盗</td><td>なし</td><td>20万</td><td>20万・10分</td></tr>
      <tr><td colspan="5" style="background:rgba(244,196,48,.04);font-weight:600;font-size:.85em;color:var(--yuzu);">中強盗（先撃ちOK）：犯罪者1〜5人 / 警察7人 / 最低受注6人〜</td></tr>
      <tr><td><span class="pill pill-warning">中</span></td><td>フリーカ強盗（撃ち合いなし）</td><td>10分</td><td>100万</td><td>20万・10分</td></tr>
      <tr><td><span class="pill pill-warning">中</span></td><td>サーマイト強盗</td><td>10分</td><td>160万</td><td>20万・10分</td></tr>
      <tr><td><span class="pill pill-warning">中</span></td><td>金庫強盗（撃ち合いなし）</td><td>10分</td><td>300万</td><td>20万・10分</td></tr>
      <tr><td><span class="pill pill-warning">中</span></td><td>砂漠強盗</td><td>10分</td><td>160万</td><td>20万・10分</td></tr>
      <tr><td><span class="pill pill-warning">中</span></td><td>宝石店強盗（人質なし）</td><td>10分</td><td>200万</td><td>20万・10分</td></tr>
      <tr><td><span class="pill pill-warning">中</span></td><td>ブースティング(A,S) ※4人まで</td><td>10分</td><td>1,000万</td><td>20万・10分</td></tr>
      <tr><td colspan="5" style="background:rgba(244,196,48,.04);font-weight:600;font-size:.85em;color:var(--yuzu);">準大型強盗：犯罪者5〜10人 / 警察13人 / 最低受注8人〜</td></tr>
      <tr><td><span class="pill pill-info">準大型</span></td><td>飛行機墜落</td><td>20分</td><td>700万</td><td>20万・20分</td></tr>
      <tr><td><span class="pill pill-info">準大型</span></td><td>客船強盗</td><td>20分</td><td>800万</td><td>20万・20分</td></tr>
      <tr><td><span class="pill pill-info">準大型</span></td><td>デラックス強盗（飛行場強盗）</td><td>20分</td><td>900万</td><td>20万・20分</td></tr>
      <tr><td><span class="pill pill-info">準大型</span></td><td>パレト強盗</td><td>20分</td><td>1,100万</td><td>20万・20分</td></tr>
      <tr><td colspan="5" style="background:rgba(244,196,48,.04);font-weight:600;font-size:.85em;color:var(--yuzu);">大型強盗（ギャングのみ）：犯罪者8〜12人 / 警察15人 / 最低受注10人〜</td></tr>
      <tr><td><span class="pill pill-danger">大型</span></td><td>ヒューメイン強盗</td><td>30分</td><td>1,800万</td><td>20万・30分</td></tr>
      <tr><td><span class="pill pill-danger">大型</span></td><td>アーティファクト強盗</td><td>30分</td><td>2,500万</td><td>20万・30分</td></tr>
      <tr><td><span class="pill pill-danger">大型</span></td><td>空母強盗</td><td>30分</td><td>4,500万</td><td>20万・30分</td></tr>
      <tr><td><span class="pill pill-danger">大型</span></td><td>ユニオン強盗</td><td>30分</td><td>5,000万</td><td>20万・30分</td></tr>
      <tr><td><span class="pill pill-danger">大型</span></td><td>パシフィック強盗</td><td>30分</td><td>6,000万</td><td>20万・30分</td></tr>
    </tbody>
  </table>
</div>
"""
    return page('job-pd', '警察 (PD) ルール', '🚓',
                '警察官として活動する際のルール',
                body, breadcrumb=['職業', '警察 (PD)'])


def job_ems_page():
    rules = [
        ('E-002', '車両カラー', '事件対応用は白のみ、パール色は自由。事件対応以外は色自由。EMS以外への貸し出しは一律禁止', 'pill-info', '基本'),
        ('E-003', '倒れてからの光判断', '倒れてから5分経過後に光を見てもよい（EMSに拾われている場合は禁止）', 'pill-info', '基本'),
        ('E-005', '事件対応体制', 'EMS内で最低2名の事件対応員を用意。スマホ電話で連携し安全な位置のpdを救助。アーマー着用必須。フリーで動ける人数が最低2人いない場合は対応不可、その旨をバーディに記載', 'pill-warning', '条件'),
        ('E-006', '犯罪・前科', 'EMSは犯罪禁止。前科がある方の採用は応相談'),
        ('E-007', 'EMS物資の譲渡', 'EMSジョブ専用アイテムの譲渡・貸与禁止。EMS車両の貸出も一律禁止'),
        ('E-008', '情報共有', '事件対応時に得た情報、EMSとして知り得た情報の共有を禁止'),
        ('E-009', '仲間間での治療', 'EMS仲間同士で空腹値や水分値を満たすための治療行為を禁止'),
        ('E-010', '治療費請求', '治療費を請求しない・不当に割引することを禁止'),
        ('E-014', 'IFAKS・包帯販売', '包帯（けがを治す/体力回復量少）¥50,000、IFAKS（けがは治らない/体力回復量大）¥100,000。基本病院で販売', 'pill-info', '価格'),
    ]
    items = '\n'.join(rule_item(*r) for r in rules)
    return page('job-ems', 'EMS（救急）ルール', '🚑',
                '救急隊員として活動する際のルール',
                items, breadcrumb=['職業', 'EMS'])


def job_doctor_page():
    rules = [
        ('DR-002', 'ヘリ・カラー', 'ヘリはスパローとシースパローのみ使用可。車両の色はプライマリ・セカンダリ・パールすべてメタリックのレースイエロー', 'pill-info', '基本'),
        ('DR-003', '服装規定', '服装は黄色であれば自由。防弾性のあるヘルメットは着用禁止', 'pill-info', '基本'),
        ('DR-004', 'ダウン者のピック', 'エスコートで実施。患者を起こす際は安全な場所まで連れて行き蘇生', 'pill-info', '基本'),
        ('DR-005', 'PD・EMSへの行為', '現場対応中の故意のアタック・殺害行為禁止。ダウンや逮捕された場合の現場復帰禁止'),
        ('DR-006', '情報・物資の取扱', '個人医として知り得た情報の部外者への提供禁止。医療器具・手錠・アーマー等の譲渡・他用途使用禁止'),
        ('DR-009', '犯罪参加', '個人医が可能な犯罪・強盗は小型と中型のみ。退勤して実施。準大型・大型強盗への参加・傭兵参加は禁止', 'pill-warning', '条件'),
        ('DR-010', '治療料金', '怪我治療・松葉あり蘇生は最低150万円', 'pill-leaf', '価格'),
        ('DR-011', '松葉なし蘇生料金', '最低300万円', 'pill-leaf', '価格'),
    ]
    items = '\n'.join(rule_item(*r) for r in rules)
    return page('job-doctor', '個人医ルール', '⚕️',
                '個人医（闇医者）として活動する際のルール',
                items, breadcrumb=['職業', '個人医'])


def job_mechanic_page():
    body = """
""" + '\n'.join([
        rule_item('M-001〜003', '基本ルール', '汚職禁止 / 犯罪禁止 / 白市民限定JOB', 'pill-info', '基本'),
        rule_item('M-004', '自店舗カスタム', '自分の店舗で車をカスタムするのは禁止ではないが、正規の値段で利用すること。経済活性化のため他店舗もなるべく使う', 'pill-info', '基本'),
        rule_item('M-005', '料金統一', '市が決めた料金以外での請求を禁止。お店の値段を統一'),
        rule_item('M-006', '性能カスタムの乗せ換え禁止', '移し替え禁止'),
    ]) + """

<h2 style="margin:2rem 0 1rem;font-size:1.3rem;">💰 料金表（修理）</h2>
<div class="table-wrap">
  <table>
    <thead><tr><th>項目</th><th>料金</th></tr></thead>
    <tbody>
      <tr><td>1ヶ所修理</td><td>¥50,000</td></tr>
      <tr><td>タイヤ</td><td>¥100,000</td></tr>
      <tr><td>全修理</td><td>¥450,000</td></tr>
      <tr><td>出張修理</td><td>¥800,000</td></tr>
    </tbody>
  </table>
</div>

<h2 style="margin:2rem 0 1rem;font-size:1.3rem;">⚙️ 部品料金（抜粋）</h2>
<div class="table-wrap">
  <table>
    <thead><tr><th>部品</th><th>価格</th></tr></thead>
    <tbody>
      <tr><td>エンジン Lv1〜5</td><td>30万 / 60万 / 90万 / 120万 / 150万</td></tr>
      <tr><td>ターボ単体</td><td>¥3,500,000</td></tr>
      <tr><td>NOSボトル単体</td><td>¥3,500,000</td></tr>
      <tr><td>NOS補充</td><td>¥750,000</td></tr>
      <tr><td>ターボ+NOS</td><td>¥3,000,000</td></tr>
      <tr><td>ミッション Lv1〜4</td><td>30万 / 60万 / 90万 / 120万</td></tr>
      <tr><td>ブレーキキャリパー Lv1〜3</td><td>60万 / 90万 / 150万</td></tr>
      <tr><td>車高調 Lv1〜5</td><td>30万 / 60万 / 90万 / 120万 / 150万</td></tr>
      <tr><td>構造用接着剤（アーマー）</td><td>¥3,500,000</td></tr>
      <tr><td>外装カスタム（色含む1個当たり）</td><td>¥45,000</td></tr>
      <tr><td>アンチラグ</td><td>¥1,500,000</td></tr>
      <tr><td>ハーネス</td><td>¥450,000</td></tr>
    </tbody>
  </table>
</div>
"""
    return page('job-mechanic', 'メカニックルール', '🔧',
                'メカニックとして活動する際のルール',
                body, breadcrumb=['職業', 'メカニック'])


def job_food_page():
    rules = [
        ('F-001', '商品の無料譲渡禁止', 'お店の商品を無料で渡す行為、横流し、商品の転売を禁止'),
        ('F-002', '値段ルール',
         '運営が決めた値段を下回る請求禁止。下回らなければ店長一任。<br><span style="color:var(--text-muted);font-size:.85em;">飲食店：Food/Drink ¥30,000 / joint ¥50,000<br>joint店：Food/Drink ¥50,000 / joint ¥30,000<br>自販機は各値段に+¥10,000</span>',
         'pill-info', '価格'),
        ('F-003', '購入上限', '店舗の1回の購入上限：ご飯30個 / 飲み物30個 / joint 30個', 'pill-info', '基本'),
        ('F-004', '商品登録', '商品登録時に素材を1つ以上選択。無から生み出すのは禁止'),
        ('F-005', '他店舗商品', '他店舗の商品を自分の店舗で売るのは禁止。コラボ商品は可'),
        ('F-008', '開業', '最初はバーガーショットかジョイントショップから。分社・オリジナルショップ希望はチケットで運営にメンション', 'pill-info', '手続き'),
    ]
    items = '\n'.join(rule_item(*r) for r in rules)
    return page('job-food', '飲食店ルール', '🍔',
                '飲食店経営者・従業員のルール',
                items, breadcrumb=['職業', '飲食店'])


def job_crime_page():
    body = """
<div class="tab-group">
  <button class="tab active" onclick="showTab('cr',this,0)">基本</button>
  <button class="tab" onclick="showTab('cr',this,1)">人質・参加</button>
  <button class="tab" onclick="showTab('cr',this,2)">服装・シーン</button>
  <button class="tab" onclick="showTab('cr',this,3)">時間・歪み</button>
</div>

<div class="tab-content active" data-group="cr">
""" + '\n'.join([
        rule_item('CR-001〜002', 'ヘリ制限', '軽強盗・中型：ヘリ使用禁止 / 準大型・大型：ヘリ×2', 'pill-warning', '条件'),
        rule_item('CR-003', '警察側ヘリ', '小型犯罪は禁止、中型・準大型・大型は警察ヘリ＋1', 'pill-info', '基本'),
        rule_item('CR-039', '犯罪禁止ジョブ', 'メカニック、EMS、警察'),
        rule_item('CR-501', '禁止車両', 'ボート: avisa'),
        rule_item('CR-701', '先配置禁止', '犯罪現場における先配置を禁止（ex. 客船であれば全員船尾スタート）'),
    ]) + """
</div>

<div class="tab-content" data-group="cr">
""" + '\n'.join([
        rule_item('CR-005', '人質ありルール', 'チェイスのみ（発砲禁止）', 'pill-warning', '条件'),
        rule_item('CR-006', '同グループ人質禁止', '同ギャング・同グループを人質にするのは禁止'),
        rule_item('CR-007', '人質OK場所', 'コンビニ、フリーカ銀行のみ人質OK<br><span style="color:var(--text-muted);font-size:.8em;">※宝石店・客船は人質不可に変更</span>', 'pill-info', '基本'),
        rule_item('CR-008〜011', '参加制限', '準大型・大型はギャングのみ実行可能。半グレの傭兵禁止。他ギャングとの合同は可能', 'pill-warning', '条件'),
    ]) + """
</div>

<div class="tab-content" data-group="cr">
""" + '\n'.join([
        rule_item('CR-020〜023', '服装・車両', '同一グループは服装・車両カラー統一必須。プライマリー・セカンダリ・パール統一。白・黒・黄色は禁止。合同犯罪は1色に統一', 'pill-info', '基本'),
        rule_item('CR-024〜030', 'シーン中禁止事項', 'エモート禁止（射撃中・ダウン中含む）／無線撃ち禁止／グリッチ・チート禁止／グレネードはグループ合計5個まで／carry禁止（escortは可能）／セーフゾーン侵入禁止／ゾンビ行為禁止'),
        rule_item('CR-031', '同グループ・個人医接近', '撃ち合い犯罪中、現場付近に来た同グループ・個人医は即撃たれる対象', 'pill-warning', '条件'),
        rule_item('CR-032', '金庫内外の発砲', '金庫内→外、金庫外→内、相互発砲禁止'),
    ]) + """
</div>

<div class="tab-content" data-group="cr">
""" + '\n'.join([
        rule_item('CR-012〜014', '受注', '瞑想後20分後から受注可能。被った場合はチンチロで決定。受注時の警察人数が条件を満たせば犯罪実行可', 'pill-info', '基本'),
        rule_item('CR-015〜016', '利確', '警察への犯罪通知開始から15分後に利確可能。利確前に報酬を車両へ保管するのは禁止', 'pill-info', '基本'),
        rule_item('CR-017〜019', '金持ちルール', '金回収は1人のみ。途中で死亡・歪んだ場合のみ変更可。歪み時のためクリップ必須', 'pill-info', '基本'),
        rule_item('CR-033〜036', '時間ルール', '犯罪禁止時間：瞑想前後20分。瞑想20分前までに犯罪終了必須。逃走シーンで時間超過は警察に投降。タイマー0で強制投降', 'pill-warning', '条件'),
        rule_item('CR-601〜609', '歪み対応', 'プレイヤー判断でのやり直しは禁止。動画を準備して「補填申請」より申請。必須条件：①受注開始から終了まで撮影 ②歪みが確認できる ③/911で5分耐久連絡 ④金持ち役が両手を上げ5分耐久 ⑤逃走完了。提出テンプレート：強盗名/補填希望金額/補填理由/動画URL', 'pill-info', '手続き'),
    ]) + """
</div>
"""
    return page('job-crime', '犯罪ルール', '💀',
                '犯罪行為に関する詳細ルール',
                body, breadcrumb=['職業', '犯罪'])


def news_page():
    items = [
        ('high', '2026-05-02 — 機能変更', '車の積載量縮小', '全体的に車の積載量が減少。消えた場合はその瞬間を録画して補填申請可能。'),
        ('mid', '2026-05-02 — 機能変更', 'リサイクルセンター排出量増加', 'リサイクルセンターの排出量を増加。'),
        ('mid', '2026-05-02 — 機能変更', 'カジノ税の撤廃', 'カジノのtaxをなくしました。稼いだ金額をそのまま取得できます。'),
        ('mid', '2026-05-02 — 機能変更', '溶鉱炉のおじさんの値段調整', '溶鉱炉のおじさんの値段を調整しました。'),
        ('high', '2026-05-01 — サーバー', 'サーバーOPEN！', '本日19時よりスタート。ピーク時には150名の方に遊んでいただきました。開始2時間は犯罪禁止時間。'),
        ('high', '2026-05-01 — ガイドライン', '名前表示の徹底', '基本的に犯罪中以外は <code>/name</code> で名前表示。FiveMのプレイヤー名も街中の名前と同じに。'),
        ('high', '2026-05-01 — 仕様変更', '/me 使用禁止', '/me コマンドの使用を禁止。使用したい方は理由を記載してチケット申請。'),
        ('high', '2026-05-01 — ルール改定', '人質ルール改定', '宝石店も人質OKとされていましたが、人質なしに変更。'),
        ('high', '2026-04-26 — ガイドライン', '恋愛RPに関する注意事項', '禁止はしないが、相互同意・OOC感情との分離・関係強要禁止・他プレイヤーへの配慮が必要。'),
        ('mid', '2026-04-25 — ルール改定', '防弾ヘルメット解除', '防弾性能を取り除けたため、ヘルメット着用を再可能に。'),
        ('high', '2026-04-23 — ルール改定', '禁止車両・カスタム追記', '防弾ガラス・防弾タイヤ装着車両、武装搭載車両、殺傷能力車両、飛行機能車両の使用を禁止。'),
        ('high', '2026-04-23 — ルール改定', '無断DM・フレンド申請禁止', '相手の許可なく Discord での個別連絡・フレンド申請を禁止。'),
        ('high', '2026-04-13 — ルール改定', 'レティクル禁止追記', '外部ツール・ゲーム内コマンドでのレティクル表示を禁止。'),
        ('high', '2026-04-10 — ルール改定', '高画質MOD禁止追記', 'NVE / reshade / QUANT V を含む高画質MODの使用を禁止。'),
    ]
    timeline = '\n'.join(
        f'<div class="timeline-item {cls}"><div class="timeline-date">{date}</div><div class="timeline-title">{title}</div><div class="timeline-content">{desc}</div></div>'
        for cls, date, title, desc in items
    )
    body = f'<div class="timeline">{timeline}</div>'
    return page('news', 'お知らせ', '📢',
                '運営からの最新情報・ルール改定',
                body, breadcrumb=['お知らせ'])


def updates_page():
    cards = [
        ('2026-05-02', '車の積載量を全体的に縮小', '消えた場合は録画して補填申請'),
        ('2026-05-02', 'リサイクルセンター排出量を増加', ''),
        ('2026-05-02', 'カジノ税を撤廃', '稼いだ金額がそのまま取得可能に'),
        ('2026-05-02', '溶鉱炉のおじさんの値段を調整', ''),
        ('2026-05-01', '/me コマンドを使用禁止に', '必要な場合はチケット申請'),
        ('2026-05-01', '請求書システムのエラー修正', ''),
    ]
    items = '\n'.join(
        f'<div class="card"><div class="card-meta">{date}</div><div class="card-title">{title}</div>{("<p>"+desc+"</p>") if desc else ""}</div>'
        for date, title, desc in cards
    )
    body = f'<div class="card-grid">{items}</div>'
    return page('updates', '機能変更履歴', '🔄',
                'サーバー機能のアップデート履歴',
                body, breadcrumb=['機能変更'])


# Build all pages
PAGES = [
    ('index', home_page),
    ('guide', guide_page),
    ('commands', commands_page),
    ('terms', terms_page),
    ('rules-general', rules_general_page),
    ('rules-rp', rules_rp_page),
    ('rules-combat', rules_combat_page),
    ('rules-vehicle', rules_vehicle_page),
    ('rules-relationship', rules_relationship_page),
    ('job-pd', job_pd_page),
    ('job-ems', job_ems_page),
    ('job-doctor', job_doctor_page),
    ('job-mechanic', job_mechanic_page),
    ('job-food', job_food_page),
    ('job-crime', job_crime_page),
    ('news', news_page),
    ('updates', updates_page),
]

for slug, fn in PAGES:
    html = fn()
    path = os.path.join(OUT, f'{slug}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'wrote {slug}.html')

print(f'\nbuilt {len(PAGES)} pages')
