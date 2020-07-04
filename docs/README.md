
# The project 
This paper proposes a methodology to estimate stress in the subsurface by a hybrid method 
combining finite element modelling and neural networks. This methodology exploits the idea 
of obtaining a “multi-frequency solution” in the numerical modelling of systems whose behaviour
 involves a wide span of length scales. One “low-frequency” solution is obtained via inexpensive 
 finite element modelling at a coarse scale. The second solution provides the fine-grained 
 details introduced by the heterogeneity of the free parameters at the fine scale. 
 
 This “high-frequency” solution is estimated via neural networks pre-trained with partial 
 solutions obtained in high-resolution finite-element models. When the coarse finite element 
 solutions are combined with the neural network estimates, the results are within  a 2% 
 of error of the results that would be computed with high-resolution finite element models.
 The  paper discusses the benefits and drawbacks of the method and illustrates its applicability 
 via a worked example.

# This is an <h1> tag
## This is an <h2> tag
###### This is an <h6> tag

*This text will be italic*
_This will also be italic_

**This text will be bold**
__This will also be bold__

_You **can** combine them_


* Item 1
* Item 2
  * Item 2a
  * Item 2b


# Methodology   
![](/images/S1Example.PNG)
*Effective minimum principal stress σ_1. A: Cross horizontal section of the coarse model 
used for training. B: Cross horizontal section of the correct solution. 
C: Projections along a vertical line and zoomed-in view. Filled curve corresponds to 
the correct solution and the dashed line to the coarse model used for training. 


![](/images/network.PNG)
*Neural network used. Four independent 3D valid convolutions using a (2,2) kernel  
operated on s1,s2,E,ν, all sampled from 27 cells. Stress was sampled from coarse 
cells and E,ν were sampled from the high-resolution model. The outputs of the convolutions 
were flattened and merged with  pressure and overburden load and passed to a stage of  fully connected 
layers (see paper)

# Results 
![](/images/FrontPage2.png)
* Zoomed-in view of the fracture gradient projected on a vertical  plane. Coarse (left)  and high-resolution 
(middle) 3D finite element models and fracture gradient predictions in the 3D model (right).  



