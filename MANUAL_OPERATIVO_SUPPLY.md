# Manual Operativo Integral: Supply & CRM ArreglaTodo
**Versión Unificada y Orgánica 2.0**  
*Consolidación de procesos operativos para el equipo de Supply y Atención al Cliente.*

---

## 🗺️ Índice General y Estructura Orgánica

- **Módulo 1: Arquitectura del Ecosistema y Reglas Críticas**
  - 1.1 Las 3 piezas del sistema: `supply.arreglatodo.uy`, `crm.arreglatodo.uy` y el bot `n8n`.
  - 1.2 Punto ciego de seguridad: El desfasaje entre CRM y n8n (*"Recibe ofertas igual"*).
  - 1.3 Política de mensajería Meta: Ventana de 24 horas y plantillas oficiales de Utilidad.
- **Módulo 2: Curado Diario del Pipeline de Supply (El Orden Correcto)**
  - 2.1 Filosofía de priorización: *"Se trabaja primero lo que destraba a los demás"*.
  - 2.2 Prioridad 1: *"Sin Decidir"* (El triaje obligatorio: A prueba vs. Inactivo).
  - 2.3 Prioridad 2: *"Completando Registro"* (Faltantes y conversión rápida).
  - 2.4 Prioridad 3: *"Sin Acceso"* (Carga del Gmail desde el chat en tandas de 15).
  - 2.5 Seguridad Antifraude: *"Piden entrar con otro Gmail"* (Validación por WhatsApp oficial).
  - 2.6 Cadencia de seguimiento: Recordatorios automáticos días 3, 7 y 10 (asistencia telefónica).
- **Módulo 3: Protocolo de Revisión y Auditoría de Perfiles (Pestaña "Revisión")**
  - 3.1 Criterio editorial: *"Corregir es parte de revisar"* (SLA máximo: 48 horas).
  - 3.2 Validación de rubros: Llamada obligatoria a las 2 referencias (guion y confidencialidad).
  - 3.3 Curaduría editorial directa (Nombre, Sobre mí y Zonas de cobertura).
  - 3.4 Auditoría de fotos y videos: Motivos de rechazo y la *Regla de las 2 fotos*.
  - 3.5 Determinación final: *Aprobar y verificar* vs. *Pedir correcciones*.
- **Módulo 4: Operaciones Avanzadas, Retención y Despacho Comercial**
  - 4.1 Monitoreo en tiempo real: El indicador *En vivo* (punto verde) y la campana de avances.
  - 4.2 Gestión de prestadores inactivos: Consulta y registro de motivo en el bot.
  - 4.3 Mecanismo de corte: *"Sin oportunidades"* (Motivo obligatorio y botón inverso).
  - 4.4 Operación en CRM (Atención al Cliente): Selección de visibles y respuesta ante *"No me llegan trabajos"*.

---

## MÓDULO 1: Arquitectura del Ecosistema y Reglas Críticas

### 1.1 Las Tres Piezas del Sistema
1. **supply.arreglatodo.uy:** Plataforma donde el equipo de Supply gestiona a los prestadores, audita sus carpetas, realiza el onboarding y mantiene el seguimiento diario.
2. **crm.arreglatodo.uy:** Herramienta utilizada por Atención al Cliente para coordinar presupuestos con clientes y asignar los trabajos a los prestadores del rubro.
3. **Bot de Reparto Automático (n8n):** Flujo automatizado que dispara avisos de oportunidades laborales a los teléfonos de los prestadores.

> **Regla de Oro:** Toda la comunicación oficial con el prestador se gestiona **únicamente desde el panel de Supply**. Nunca se debe escribir desde celulares personales ni WhatsApp Web externo.

