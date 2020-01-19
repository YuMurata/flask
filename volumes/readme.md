# volumes structure
volumesフォルダの構成案

***実際に変更するときはftpとかでバックアップとっておくべき！***

```
volumes
├─image
│  ├─comparable
│  ├─optimizable
│  └─optimized
│      └─[NIMA]
│          └─[ResNet]
└─users
    └─[user]
        ├─optimizes
        ├─scored_params
        └─weights
```

## image
* 比較用とか補正用の画像入れる

### comparable
* 比較用の画像入れるフォルダ
* 一意のファイル名にするかカテゴリ別にフォルダ分けしてさらに名前つけるか
    * 今のところ一意のファイル名にしたい

### optimizable
* 補正用の画像入れるフォルダ
* 一意のファイル名にするかカテゴリ別にフォルダ分けしてさらに名前つけるか
    * 今のところ一意のファイル名にしたい

### optimized
* NIMAとかで補正済みの画像入れるフォルダ
* ファイル名を`optimizable`のファイル名と対応付けたい

#### [NIMA]
* フォルダ名は手法名にする
* 今のとこNIMAしか考えてない

##### [ResNet]
* フォルダ名は手法名にする
* 今のとこResNet、NasNet、MobileNet考えてる

## users
* 各ユーザーのデータ入れる

### [user]
* フォルダ名はユーザー名

#### optimizes
* 補正した画像入れるフォルダ
* `optimizable`のファイル名と対応付けたい

#### scored_params
* スコアリングデータ入れるフォルダ
* 一意のファイル名にするかカテゴリ別にフォルダ分けしてさらに名前つけるか
    * ファイル名を`comparable`のファイル名と対応付けるべき

#### weights
* モデルの重みデータ入れるフォルダ
* 重みの名前は`weight.h5`とかでいい気がする。
* tensorbordのlogとかvalidation_lossのログとか取りたい
    * tensorboardのlogはさらにフォルダ作ったほうがいいかも？
