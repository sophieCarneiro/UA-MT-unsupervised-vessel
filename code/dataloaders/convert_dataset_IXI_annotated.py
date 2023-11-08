import numpy as np
from glob import glob
from tqdm import tqdm
import os
import h5py
import nibabel as nib


def covert_h5():

    # for i in tqdm(range(316)):
    #     image_file = f"../../data_ircad/synthetics/label_{i}_rician_8.0.nii.gz"
    #     label_file = f"../../data_ircad/synthetics/label_{i}.nii.gz"
    #     # print(image_file)
    #     # print(label_file)
    #     # print()
    #
    #     image = nib.load(image_file)
    #     image = image.get_fdata()
    #
    #     label = nib.load(label_file)
    #     label = label.get_fdata()
    # #
    # #
    #     image = (image - np.mean(image)) / np.std(image)
    #     image = image.astype(np.float32)
    #     os.makedirs(f"../../data_ircad/synthetics_h5/data_{i}")
    #     f = h5py.File(f"../../data_ircad/synthetics_h5/data_{i}/mri_norm2.h5", 'w')
    #     f.create_dataset('image', data=image, compression="gzip")
    #     f.create_dataset('label', data=label, compression="gzip")
    #     if i <= 290 :
    #         with open('../../data_ircad/synthetics_h5/train.list', 'a') as text:
    #                 text.write(f"data_{i}\n")
    #     else:
    #         with open('../../data_ircad/synthetics_h5/test.list', 'a') as text:
    #                 text.write(f"data_{i}\n")
    #     f.close()
    #
    for i in tqdm(range(1, 21)):
        image_file = f"../../data_ircad/ircad/3Dircadb1.{i}/maskedLiverIso.nii"
        label_file = f"../../data_ircad/ircad/3Dircadb1.{i}/vesselsIso.nii"
        mask_file = f"../../data_ircad/ircad/3Dircadb1.{i}/liverMaskIso.nii"

        image = nib.load(image_file)
        image = image.get_fdata()

        mask = nib.load(mask_file)
        mask = mask.get_fdata()

        label = nib.load(label_file)
        label = label.get_fdata()
        label = label * mask

        image = (image - np.mean(image)) / np.std(image)
        image = image.astype(np.float32)
        os.makedirs(f"../../data_ircad/synthetics_h5/ircad_{i}")
        f = h5py.File(f"../../data_ircad/synthetics_h5/ircad_{i}/mri_norm2.h5", 'w')
        f.create_dataset('image', data=image, compression="gzip")
        f.create_dataset('label', data=label, compression="gzip")
        f.create_dataset('mask', data=mask, compression="gzip")
        with open('../../data_ircad/synthetics_h5/train.list', 'a') as text:
            text.write(f"ircad_{i}\n")


    # #     item = item.replace('IXI-MRA', 'dataset')
    # #     item = item.replace('.nii.gz', '/mra_norm.h5')
    # #     os.makedirs(item.replace('/mra_norm.h5', ''))
    # #     f = h5py.File(item, 'w')
    # #     f.create_dataset('image', data=image, compression="gzip")
    # #     f.create_dataset('label', data=label, compression="gzip")
    # #     f.close()

if __name__ == '__main__':
    covert_h5()