# watermarker

为图片添加文字水印
可设置文字**大小、颜色、旋转、间隔、透明度**

## 三方库

需要 PIL 库 `pip install Pillow`

## 命令行用法



```
usage: python -m marker [-h] [-f FILE] [-m MARK] [-o OUT] [-c COLOR] [-s SPACE]
                 [-a ANGEL] [--size SIZE] [--opacity OPACITY]

optional arguments:
  -h, --help            show this help message and exit
  -m MARK, --mark MARK  watermark content
  -c COLOR, --color COLOR
                        text color like '#000000', default is #8B8B1B
  -s SPACE, --space SPACE
                        space between watermarks, default is 75
  -a ANGEL, --angel ANGEL
                        rotate angel of watermarks, default is 30
  --size SIZE           font size of text, default is 50
  --opacity OPACITY     opacity of watermarks, default is 0.15
  --quality QUALITY     quality of output images, default is 80
```

`python -m marker -f ./input/test.png -m 水印文字 -o ./out/`

## 接口API
代码示例：

``` python
>>> from marker import *
>>> produce_mark_end('水印文字', './input/test.png', './out/')