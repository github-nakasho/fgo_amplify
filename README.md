# fgo_amplify

## 実行方法

1. 以下の方法で、このスクリプトで用いられているライブラリをインストールします。

```bash
$ pip install -r requirements.txt
```

2. `solve_problem.py`の`client.token = 'xxxxx'`の部分に、ご自分のアクセストークンを入力します。

3. 以下の方法で、`main.py`を実行します。

```bash
$ python main.py
```

## 実行結果

```bash
***** Enemies *****
0: assassin
1: caster
2: rider
***** My party *****
0: berserker
1: alter ego
2: alter ego
3: alter ego
4: alter ego
5: ruler
```

## インスタンスの変更

デフォルトでは、敵メンバーが「assassin(殺)・caster(術)・rider(騎)」に設定されています。ここではそれを変更する手順をご紹介します。  
`make_instance.py`で敵メンバーの数やタイプを変更することができます。例えば、敵メンバーを「saber(剣)・moon cancer(月)」にする場合は以下のようにします。

```python
enemy1 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
enemy2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
enemies = np.array([enemy1, enemy2])
```

enemy1にsaber(剣)、enemy2にmoon cancer(月)を割り当て、それを`enemies`というNumPy配列に格納します。  
enemy1, enemy2において、指定したいタイプの箇所に1を代入します。それ以外のタイプの箇所には0を入力します。敵タイプの指定における、タイプの並びは以下のようになっています。

```python
['saber', 'archer', 'lancer', 'rider', 'caster', 'assassin', 'berserker', 'ruler'. 'avenger', 'moon cancer', 'alter ego', 'foreigner', 'shielder']
```

