# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "datalad>=1.4.1",
#     "git-annex>=10.20260525",
# ]
# ///
from datalad import api as dl


def main() -> None:
    dataset = dl.Dataset('inputs/ds005365')
    derivs = dl.Dataset('inputs/ds005365-fmriprep')

    dataset.get('sub-CISC13877/func/sub-CISC13877_task-rest_dir-AP_run-01_bold.nii.gz')
    derivs.get('sub-CISC13877/anat/sub-CISC13877_from-T1w_to-MNI152NLin2009cAsym_mode-image_xfm.h5')
    derivs.get('sub-CISC13877/fmap')
    derivs.get('sub-CISC13877/func/sub-CISC13877_task-rest_dir-AP_run-01_from-orig_to-boldref_mode-image_desc-hmc_xfm.txt')
    derivs.get('sub-CISC13877/func/sub-CISC13877_task-rest_dir-AP_run-01_from-boldref_to-T1w_mode-image_desc-coreg_xfm.txt')
    derivs.get('sub-CISC13877/func/sub-CISC13877_task-rest_dir-AP_run-01_from-boldref_to-auto00000_mode-image_xfm.txt')


if __name__ == "__main__":
    main()
