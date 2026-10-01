import json
import os

# Load the user's latest audit exported file
audit_file = '/home/leondon-pc/DatosComprimidos/Descargas/auditoria_solicitudes_2026-10-01.json'
with open(audit_file, 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

records = raw_data.get('records', []) if isinstance(raw_data, dict) else raw_data

# Classification logic for 6 standardized categories
def categorize_clavo(record):
    txt = (record.get('fundamento') or '').lower()
    
    # 1. Emergencia sin cobertura
    if any(k in txt for k in ['emergencia', 'urgencia', 'no tenemos gente para éstas cosas', 'no tenemos gente para estas cosas']):
        return 'Emergencia sin Cobertura'
        
    # 2. Fricción de Pago Adelantado
    if any(k in txt for k in ['pago adelantado', 'pago por adelantado']):
        return 'Fricción de Pago Adelantado'
        
    # 3. Error Administrativo / Duplicada
    if any(k in txt for k in ['creada en vano por error', 'en vano por error', 'se creó otra', 'se creo otra', 'solicitud duplicada', 'solicitud creada solo para ayudar', 'cambió de idea y en vez de reparar eligió reemplazo', 'cambio de idea']):
        return 'Error Administrativo / Duplicada'
        
    # 4. Lead No Calificado / Inquilino
    if any(k in txt for k in ['inquilino', 'curioseando', 'tanteando precios', 'no sabe lo que quiere', 'ni sabia lo que quería', 'ni sabia lo que queria']):
        return 'Lead No Calificado (Inquilino/Curioso)'
        
    # 5. Servicio Incompatible / Fuera de Regla
    if any(k in txt for k in ['institución estatal', 'institucion estatal', 'pedido de trabajo', 'no de servicio', 'no tiene rut', 'sin rut', 'servicio complejo para el personal', 'no se dan las condiciones', 'multiline']):
        return 'Servicio Incompatible / Fuera de Regla'
        
    # 6. Falla de Supply / Opciones Insuficientes
    return 'Falla de Supply / Opciones Insuficientes'

# Assign categories
for r in records:
    if r.get('esClavo') and not r.get('noEsClavo'):
        r['categoriaClavo'] = categorize_clavo(r)
    else:
        r['categoriaClavo'] = ''

# Separate subsets
clavos = [r for r in records if r.get('esClavo') and not r.get('noEsClavo')]
conflictos = [r for r in records if r.get('noEsClavo') and r.get('esClavo')]
noclavos = [r for r in records if r.get('noEsClavo') and not r.get('esClavo')]
sinmarcar = [r for r in records if not r.get('noEsClavo') and not r.get('esClavo')]

print(f'Total: {len(records)} | Clavos: {len(clavos)} | Conflictos: {len(conflictos)} | No Clavos: {len(noclavos)} | Sin marcar: {len(sinmarcar)}')

# Output categorized records back to assets
with open('/home/leondon-pc/Desktop/Manual_Operativo_Supply_ArreglaTodo/assets/datos_solicitudes_auditadas.json', 'w', encoding='utf-8') as f:
    json.dump(records, f, ensure_ascii=False, indent=2)

print('Saved categorized records to assets/datos_solicitudes_auditadas.json')
