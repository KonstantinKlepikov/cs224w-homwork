import os
import matplotlib.pyplot as plt
from .core_paths import IMAGES_PATH

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    """
    Save ploting by matplotlib images
    
    Parameters
    ----------
    :param fig_id:
    Name of saving image
        str
    
    :param tight_layout:

        default True

    :param fig_extension:
    Extension of image
        str, default png

    :param resolution:
    Dpi resolution of saved image
        int, default 300
    """
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)