[TOC]

# Python Cookbook

## Data Structures and Algorithms

### 1.12 Determine the Most Frequently Occurring Items in a Sequence

* Prefer using `collections.Counter`
* `Counter(dict)`來初始化
* 兩個Counter可以加、減。counter減成負數的key會被移除。
* `word_counts[word] += 1`, `word_counts[word] -= 10`這些都是允許的，但是減法即使減出了負數，對應的key也**不會**被移除。
  * 但是Counter的加減法之後會重新驗證驗證一下哪些key需要被刪除
  * 所以，如果intentionally地想保留負值的counts，不要用Counter的加減法生成出來的新的object來給原來的object賦值。
* `Counter.elements()`很好用，會根據每個key的counts把它們收集成一個`list`。
  * 負的counts對應的key會被忽略。
  
## String and Text

### 2.15 Interpolating Variables in Strings
* `s.format_map(vars())`, `s.format_map(locals())`, and `s.format(**locals())` 是等價的。
* `vars()`和`locals()`是等價的。
  * 但是`vars(object)`還可以抓到object里的variables。
* `__missing__()` method可以用來定義缺省值。之前的`defaultdict`應該用的就是它。  
* `sys._getframe(0)`是獲取stack最頂端的frame，所以文中取了`sys._getframe(1)`，意思是獲取`sub()`方法的caller對應的`locals()`。