### 1.2 Alerta de Seguridad Crítica: CRM vs. n8n
- **El CRM:** Al usar el botón *"Seleccionar visibles"*, el sistema saltea automáticamente a los prestadores **Suspendidos**, **De baja** y **Sin oportunidades**.
- **El Bot n8n (Punto Ciego):** El script automático **hoy en día SOLO excluye a los "Suspendidos"**. A los que están "De baja", "Inactivos" o "Sin oportunidades" les pueden seguir llegando ofertas.
- **Protocolo de Alerta:** Si en la tarjeta del pipeline aparece en rojo `Recibe ofertas igual (X)`, significa que el bot le sigue enviando trabajos a pesar del estado. Si lleva días cortado, **se debe reportar inmediatamente a Máximo con el nombre del prestador**.

### 1.3 Ventana de 24 Horas y Plantillas de Meta
- Si pasaron más de 24 horas desde que el prestador escribió por última vez, Meta bloquea los mensajes de texto libre.
- Se debe utilizar el botón **"Mandar plantilla"** seleccionando entre las 8 plantillas oficiales aprobadas de Supply (categoría Utilidad).
- Antes de enviar, verificar con **"Ver cómo le llega"** que los links y variables dinámicas estén correctos.
- Las plantillas salen firmadas por **Máximo**.
- En cuanto el prestador responde la plantilla, la ventana de 24 horas se reabre y ya se puede volver a chatear con texto libre usando *"Poner en el chat"*.

---

## MÓDULO 2: Curado Diario del Pipeline de Supply

El orden visual del tablero Kanban no es el orden cronológico de trabajo diario. Se debe ejecutar en el siguiente orden de prioridades:

### Paso 1: "Sin Decidir" (El filtro inicial)
- Son nuevos registros donde nadie definió si trabajarán con nosotros.
- **Regla inalterable:** *Hasta que no se decida, no se le escribe.*
- **Acción:**
  - Si cumple el perfil -> Arrastrar a **"A prueba"**.
  - Si no aplica -> Arrastrar a **"Inactivo"** registrando obligatoriamente el motivo del descarte en el bot.

### Paso 2: "Completando Registro" (Conversión Rápida)
- Son prestadores que ya tienen Gmail y ya iniciaron el proceso. Son los que más rápido quedan activos.
- Cada tarjeta especifica con precisión los campos faltantes (cédula, fotos, experiencia, zonas, RUT, datos de pago).
- El botón **"Escribirle"** abre el chat con el mensaje exacto redactado para su situación.
- Si nunca entró, se le envía el acceso; si ya entró, se le reclaman los ítems pendientes.

### Paso 3: "Sin Acceso" (Carga de Gmail)
- **Sin Gmail no hay espacio ni perfil.**
- Se procesan en tandas de **15 contactos por día**.
- Pedirle el correo por chat. Cuando lo pase, copiarlo y pegarlo en el campo lateral `Cargar su Gmail`.
- Verificar ortografía con sumo cuidado. Click en *Guardar en su ficha*.
- **La tarjeta se mueve SOLA** a *"Completando registro"*. Enviar inmediatamente el link de acceso generado.

### Protocolo Antifraude: Cambio de Gmail ("Piden entrar con otro Gmail")
- Si un prestador pide cambiar su correo, en la pestaña Revisión aparecerá el aviso rojo `Piden entrar a su perfil`.
- **Procedimiento:** Escribirle SIEMPRE al WhatsApp oficial de su ficha preguntándole expresamente por ambos correos. Solo cuando confirme fehacientemente, presionar en Revisión *"Es quien dice ser"*. Si no responde o desconoce el pedido, no aprobar.

### Cadencia de Seguimiento Automático
- **Día 3:** Recordatorio inicial de ficha pendiente.
- **Día 7:** Segundo recordatorio de avance.
- **Día 10:** Mensaje de oferta de asistencia telefónica guiada (*"Ofrecer ayuda por teléfono"*).

---

## MÓDULO 3: Protocolo de Revisión y Auditoría de Perfiles

SLA de atención obligatorio: **Máximo 48 horas** desde que el prestador envía su carpeta.

