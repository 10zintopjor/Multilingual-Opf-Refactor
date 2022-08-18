from test_span import toyaml,from_yaml
from pathlib import Path

def get_alignmnets():
    alignemnt = from_yaml(Path("A8FF88F64/A8FF88F64.opa/E38A/Alignment.yml"))
    segment_pairs = alignemnt["segment_pairs"]
    return segment_pairs

def get_segment_layer():
    seg_layer = from_yaml(Path("opf/I3EE785F4/I3EE785F4.opf/layers/246C/Segment.yml"))
    return seg_layer

segment_pairs = get_alignmnets()
seg_layer = get_segment_layer()
annotations = seg_layer["annotations"]
new_annotaions = {}

for seg_id,ann_id in zip(segment_pairs,annotations):
    mother_seg_id = segment_pairs[seg_id]["I75A88184"]
    new_annotaions.update({mother_seg_id:annotations[ann_id]})

seg_layer["annotations"] = new_annotaions

new_Segment_layer = toyaml(seg_layer)
Path("./new_Segment_layer.yml").write_text(new_Segment_layer)