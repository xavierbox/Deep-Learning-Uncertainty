# Deep Learning for Uncertainty in Stress Modelling: (In progress)

## The project 
A challenge found in many areas of science and engineering is in the correlation of 3D spatial data collected 
at different scales. 

In <b> Environmental sciences </b> for instance, climate data is collected in local monitoring stations 
(fine and high-resolution scale) but that only provides information at discrete locations. For the prediction of temperature 
and rainfall everywhere else, some sort of interpolation is needed. We could argue that the information collected 
via satelite images and large scale simulators (that sometimes take days to run) can be used to fill the gaps as long as 
one could correlate these large-scale (planet-wide) information to the local and fine-grained scale. The problem is that 
it is not obvious how to do so. The large-scale models cover a vast area but the resolution is coarse. The local stations provide 
a finer time and space resolution (sometimes) but cover little extent. 

The aforementioned problem is found everywhere in science and engineering. In  <b> Geotecnics </b> we basically need to 
change the name of the variables (temperature to stress) and the problem is the same. Modelling stress at different 
length scales will be the objective of this project. The methodology presented, however, is of general application. At present, 
an ongoing project is exploring the potential of applying this technique with some adaptations in finance. 

##### Method  

This project proposes a methodology to estimate 3D geo-spatial field (such as stress in the subsurface) by a hybrid 
method combining finite element modelling and neural networks. 

This methodology exploits the idea of obtaining a “multi-frequency solution”. 
One “low-frequency” solution is obtained via inexpensive finite element modelling at a coarse scale. 
The second solution provides the fine-grained details introduced by the heterogeneity of the free 
parameters at the fine scale. 
 
This “high-frequency” solution is estimated via neural networks pre-trained with partial 
solutions obtained in high-resolution finite-element models. Such a model is indeed a transformation rule 
in-between scales. If found, it can be applied to the large-scale solutions to predict the high-resolution 
information. 

Preliminary results obtained are within  a 2% of error. 


<b>There is a draft paper that can be found here:</b> 
 <a href="https://drive.google.com/file/d/1vew6OoRC5vxERwdCl27J2xvy-yxNpib0/view?usp=sharing">
Physics-Informed Neural Networks for Multi-Scale Stress Modelling in Geological Structures
</a>
 
 
 
## Methodology   
![](/images/network.PNG)
<p>Neural network used. Four independent 3D valid convolutions using a (2,2) kernel  
operated on stress and mechanical properties in 3D. Stress was sampled from coarse 
cells and E,ν were sampled from the high-resolution model. The outputs of the 
convolutions were flattened and merged with  pressure and overburden load and passed 
to a stage of  fully connected layers (see paper)</p>

##### Preliminary results  
![](FrontPage2.png)
<p>Effective minimum principal stress σ_1. A: Cross horizontal section of the coarse 
model used for training. B: Cross horizontal section of the correct solution. 
C: Projections along a vertical line and zoomed-in view. Filled curve corresponds 
to the correct solution and the dashed line to the coarse model used for training. 
</p>
  
## How to reproduce these results, or how to apply the method in other fields?

### Data Processing. Workflow step 1
![](/images/raw_data_step1.PNG)

In this project the data comes straingt from a software package in a legacy uncompressed format GRDCL. The data is in good shape so little manipulaion 
is needed but this step is clearly unique to details of the input. The main output is the data in a more standrd format that we can work with later. 
In the notebook, the input files are parsed via a class created for this project. The parsing converts the information inside the files into several pandas dataframes for easy processing later. The parser in itself just have one static method that receives as a string the input file and returns a data frame:

```python
class EclipseFileParser:
    
    @staticmethod 
    def PetrelEclipseKeywords_to_pandas( file_name :str  )->pd.DataFrame:
    ...
```

This is called near the top of the notebook 

```python
data_raw = EclipseFileParser.PetrelEclipseKeywords_to_pandas( data_file );
```

Although the data is in good shape, some minimal checking and processing is still due. 
Here is one example of the code in the notebook performing a basic check. 

```python

(...)
eff=[ data_raw[col] for col in data_raw.columns if "POISS" in col ]
print( f"Any out-of-range Poisson's ratio? { is_condition(eff, lambda item: any(item <0.1) or any(item >0.5)  ) } ")
(...)

```
Finally the code stores the pre-processed data as a feather.
```python
 %time data_raw.to_feather(output_file_name)
```

Once all the files are stored as feathers, the workflow continues with extra pre-processing steps before the data 
is in the format needed for the neural network training. 

#### The full workflow is long. It will be published here little by little. 
