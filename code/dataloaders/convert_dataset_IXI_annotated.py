import numpy as np
from glob import glob
from tqdm import tqdm
import os
import h5py
import nibabel as nib
import image_utils
from skimage.color import rgb2grey
import matplotlib.pyplot as plt

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
    # for i in tqdm(range(1, 21)):
    #     image_file = f"../../data_ircad/ircad/3Dircadb1.{i}/maskedLiverIso.nii"
    #     label_file = f"../../data_ircad/ircad/3Dircadb1.{i}/vesselsIso.nii"
    #     mask_file = f"../../data_ircad/ircad/3Dircadb1.{i}/liverMaskIso.nii"
    #
    #     image = nib.load(image_file)
    #     image = image.get_fdata()
    #
    #     mask = nib.load(mask_file)
    #     mask = mask.get_fdata()
    #
    #     label = nib.load(label_file)
    #     label = label.get_fdata()
    #     label = label * mask
    #
    #     image = (image - np.mean(image)) / np.std(image)
    #     image = image.astype(np.float32)
    #     os.makedirs(f"../../data_ircad/synthetics_h5/ircad_{i}")
    #     f = h5py.File(f"../../data_ircad/synthetics_h5/ircad_{i}/mri_norm2.h5", 'w')
    #     f.create_dataset('image', data=image, compression="gzip")
    #     f.create_dataset('label', data=label, compression="gzip")
    #     f.create_dataset('mask', data=mask, compression="gzip")
    #     with open('../../data_ircad/synthetics_h5/train.list', 'a') as text:
    #         text.write(f"ircad_{i}\n")
    #     f.close()




    ################################# donnees 2D Synthetiques ##############################################
    # image_file = sorted(glob(f"../../data_synthetics_DRIVE/simulations/*"))
    # label_file = sorted(glob(f"../../data_synthetics_DRIVE/cco_modifie/*"))
    #
    # i = 0
    # for image_file, label_file in tqdm(zip(image_file, label_file)):
    #
    #     image = image_utils.read_image(image_file)
    #     label = image_utils.read_image(label_file)
    #     label= image_utils.normalize_image(label)
    #
    #     image = (image - np.mean(image)) / np.std(image)
    #     image = image.astype(np.float32)
    #     image_utils.show_image(image)
    #     image_utils.show_image(label)
    #
    #     plt.show()
    #     break
    #     os.makedirs(f"../../data_synthetics_DRIVE/datas_synth/synth_{i}")
    #     f = h5py.File(f"../../data_synthetics_DRIVE/datas_synth/synth_{i}/mri_norm2.h5", 'w')
    #     f.create_dataset('image', data=image, compression="gzip")
    #     f.create_dataset('label', data=label, compression="gzip")
    #     with open('../../data_synthetics_DRIVE/train.list', 'a') as text:
    #         text.write(f"synth_{i}\n")
    #     f.close()
    #     i += 1
    #
    #
    # # ######################################### DRIVE ########################################################
    # image_file = sorted(glob(f"../../data_synthetics_DRIVE/DRIVE/training/images/*")) +  sorted(glob(f"../../data_synthetics_DRIVE/DRIVE/test/images/*"))
    # label_file = sorted(glob(f"../../data_synthetics_DRIVE/DRIVE/training/1st_manual/*")) + sorted(glob(f"../../data_synthetics_DRIVE/DRIVE/test/1st_manual/*"))
    #
    # for i, j in zip(image_file, label_file):
    #     print(i)
    #     print(j)
    #     print()
    #
    # i = 0
    # for image_file, label_file in tqdm(zip(image_file, label_file)):
    #     image = image_utils.read_image(image_file)
    #     image = image_utils.normalize_image(rgb2grey(image))
    #     label = image_utils.read_image(label_file)
    #
    #     if len(label.shape) == 3:
    #         label = label[:,:,0]
    #     label = image_utils.normalize_image(label)
    #     image = (image - np.mean(image)) / np.std(image)
    #     image = image.astype(np.float32)
    #     image_utils.show_image(image)
    #     image_utils.show_image(label)
    #
    #     plt.show()
    #     # os.makedirs(f"../../data_synthetics_DRIVE/datas_synth/DRIVE_{i}")
    #     # f = h5py.File(f"../../data_synthetics_DRIVE/datas_synth/DRIVE_{i}/mri_norm2.h5", 'w')
    #     # f.create_dataset('image', data=image, compression="gzip")
    #     # f.create_dataset('label', data=label, compression="gzip")
    #     # # with open('../../data_synthetics_DRIVE/test.list', 'a') as text:
    #     # #     text.write(f"DRIVE_{i}\n")
    #     # # f.close()
    #     break
    #     i += 1
    # # ######################################### STARE ########################################################
    # image_file = sorted(glob(f"../../data_synthetics_DRIVE/STARE/im*.tif"))
    # label_file = sorted(glob(f"../../data_synthetics_DRIVE/STARE/gt*.tif"))
    # for i, j in zip(image_file, label_file):
    #     print(i)
    #     print(j)
    #     print()
    #
    # i = 0
    # for image_file, label_file in tqdm(zip(image_file, label_file)):
    #     image = image_utils.read_image(image_file)
    #     image = image_utils.normalize_image(rgb2grey(image))
    #     label = image_utils.read_image(label_file)
    #     if len(label.shape) == 3:
    #         label = label[:,:,0]
    #     label= image_utils.normalize_image(label)
    #     image = (image - np.mean(image)) / np.std(image)
    #     image = image.astype(np.float32)
    #     image_utils.show_image(image)
    #     image_utils.show_image(label)
    #
    #     plt.show()
    #     break
    #     os.makedirs(f"../../data_stare_drive/datas_synth/STARE_{i}")
    #     f = h5py.File(f"../../data_stare_drive/datas_synth/STARE_{i}/mri_norm2.h5", 'w')
    #     f.create_dataset('image', data=image, compression="gzip")
    #     f.create_dataset('label', data=label, compression="gzip")
    #     # with open('../../data_stare_drive/train.list', 'a') as text:
    #     #     text.write(f"STARE_{i}\n")
    #     # f.close()
    #     i += 1
    images_paths = sorted(glob(f"../../decath_ircad/decath/imagesTr/*"))
    labels_paths = sorted(glob(f"../../decath_ircad/decath/labelsTr/*"))
    i = 0
    for image_file,label_file in zip(images_paths, labels_paths):
        image = nib.load(image_file)
        image = image.get_fdata()

        label = nib.load(label_file)
        label = label.get_fdata()

        image = (image - np.mean(image)) / np.std(image)
        image = image.astype(np.float32)
        os.makedirs(f"../../decath_ircad/datas/decathlon_{i}")
        f = h5py.File(f"../../decath_ircad/datas/decathlon_{i}/mri_norm2.h5", 'w')
        f.create_dataset('image', data=image, compression="gzip")
        f.create_dataset('label', data=label, compression="gzip")
        with open('../../decath_ircad/train.list', 'a') as text:
            text.write(f"decathlon_{i}\n")
        f.close()
        i = i + 1

    for i in tqdm(range(1, 21)):
        image_file = f"../../data_ircad/ircad/3Dircadb1.{i}/patientIso.nii"
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
        os.makedirs(f"../../decath_ircad/datas/ircad_{i}")
        f = h5py.File(f"../../data_ircad/synthetics_h5/ircad_{i}/mri_norm2.h5", 'w')
        f.create_dataset('image', data=image, compression="gzip")
        f.create_dataset('label', data=label, compression="gzip")
        f.create_dataset('mask', data=mask, compression="gzip")
        with open('../../decath_ircad/train.list', 'a') as text:
            text.write(f"ircad_{i}\n")
        f.close()
        with open('../../decath_ircad/test.list', 'a') as text:
            text.write(f"ircad_{i}\n")
        f.close()

if __name__ == '__main__':
    covert_h5()