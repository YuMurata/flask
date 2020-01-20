# Enhancer
毎日定時に全ユーザーの嗜好データから画像を補正する
手動でも補正できる

# `run.py`
定時に補正するプログラム。基本的にこれ動かしっぱ。

毎日<>時（未定、1時ぐらい）に補正プログラムが実行される
## 処理手順
1. `volumes/users`を上から順番に見る
    * フォルダじゃないファイルがあったらwarn
1. `volumes/users/<user>/weights/weight.h5`の存在を確認
    * あったら3.
    * なかったら1.
1. `volumes/optimizables`を上から順番に見る
    * フォルダじゃないファイルがあったらwarn
1. `volumes/users/<user>/scored_params`内のファイル名と同じ名前のフォルダの存在を確認
    * あったら5.
    * なかったら3.
1. `volumes/optimizables/<category>`を上から順番に見る
    * フォルダじゃないファイルがあったらwarn
1. 最適化した画像を`volumes/users/<user>/optimizes/<category>`へ
1. 最適化時のログを`volumes/users/<user>/optimizes/<category>/logs`へ
1. 1.へ戻る



