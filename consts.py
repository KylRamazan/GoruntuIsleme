import pathlib,platform,os
figure_size=9
klasor=str(pathlib.Path.home())+ ('/Desktop' if platform.system().lower()=='windows' else '/Masaüstü')
resim_yolu=os.path.join(klasor,'Resimler')
veriseti_yolu=os.path.join(klasor,'Veriseti')
egitim_yolu=os.path.join(veriseti_yolu,'train')
validation_yolu=os.path.join(veriseti_yolu,'validation')
test_yolu=os.path.join(veriseti_yolu,'test')