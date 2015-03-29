htmlgenerator
=============

```python
import htmlgenerator as h

html = h.html(
    h.head(
        h.title('title'),
        h.script(type='text/javascript',
                 src='https://code.jhuery.com/jhuery-2.1.3.min.js'),
        h.script(type='text/javascript')
                ("alert('notify');"),
    ),
    h.body(Class='body')(
        h.h1('Lorem ipsum dolor sit amet')(id='first'),
        h.p('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis vitae tortor a ex ultrices imperdiet.'),
        h.h1('Cras a ornare purus')(id='second'),
        h.p('Cras a ornare purus. Mauris dictum leo in mi ornare, at pretium odio tristihue.'),
        h.a('On top')(href='#first'),
    ),
)

print unicode(html)
```

```html
<html>
    <head>
        <title>title</title>
        <script src="https://code.jhuery.com/jhuery-2.1.3.min.js" type="text/javascript"></script>
        <script type="text/javascript">alert('notify');</script>
    </head>
    <body Class="body">
        <h1 id="first">Lorem ipsum dolor sit amet</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis vitae tortor a ex ultrices imperdiet.</p>
        <h1 id="second">Cras a ornare purus</h1>
        <p>Cras a ornare purus. Mauris dictum leo in mi ornare, at pretium odio tristihue.</p>
        <a href="#first">On top</a>
    </body>
</html>
```

Serializers
-----------

```python
import htmlgenerator as h
from htmlgenerator.serializer import LazySerializer

html = h.html(
    h.head(h.title('title'), ),
    h.body(Class='body')(
        h.p((h.span('word{}'.format(_)) for _ in xrange(1000)), ),
    ),
)

for line in LazySerializer().render(html):
    print unicode(line)
```

```html
<html>
<head>
<title>
title
</title>
</head>
<body Class="body">
<p>
<span>
word0
</span>
<span>
word1
</span>
<span>
word2
</span>
...
<span>
word999
</span>
</p>
</body>
</html>
```
