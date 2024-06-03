# IntroductionPrograming-library

## Overview
千葉工業大学 先進工学部 知能メディア工学科の第2セメスター「プログラミング言語基礎」及び第3セメスター「プロジェクト1」において使用される、Pythonの図形描画ライブラリです。
tkinterのWrapperで、[Processing](https://processing.org/)ライクに動作させることを目指して作成されました。

## Requirement
### 必要環境
- MacOS
  - Windowsでも使用可能ですが、音楽を再生する機能のみ使用不可です
- Python3.10.5 <
  - 動作確認済み >=3.11.5
  - 3.12系は現在未対応
- Pythonの標準ライブラリのみで動作
  - tkinter 8.6以上が必須

### 開発・動作確認環境
- MacOS Ventura以降
- Python
  - brew + pyenv
  - 3.10.5 <
  - <= 3.11.5
- ライブラリ
  - Python標準
  - tkinter 8.6

### 環境構築の既知トラブル
#### MacOSかつpython3.10系の場合
tkinter8.5がデフォルトで入っているようですが、[Pythonとtcl/tkの対応問題](https://www.python.org/download/mac/tcltk/)によって実行時にWindowが黒く表示される不具合が発生します。

```
import tkinter
tkinter.Tcl().eval('info patchlevel')
```

上記をPythonで実行するとtkinterのバージョンを確認することが可能です。

開発・動作確認環境と同様にbrew + pyenv環境の場合は

```
pyenv uninstall 3.10.x
brew install python-tk
pyenv install 3.10.x
```

でおおよその場合解決します。

#### 実行時にImportErrorが出て、エラー箇所がImport _tkinterの場合
tkinterがうまく読み込めていません。
Python Build時にtkinterのリンクがちゃんといってない？詳細な原因は不明です。
開発・動作確認環境と同様にbrew + pyenv環境の場合は

```
pyenv uninstall 3.10.x
brew install python-tk
pyenv install 3.10.x
```

でおおよその場合解決します。

#### import IP 実行時にModuleNotFoundErrorが出て、エラー箇所がimport IP.IPの場合
他にも以下パターンは同様の原因です。
```
ModuleNotFoundError: No module named "IP.mouse"
ModuleNotFoundError: No module named "IP.keyboard"
```

パッケージのダウンロードもしくは展開時(zipでダウンロードした場合)にライブラリ内のIP.py等が欠損したことが原因です。
ダウンロードもしくは展開をやり直して、以下のファイルが全てあることを確認してください。

<img width="222" alt="IPファイル構成" src="https://github.com/aais-lab/IntroductionPrograming-library/assets/75377571/97f7fa3f-47e3-4e3f-8c2d-8a0ccf99f1ad">

## Usage
### 導入方法
#### gitからクローン
```
git clone https://github.com/aais-lab/IntroductionPrograming-library.git
```
#### ライブラリのフォルダへ移動して、pip install
```
cd IntroductionPrograming-library
pip install .
```

Successfully installed IP-x.x.xと表示されれば導入完了です。

## Reference
関数等のリファレンス
[IntroductionPrograming-Reference](https://aais-lab.github.io/IntroductionPrograming-Reference/)

## Author
[Nao Yamanouchi](https://github.com/ClairdelunaEve)

## Licence
3-Clause BSD
