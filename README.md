# Flappy Bird

<div style="text-align:center;">
  <image src="https://github.com/JavierAM01/Machine-Learnig-in-Games/blob/main/images/flappybird.gif" style="width:100%; height:12cm;">
</div>
  
## Explicación

Para la creación del Flappy Bird, necesitamos de 3 componentes principales, el pájaro, los pilares y el suelo. El fondo por su parte será estático por lo que 
únicamente es poner la imagen en el fondo. 

### Bird
  
Necesitamos hacer que caiga si no hacemos nada, es decir, crear gravedad en el juego. Para ello sencillamente creamos una característica al pájaro llamada 
gravedad y otra para actualizar su posición.

```python
class Bird:
    def __init__(self, enviroment):
        self.gravity = 0.25
        self.movement = 0
```
  
Por defecto será un valor (que hace que caiga) y si presionamos el ```SPACE``` quitaremos ese efecto para que puede subir. Es decir, reiniciamos a cero el movement 
y le restamos cierta cantidad (recordar que la gráfica de pygame comienza el (0,0) en la esquina superior izquierda, por lo que sumar en el eje y va hacia abajo y 
restar hacia abajo).

```python
if event.type == pygame.KEYDOWN:
    if event.key  == pygame.K_SPACE:
        self.bird.movement = 0
            if self.bird.surface.top > 0: 
                self.bird.movement -= 5 
```
  
### Pipes

Los pilares serán creados cada cierto tiempo, tendremos una imagen hacia arriba y otra del revés para cada par de ellas. Las alturas las generaremos de forma aleatoria 
según ciertos valores predeterminados. 

```python
    def create_pipe(self, img_pipe):
        random_height = random.choice(self.pipe_heights)
        top_pipe = img_pipe.get_rect(midtop = (450, random_height))
        bottom_pipe = img_pipe.get_rect(midbottom = (450, random_height - 200))
        return top_pipe, bottom_pipe 
```

### Floor 

Para el suelo crearemos dos imagenes una seguida de la otra y la iremos moviendo hacia la izquierda en cada frame creando el efecto del movimiento a lo largo del eje x.
Cuando la primera imagen ya esté totalmente fuera del plano, se reiniciará hacia la derecha dando la sensación de que nunca termina.
