---
permalink: /tech/jupyter/
tags: python jupyter
---

通过 `Jupyter` 来作为研究平台时，需要使用很多 `Python` 代码，零散的代码片段对后期维护提出了很大的挑战。但是可以通过将常用的代码整合到对应的工具库中，在 `Jupyter` 中直接导入后使用。

# 导入外部代码库

```python
  import sys
  sys.path.append("e:/workspace/tools")

  from tools.ba import *
  Banxcel.DX_BANKS
```
