import numpy as np
from glob import glob
from tqdm import tqdm
import h5py
import nrrd

def covert_h5():
    listt = glob('../../LA_dataset/2018LA_Seg_Training Set/*/lgemri.nrrd')
    for item in tqdm(listt):
        image, img_header = nrrd.read(item)
        label, gt_header = nrrd.read(item.replace('lgemri.nrrd', 'laendo.nrrd'))
        label = (label == 255).astype(np.uint8)

        image = (image - np.mean(image)) / np.std(image)
        print(image.shape)

        print(label.shape)
        f = h5py.File(item.replace('lgemri.nrrd', 'mri_norm2.h5'), 'w')
        f.create_dataset('image', data=image, compression="gzip")
        f.create_dataset('label', data=label, compression="gzip")
        f.close()

if __name__ == '__main__':
    covert_h5()