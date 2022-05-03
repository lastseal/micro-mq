# Micro MQ
python v3.9

## Instalación

Usa el manejador de paquetes [pip](https://pip.pypa.io/en/stable/) para instalar micro-mq desde Github

```bash
$ pip install git+https://github.com/lastseal/micro-mq
```

## Uso Básico

Servidor de cola de mensajes

```python
from micro import mq

@mq.worker(port=9000)
def worker(req):
    print("hello world")
```

Cliente que envía un mensaje a la cola

```python
from micro import mq

mq.submit({"data": 1}, port=9000)
```
