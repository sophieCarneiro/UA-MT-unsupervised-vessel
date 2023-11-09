import image_utils
from skimage.color import rgb2grey
from skimage.filters import median
from skimage.morphology import disk
import numpy as np
from skimage.morphology import skeletonize
from skimage.filters import threshold_otsu
from scipy.ndimage import distance_transform_bf
from glob import glob

image_paths = sorted(glob("../../data_synthetics_DRIVE/STARE/im*.tif"))
cco_files = sorted(glob(f"../../data_synthetics_DRIVE/cco_modifie/img_*.png"))
cco_mask_files = sorted(glob(f"../../data_synthetics_DRIVE/mask_fov/mask_*.png"))

for image_path, cco_file, cco_mask_file in zip(image_paths, cco_files, cco_mask_files):
    kernel_radius = 10
    image = image_utils.read_image(image_path)
    grey_image = image_utils.normalize_image(rgb2grey(image))

    grey_int16 = (grey_image * 255).astype(np.int16)

    # #Substract the background
    bg_substract = median(grey_int16, disk(kernel_radius))
    bg_substract[bg_substract<0] = 0

    # # Apply the FOV mask
    background = bg_substract

    #Extend the dynamic between 0 and 255
    background = image_utils.normalize_image(background) * 255



    vessels = image_utils.read_image(cco_file)
    cco_mask= image_utils.read_image(cco_mask_file)

    # pretraitement fond de retine
    background = background + np.random.normal(loc = 0, scale = 5, size = background.shape)
    background[background>255] = 255

    (w, h) = background.shape

    w1 = int(round((w - vessels.shape[0]) / 2.))
    h1 = int(round((h -  vessels.shape[1]) / 2.))

    background = background[w1:w1 +  vessels.shape[0], h1:h1 + vessels.shape[1]]

    kernel_radius = 2
    distance_map = distance_transform_bf(vessels, 'chessboard')
    distance_map =  median(distance_map, disk(kernel_radius))
    value = image_utils.normalize_image(vessels) * background
    new_vessels = np.zeros(vessels.shape)
    print(distance_map.max())
    print(distance_map.min())
    for i in range(vessels.shape[0]):
        for j in range(vessels.shape[1]):
            if vessels[i, j] != 0:
                new_vessels[i, j] = distance_map[i, j] * np.random.normal(loc = 30, scale = 5)
            if vessels[i, j] != 0 and  new_vessels[i, j] == 0:
                new_vessels[i, j] = np.random.normal(loc = 15, scale = 2)


    kernel_radius = 1
    new_vessels = median(new_vessels, disk(kernel_radius))

    background = background - new_vessels
    background = background * image_utils.normalize_image(cco_mask)
    background[background<0] = 0
    print(cco_file.split('/')[-1][-6:-4])
    output_path = f"../../data_synthetics_DRIVE/simulations/simulation_{cco_file.split('/')[-1][-6:-4]}.png"

    image_utils.save_image(background.astype(np.uint8), output_path)
