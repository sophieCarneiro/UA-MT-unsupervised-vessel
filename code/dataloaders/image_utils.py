"""
Copyright or © or Copr. Odyssee Merveille (2019)
odyssee.merveille@gmail.com

This software is a computer program whose purpose is to reproduce the results 
of the article "nD variational restoration of curvilinear structures with 
prior-based directional regularization", O. Merveille, B. Naegel, H. Talbot 
and N. Passat, IEEE Transactions on Image Processing, 2019
https://hal.archives-ouvertes.fr/hal-01832636.

This software is governed by the CeCILL license under French law and
abiding by the rules of distribution of free software.  You can  use, 
modify and/ or redistribute the software under the terms of the CeCILL
license as circulated by CEA, CNRS and INRIA at the following URL
"http://www.cecill.info". 

As a counterpart to the access to the source code and  rights to copy,
modify and redistribute granted by the license, users are provided only
with a limited warranty  and the software's author,  the holder of the
economic rights,  and the successive licensors  have only  limited
liability. 

In this respect, the user's attention is drawn to the risks associated
with loading,  using,  modifying and/or developing or reproducing the
software by the user in light of its specific status of free software,
that may mean  that it is complicated to manipulate,  and  that  also
therefore means  that it is reserved for developers  and  experienced
professionals having in-depth computer knowledge. Users are therefore
encouraged to load and test the software's suitability as regards their
requirements in conditions enabling the security of their systems and/or 
data to be ensured and,  more generally, to use and operate it in the 
same conditions as regards security. 

The fact that you are presently reading this means that you have had
knowledge of the CeCILL license and that you accept its terms.
"""

import math 
import numpy as np
import nibabel as nib
from PIL import Image
import matplotlib.pylab as plt
import os
from glob import glob

def read_image(path):
    image = Image.open(path)
    return np.array(image)


def save_image(image, output_path):
	image_pil = Image.fromarray(image)
	image_pil.save(output_path)


def normalize_image(image):
    maxi = np.amax(image)
    mini = np.amin(image)
    image_norm = (image.astype(np.float64) - mini) / (maxi - mini)
    return image_norm
