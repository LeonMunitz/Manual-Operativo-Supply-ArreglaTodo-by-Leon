import os
import json
import whisper

video_dir = '/home/leondon-pc/DatosComprimidos/Escritorio/Manual_Operativo_Supply_ArreglaTodo/videos'
output_file = '/home/leondon-pc/DatosComprimidos/Escritorio/Manual_Operativo_Supply_ArreglaTodo/transcripts.json'

print("Loading Whisper model 'small'...")
model = whisper.load_model("small")

files = sorted([f for f in os.listdir(video_dir) if f.endswith('.mp4')])
results = {}

for f in files:
    path = os.path.join(video_dir, f)
    print(f"Transcribing {f}...")
    res = model.transcribe(path, language="es")
    results[f] = {
        "text": res["text"],
        "segments": [
            {
                "id": s["id"],
                "start": s["start"],
                "end": s["end"],
                "text": s["text"]
            }
            for s in res["segments"]
        ]
    }
    print(f"Done {f}: {len(res['text'])} chars")

with open(output_file, 'w', encoding='utf-8') as out:
    json.dump(results, out, ensure_ascii=False, indent=2)

print("All transcriptions saved to", output_file)
