from pathlib import Path
import yaml

def toyaml(dict):
    return yaml.safe_dump(dict, sort_keys=False, allow_unicode=True)

def from_yaml(yml_path):
    return yaml.safe_load(yml_path.read_text(encoding="utf-8"))

base_text = Path("opf/I3EE785F4/I3EE785F4.opf/base/246C.txt").read_text(encoding="utf-8")
layer_path = Path("opf/I3EE785F4/I3EE785F4.opf/layers/246C/Segment.yml")
ann = from_yaml(layer_path)

annotations = ann['annotations']
new_base_text = ""
for seg_id in annotations:
    span = annotations[seg_id]["span"]
    start = span["start"]
    end = span["end"]
    new_base_text+=base_text[start:end].replace("\n","")+"\n"

Path("test_base_text.txt").write_text(new_base_text)