### 3.1 Filosofía de Revisión: "Corregir es parte de revisar"
Lo que el operador puede corregir directamente en la pantalla (tildes, mayúsculas, formato del texto "Sobre mí", zonas), **se corrige en el acto**. No se le devuelve el perfil al prestador para no generar demoras innecesarias.

### 3.2 Validación de Rubros: Llamada a las 2 Referencias
- Es obligatorio llamar por teléfono a las 2 referencias cargadas.
- **Guion de llamada:**
  1. ¿Cómo fue el trabajo de [Rubro]?
  2. Del 1 al 10, ¿cómo calificarías calidad y puntualidad?
  3. ¿Qué aspecto mejoraría?
  4. ¿Lo volverías a contratar?
- Anotar de forma textual lo respondido. **El prestador no tiene acceso a estas notas confidenciales.**
- Calificar: `Lo recomienda`, `No lo recomienda` o `No respondió`.
- Si se aprueba, el rubro se activa en su perfil web y el bot n8n le empieza a asignar trabajos de esa especialidad.

### 3.3 Auditoría de Fotos y Videos
- Inspeccionar cada foto y video en tamaño grande.
- **Causales de eliminación inmediata de fotos:** Números de teléfono o enlaces en la imagen, logotipos de empresas competidoras, marcas de agua o fotos de catálogo de internet.
- Se borra la foto registrando el motivo (el prestador sí lo ve en su espacio).
- **Regla de las 2 fotos:** Si al quitar fotos incorrectas quedan al menos 2 fotos válidas, **NO se devuelve el perfil**: se eliminan las fotos indebidas y se aprueba.
- **Videos:** Mirarlos completos; muchos dicen o muestran teléfonos al final.

### 3.4 Decisión Final
- **Aprobar y verificar:** Presionar botón verde. Pasa a *Verificado y activo* (si ya está a prueba en el bot y completó los 11 pasos) o a *Completando registro* (si le faltan datos administrativos). Recordar avisarle por chat.
- **Pedir correcciones:** Redactar en el recuadro de devolución qué debe corregir.

---

## MÓDULO 4: Operaciones Avanzadas, Inactivos y CRM

### 4.1 Monitoreo "En Vivo" (Punto Verde)
- El punto verde late arriba a la derecha cuando un prestador estuvo activo en su espacio en los últimos 10 minutos.
- **Regla clave:** *"Escribile cuando está en su espacio"*, aprovechando que tiene el dispositivo en la mano.
- Los avisos de hitos críticos (completó todo, mandó a revisión, cambio de correo) **quedan anclados** hasta que el operador los atiende.
- La campana guarda los últimos 50 avances con acceso directo a Chat o Pipeline.

### 4.2 Gestión de Inactivos
- Prestadores que pausaron su actividad.
- Consultarles el motivo con la plantilla oficial y **asentar la respuesta en el bot** con nombre y fecha para no duplicar consultas.
- Si desean reactivarse, presionar **"Quiere volver: pasar a prueba"**. Vuelven a recibir trabajos al instante.

### 4.3 Cortar Oportunidades ("Sin Oportunidades")
- Pausa el despacho de trabajos sin alterar su estado ni suspenderlo.
- **El motivo es obligatorio** en la ventana modal.
- La tarjeta queda marcada con etiqueta negra y el botón cambia a *"Volver a mandarle"*.
- Usar el filtro *"Solo los que reciben ofertas"* para controlar filtraciones indebidas.

### 4.4 Vista desde el CRM Comercial
- En la solicitud de presupuesto, abrir *"Enviar a trabajadores"*:
  - **Sin marca:** Activo y disponible.
  - **Inactivo:** Seleccionable (recibe igual por decisión operativa de cobertura).
  - **Suspendido, De baja, Sin oportunidades:** En gris, bloqueados.
- El botón *"Seleccionar visibles"* los excluye automáticamente.
- Si un prestador reclama *"No me llegan trabajos"*, verificar su marca en esta lista y derivar a Supply con su nombre.
