# fMRIPrep minimal derivatives resampling demo

This repository was created for the OHBM 2026 educational session
*The Research Lifecycle: A Primer on Open and Sustainable Science Practices*.

The purpose of this repository is to demonstrate how to use fMRIPrep's minimal derivatives
in multiple ways.

To get started, you must install the [DataLad][] subdatasets and retrieve
the relevant data:

```console
git submodule update --init
uv run ./code/fetch-data.py
```

You can then run the Jupyter notebook with:

```console
uv run jupyter-lab
```

Open `resample.ipynb` and walk through the code cells.
This notebook demonstrates using fMRIPrep's minimal derivatives to resample BOLD
data from the raw dataset to a common space (MNI152NLin2009cAsym).
This code, or code like it, can be a part of a larger script or workflow,
which resamples the data into only the spaces needed for that particular analysis.

## Generating full derivatives from minimal

There are also workflows that expect to have full fMRIPrep derivatives available.
It is possible to generate them from the minimal derivatives, taking advantage of
the work that's already been done.

```console
uvx fmriprep-docker inputs/ds005365 outputs/ds005365-fmriprep-full participant \
  --derivatives fmriprep=inputs/ds005365-fmriprep \
  --fs-subjects-dir=inputs/ds005365-fmriprep/sourcedata/freesurfer --fs-no-resume \
  --output-spaces MNI152NLin2009cAsym
```

This is not as efficient as resampling only the data needed, but sometimes practicality wins.

TODO:

* Add/update fetch script to retrieve enough data to run fMRIPrep with minimal
  derivatives as inputs.
