# Among Us Darts Bot

```
現在こちらのbotは公開を停止しています。申し訳ありません。
```

ボイスチャンネルに入っている人の中からランダムで1人選んでDMを送るbotです。

MODが使えない環境でも「狂人」や「てるてる」が入ったAmong Usを楽しむことができます。

※非力なサーバーで動かしているので、不具合があっても許してください

## 使い方

<!--<a href="https://discord.com/api/oauth2/authorize?client_id=814485711238725652&permissions=11264&scope=bot"><img src="https://github.com/amaotone/among-us-darts-bot/blob/master/icon.png" width="200" height="200"></a>-->
<img src="https://github.com/amaotone/among-us-darts-bot/blob/master/icon.png" width="200" height="200">

~上のアイコンをクリックして、Botをdiscordサーバーに招待してください。~

現在は運用を停止しています。

1人選ぶだけの場合

```
.darts [channel]
```

たとえば「狂人」を選びたい場合

```
.darts [channel] 狂人
```

## ルール例

ルールはなんか上手いこと考えてください。
クルーに対抗する役職の場合はタスクをやるインセンティブがなくなってしまうので、「タスク終了が自分が最後なら敗北」という条件をつけると良いと考えています。

- 狂人
  - 村人にDMが届いた場合、狂人になります
  - インポスターにDMが届いた場合、無視してください（狂人欠け）
  - 狂人はインポスター勝利のときに勝利になります
  - （MODと違って）タスクをやる必要があります
  - クルー勝利 or タスク終了が自分が最後 のとき敗北します
- てるてる
  - 村人にDMが届いた場合、てるてるになります
  - インポスターにDMが届いた場合、無視してください（てるてる欠け）
  - てるてるは吊られたら勝利になります
  - （MODと違って）タスクをやる必要があります
  - クルー勝利 or インポスター勝利 or タスク終了が自分が最後 のとき敗北します
