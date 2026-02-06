# BOWLING GAME KATA🎳 

## <div id= 'introduccion'>Introducción</div>
Adrián González González    - <a href= 'https://github.com/Adriceka'>@Adriceka</a>

Este repositorio tiene la solución del juego BOWLING cuyo objetivo es calcular la puntuación de una partida normal de 10 frames.


## Reglas

Un juego de bowling tiene **10 frames (turnos)**. En cada frame el jugador intenta derribar **10 pins (bolos)**.  
Cada frame tiene hasta **2 rolls (tiradas)**, excepto el **tenth frame (décimo turno)**.

Si en un frame no se derriban los 10 pins, el **score (puntuación)** del frame es la **suma de los pins derribados**.

Un **spare (semipleno)** ocurre cuando se derriban los 10 pins en los dos rolls del frame. El score del frame es **10 más los pins del siguiente roll**.

Un **strike (pleno)** ocurre cuando se derriban los 10 pins en el primer roll del frame. El frame termina y el score es **10 más los pins de los dos siguientes rolls**.

En el décimo frame, si se consigue un spare se obtiene **1 extra roll (tirada extra)** y si se consigue un strike se obtienen **2 extra rolls**. Estos rolls solo se usan para calcular el score de ese frame.

Un **perfect game (juego perfecto)** consiste en **12 strikes consecutivos** y da un total de **300 points (puntos)**.

