# Del fragmento a la forma

Escena 3D interactiva para presentar la reconstrucción de una vasija. Abre con el escaneo texturizado, dibuja el perfil y las secciones al pulsar **Trazar**, y revela la superficie completa al pulsar **Reconstruir**. Incluye recorrido automático, giro, zoom, vista ampliada, reinicio y comparación con los fragmentos.

## Publicar en Netlify

Importar este repositorio. `netlify.toml` configura `dist` como carpeta publicada; no se necesita comando de compilación. Todo el contenido y las dependencias se sirven desde el mismo sitio. No solicita cámara ni envía imágenes.

Para verlo localmente: `python3 -m http.server 8766 --directory dist` y abrir http://localhost:8766.

## Modelos y representación

Los modelos proceden del escaneo y de la restitución aprobada en `Vasija_color_corregido.blend`. La exportación trabaja sobre una copia en memoria y no guarda cambios en ese archivo. El escaneo mantiene su textura UV; la restitución recibe un material de presentación terracota, distinto de la evidencia conservada. Los trazos siguen el perfil meridiano del proyecto; la animación ilustra la restitución existente, no calcula una reconstrucción nueva.

Los datos usan metros y Z vertical; la escena convierte Z a Y. El escaneo y la restitución mantienen su registro original. «Ver fragmentos» hace translúcida la restitución para inspeccionar ambos. La restitución es una hipótesis geométrica y no implica que las superficies coincidan exactamente.

## Dependencias

Three.js 0.160.1 y OrbitControls, licencia MIT. Archivos locales en `dist/vendor`; se conserva la licencia. OrbitControls se modifica únicamente para importar el módulo local de Three.js.

## Accesibilidad y uso

Girar: arrastrar con ratón o dedo. Zoom: rueda o gesto con dos dedos. Con el lienzo enfocado, flechas izquierda/derecha giran; +/− acercan/alejan. Se respeta la preferencia de reducir movimiento. El botón Escaneo interrumpe y reinicia la secuencia.

## Validación de esta entrega

Safari 26.6.2 en macOS: escaneo, trazado, reconstrucción, comparación y reinicio correctos. Chromium: recorrido automático, interrupción de animación, giro y zoom; vista de 390 px sin desbordamiento horizontal. Resultados en `qa/`. La interfaz está adaptada al móvil; no se ha realizado una prueba en un iPhone físico.
