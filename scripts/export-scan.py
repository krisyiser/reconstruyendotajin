import bpy,json,numpy as np
from pathlib import Path
r=Path(__file__).resolve().parents[1];out=r/'dist/assets'
bpy.ops.wm.open_mainfile(filepath=str(r.parent/'vasija_color_corregido/Vasija_color_corregido.blend'))
s=bpy.data.scenes['01_Comparacion'];bpy.context.window.scene=s
obj=next(o for o in s.objects if o.name.startswith('SM_Escaneo'));obj.data=obj.data.copy();obj.location=(0,0,0)
for o in bpy.context.selected_objects:o.select_set(False)
obj.select_set(True);bpy.context.view_layer.objects.active=obj
mod=obj.modifiers.new('Web presentation copy','DECIMATE');mod.ratio=.012;bpy.ops.object.modifier_apply(modifier=mod.name)
m=obj.data;m.calc_loop_triangles();uv=m.uv_layers.active.data;pos=[];tex=[]
for t in m.loop_triangles:
 for li,vi in zip(t.loops,t.vertices):
  pos.extend([v*.001 for v in m.vertices[vi].co]);tex.extend(uv[li].uv[:])
assert np.isfinite(pos).all() and .25<np.ptp(np.array(pos).reshape(-1,3)[:,0])<.26
np.array(pos,dtype='<f4').tofile(str(out/'scan-position.bin'));np.array(tex,dtype='<f4').tofile(str(out/'scan-uv.bin'))
im=next(n.image for mat in obj.data.materials if mat and mat.use_nodes for n in mat.node_tree.nodes if n.type=='TEX_IMAGE' and n.image)
im=im.copy();w,h=im.size;scale=min(1,2048/max(w,h));im.scale(round(w*scale),round(h*scale));im.filepath_raw=str(out/'scan-texture.png');im.file_format='PNG';im.save()
(out/'scan-export.json').write_text(json.dumps({'vertices':len(pos)//3,'triangles':len(pos)//9,'units':'meters','axes':'Blender Z up','texture':list(im.size),'validation':'finite coordinates; width 250–260 mm; UV retained; source blend not saved'}))
print('EXPORT OK',len(pos)//9,flush=True)
