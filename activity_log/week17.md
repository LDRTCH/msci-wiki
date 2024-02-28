# Week 16

# 0. Table of Contents

# 1. Introduction



# 2. Story

The aim of the second part of our project was to generate neural network automatised recovery of intrinsic properties within our persistent exclusion process system by evaluating experimental data. The motivation is twofold: pragmatically, the aim is to provide a proof of concept engineering of a tool which can evaluate and identify active matter systems. To this end, generalisation of phenomena is key; such a neural network should be able to adapt to a vast variation of parameters, namely tumbling rates, densities and sample sizes. Furthermore, there is a theoretical component to the utility of this research - on one hand, a machine learning algorithm reproducing the inherent tumbling quantity of a system can serve as external validation of active matter phenomena; with the caveat, of course, that this external validation (by which we mean externalised, removed from human judgement) is nonetheless trained and verified with human-set metrics and understanding.** On the other hand, obtaining a generalised and automated tool for evaluating active matter systems can point human focus to the interesting regions of behaviour, thus supplementing analytical examination.**

The algorithm returns various predictions for every tumbling-density-size system it is applied to; these predictions have a spread, which we intend to lower and center around the real tumbling rate, but nonetheless it is important to note that it does not provide a discrete singular prediction. One goal is to qualitatively evaluate the distributions of predictions, with the hopes of a gaussian-like organisation centred on the actual tumbling rate. In this sense the algorithm exhibits human-like prediction. The crux of the issue is determining satisfactory metrics for evaluating the systems. The goal, however, is not to perfectly fine-tune the system as much as to make it applicable enough in order to highlight different qualitative distinctions and how they influence the algorithm's output - with the explicit intent to link to qualitative phenomena which we have examined in the first part of our project.

##### 1. Degrees of freedom
One of the important explorations is examining how changing the input degrees of freedom alters the machine output. By degrees of freedom, we specifically mean positions and orientations - the CNN can be fed either 'experiment-like' images, which present only black and white displays of our active matter system, and thus only allows the network to extrapolate on positions, or it can be fed afferent orientations as well, as colours for each particle, and henceforth weight its parameters with this extra difference. We can then explore how training the CNN on one degree of freedom setup influences its predictions on the other. Our expectations going in are that:

- training the CNN on strictly positions will have similar predictions when validating it on positions+orientations; this is because it will/might simply approach the coloured landscape the same way it approaches the monochrome landscape, by contrasting existing particles with the black background. 
- training the CNN on positions and orientations will have worse preditions when validating it just on positions; this is because, having been trained to recognise colour and incorporate it in predictions, the system might struggle to 'explain' the images which now lack this degree of freedom

If these expectations prove to be correct, training the CNN on positions+orientations might be a worse prospect, due to most real life applications/evaluations of active matter not being able to access the orientation of agents through still images. Nonetheless, training on positions+orientations may give the CNN a better insight into the clustering phenomenon as a whole, due to the role particle orientations play in cluster formation and evaporation.

misinformation extension - janus particles rolling in 2d

SPRINKLES

##### 2. Predicting novel tumbling rates

Another important exploration is how training on a certain set of tumbling rates can then cause the CNN to be able to accurately predict tumbling rates in different regions. Our preliminary experiments have not been able to replicate such results - attempting to predict tumbling rates spaced out inbetween the training tumbling rates has caused the system to attempt to fit its predictions to the neighbouring training rates, and therefore given a very large spread to the data. This may however be strictly due to the low training data we have given the CNN so far - both low amount of original evolutions to give the system more depth of experience, as well as low amount of distinct tumbling rates. It ma

Here are our expectations regarding this part of the project:

- Using interspersed sets of training/validation will yield accurate predictions (on the validation samples) provided the spacing between values is low enough.

- Using vastly separated sets is going to fare poorly in prediction, due to different clustering behaviour which the CNN is not adequately accustomed to.
 
##### 3. Predicting novel densities

Training on a certain set of densities will

We have experimented with various architecture models (a summary of the different architectures can be found [here](./../models.qmd)).








A noteworthy extension of our research is to then apply this neural network to real active matter systems by 'translating'  physical scenarios into the visual language our tool is familiar with.

to recover patterns

MONOCHROME
if img > 0
img = 1



