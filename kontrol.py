import os,consts
def kontrol_et():
    if os.path.exists(consts.veriseti_yolu) is False:os.mkdir(consts.veriseti_yolu)
    if os.path.exists(consts.egitim_yolu) is False:os.mkdir(consts.egitim_yolu)
    if os.path.exists(consts.validation_yolu) is False:os.mkdir(consts.validation_yolu)
    if os.path.exists(consts.test_yolu) is False:os.mkdir(consts.test_yolu)