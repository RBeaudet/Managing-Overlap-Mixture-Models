# Managing-Overlap-Mixture-Models

We propose an implementation of the Infinite Overlapping Mixture Model as described in the article <a href="http://mlg.eng.cam.ac.uk/zoubin/papers/HelGha07over.pdf">A non parametric Bayesian approach to modelling overlapping clusters</a>, by Katherine A. Heller and Zoubin Ghahramani.

## Abstract

<i> From the original paper</i>

Although clustering data into mutually exclusive partitions has been an extremely successful approach to unsupervised learning, there are many situations in which a richer model is needed to fully represent the data. This is the case in problems where data points actually simultaneously belong to multiple, overlapping clusters. For example a particular gene may have several functions, therefore belonging to several distinct clusters of genes, and a biologist may want to discover these through unsupervised modeling of gene expression data. 

We present a new nonparametric Bayesian method, the <b>Infinite Overlapping Mixture Model (IOMM)</b>, for modeling overlapping clusters. The IOMM uses exponential family distributions to model each cluster and forms an overlapping mixture by taking products of such distributions, much like products of experts (Hinton, 2002). The IOMM allows an unbounded number of clusters, and assignments of points to (multiple) clusters is modeled using an Indian Buffet Process (IBP), (Griffiths and Ghahramani, 2006). 

The IOMM has the desirable properties of being able to focus in on overlapping regions while maintaining the ability to model a potentially infinite number of clusters which may overlap. We derive MCMC inference algorithms for the IOMM and show that these can be used to cluster movies into multiple genres.
